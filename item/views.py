from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm, CommentForm
from .models import Category, Item, Comment
from django.core.paginator import Paginator


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })



def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    comments = item.comments.filter(parent__isnull=True)


    related_items = Item.objects.filter(category=item.category).exclude(pk=item.pk)[:6]


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.user = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent_id = int(parent_id)
            comment.save()
            return redirect('item:detail', pk=pk)
    else:
        form = CommentForm()


    paginator = Paginator(comments, 5)
    page = request.GET.get('page')
    comments_paginated = paginator.get_page(page)

    return render(request, 'item/detail.html', {
        'item': item,
        'form': form,
        'comments': comments_paginated,
        'related_items': related_items,  # <-- Pass this to template
    })




@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


def browse_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    items = Item.objects.filter(category=category, is_sold=False)
    categories = Category.objects.all()  # ✅ Add this
    return render(request, 'item/category.html', {
        'category': category,
        'items': items,
        'categories': categories,  # ✅ So the bottom category list works
    })


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.user == request.user:
        item_id = comment.item.id
        comment.delete()
        return redirect('item:detail', pk=item_id)

    return redirect('item:detail', pk=comment.item.id)


@login_required(login_url='core:login')  # redirect to login if not logged in
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)


    if request.user != comment.user:
        return redirect('item:detail', pk=comment.item.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=comment.item.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'item/edit_comment.html', {
        'form': form,
        'comment': comment
    })
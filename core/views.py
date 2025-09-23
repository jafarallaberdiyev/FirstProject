from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import login
from item.models import Category, Item
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime
from django.contrib import messages
from django.contrib.auth.models import User

from .models import UserProfile


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')


def privacy(request):
    return render(request, 'core/privacy.html')


def terms(request):
    return render(request, 'core/terms.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('core:index')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')
        else:
            print("Form validation errors:", form.errors)
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    authentication_form = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:index')  # or your home page
        return super().dispatch(request, *args, **kwargs)


class LogoutViewAllowGet(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



@login_required
def profile(request):
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()

        profile.phone = request.POST.get('phone', '')
        profile.birthdate = request.POST.get('birthdate') or None
        profile.gender = request.POST.get('gender', '')
        profile.save()

        return redirect('core:profile')

    return render(request, 'core/profile.html', {
        'user': user,
        'profile': profile
    })


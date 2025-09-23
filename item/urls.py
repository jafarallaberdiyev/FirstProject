from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('category/<int:pk>/', views.browse_by_category, name='category'),
    path('comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('comments/<int:pk>/edit/', views.edit_comment, name='edit_comment'),

]

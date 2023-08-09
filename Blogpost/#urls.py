#urls.py

from django.contrib.auth import views as auth_views
from django.urls import path
from posts.views import PostListView, PostDetailView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    # ...
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    # ...
]

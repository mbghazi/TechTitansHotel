"""
Definition of urls for TechTitansHotel2.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    # Application-specific URLs
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),

    # Authentication-related URLs
    path('login/',
         LoginView.as_view(
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context={'title': 'Log in'}
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # Admin URL
    path('admin/', admin.site.urls),
]

from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from rest_framework.routers import DefaultRouter
from app.views import RoomViewSet, RoomListCreateView
from django.urls import path, include

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    # Application-specific URLs
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    # API URLs
    path('api/', include(router.urls)),
    path('api/room-list/', RoomListCreateView.as_view(), name='room-list-create'),

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

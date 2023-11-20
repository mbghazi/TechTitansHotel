from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from app import views
from app.forms import BootstrapAuthenticationForm
from app.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('login/',
         LoginView.as_view(
             template_name='app/login.html',
             authentication_form=BootstrapAuthenticationForm,
             extra_context={'title': 'Log in'}
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/', include('app.urls')),
]

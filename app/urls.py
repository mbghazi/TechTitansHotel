from django.urls import path, include
from .views import RoomListCreateView, RoomViewSet
from rest_framework.routers import DefaultRouter
from .views import RegisterView
from rest_framework import routers
from . import views
from django.urls import path, include


router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('room-list/', RoomListCreateView.as_view(), name='room-list'),
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'), 
    path('api/', include(router.urls)),

]

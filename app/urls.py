from django.urls import path, include
from .views import RoomListCreateView, RoomViewSet
from rest_framework.routers import DefaultRouter
from .views import RegisterView

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('room-list/', RoomListCreateView.as_view(), name='room-list'),
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'), 
    
]

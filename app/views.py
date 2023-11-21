from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpRequest
from .models import Room
from .forms import ReservationForm
from rest_framework import viewsets
from .serializers import RoomSerializer
from rest_framework import generics
from .serializers import RoomSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.views.generic import View
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.urls import path, include



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('api/', include(router.urls)),
]

class ConciergeOnlyView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='concierge').exists()

    def handle_no_permission(self):
        return HttpResponseForbidden("WARNING:You do not have permission to access this page!")


@login_required
def some_view(request):
    if not request.user.groups.filter(name='concierge').exists():
        return HttpResponseForbidden("WARNING: You do not have permission to access this page!")


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'app/register.html'
    def form_valid(self, form):
        user = form.save()
        role = form.cleaned_data.get('role')
        group = Group.objects.get(name=role)
        user.groups.add(group)
        return super().form_valid(form)


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


def home(request):
    is_concierge = request.user.groups.filter(name='concierge').exists()
    return render(
        request,
        'app/layout.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'is_concierge': is_concierge,  # Pass a simple boolean variable
        }
    )


def contact(request):
    """Renders the contact page."""
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'app/room_list.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.save()
            return redirect('room_detail', room_id=room.id)
    else:
        form = ReservationForm()
    
    return render(request, 'app/room_detail.html', {'room': room, 'form': form})


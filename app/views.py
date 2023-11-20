from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import Room
from .forms import ReservationForm
from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer



def home(request):
    """Renders the home page."""
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
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

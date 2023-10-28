from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Room

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
    return render(request, 'app/room_detail.html', {'room': room})

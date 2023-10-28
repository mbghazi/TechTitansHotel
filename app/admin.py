from django.contrib import admin
from .models import Room, Guest, Reservation, Service

admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Service)

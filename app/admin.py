from django.contrib import admin
from .models import Room, Guest, Reservation, Service

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price_per_night', 'is_available')
    search_fields = ('room_number', 'room_type')

class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('guest', 'room', 'check_in', 'check_out')
    search_fields = ('guest__first_name', 'guest__last_name', 'room__room_number')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

admin.site.register(Room, RoomAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Service, ServiceAdmin)

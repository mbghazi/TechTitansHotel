from rest_framework import serializers
from .models import Room, Guest, Reservation, RoomService, GeneralService, ReservationService

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'price_per_night', 'is_available']

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'first_name', 'last_name', 'email']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'guest', 'room', 'check_in_date', 'check_out_date']

class RoomServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomService
        fields = ['id', 'room', 'service', 'date', 'quantity']

class GeneralServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralService
        fields = ['id', 'guest', 'service_type', 'price', 'description']

class ReservationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationService
        fields = ['id', 'reservation', 'service', 'date', 'quantity']


"""
Definition of models.
"""

from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Room {self.room_number} - {self.room_type}'

class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    def calculate_total_price(self):
        total_price = self.room.price_per_night * (self.check_out_date - self.check_in_date).days
        services = ReservationService.objects.filter(reservation=self)
        for service in services:
            total_price += service.service.price * service.quantity
        return total_price

    def __str__(self):
        return f"Reservation for {self.guest} - Room {self.room}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class RoomService(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.service.name} for Room {self.room.room_number} on {self.date}"


class ReservationService(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)  # Using string reference to avoid errors
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.service.name} for Reservation {self.reservation.id}"


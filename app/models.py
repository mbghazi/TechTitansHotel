"""
Definition of models.
"""

from django.db import models
from django.utils import timezone


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
    def calculate_total_cost(self):
        room_cost = self.room.price_per_night  
        service_costs = sum([service.price for service in self.room.roomservice_set.all()])
        return room_cost + service_costs          

    def __str__(self):
        return f"Reservation for {self.guest} - Room {self.room}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class RoomService(models.Model):
    SERVICE_TYPES = [
        ('LAUNDRY', 'Laundry'),
        ('TAXI', 'Taxi Service'),
        ('FOOD', 'Food/Drink'),
    ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES, default='LAUNDRY')
    requested_time = models.DateTimeField(default=timezone.now)    
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.service.name} for Room {self.room.room_number} on {self.date}"    

class GeneralService(models.Model):
    SERVICE_TYPES = [
        ('TAXI', 'Taxi Service'),
     ]
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

class ReservationService(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.service.name} for Reservation {self.reservation.id}"


from django.db import models


# Ambulance Booking Model

class Booking(models.Model):

    AMBULANCE_TYPES = [

        ('ICU Ambulance', 'ICU Ambulance'),

        ('Oxygen Ambulance', 'Oxygen Ambulance'),

        ('Emergency Ambulance', 'Emergency Ambulance'),

    ]

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    pickup_location = models.TextField()

    emergency_type = models.CharField(
        max_length=50,
        choices=AMBULANCE_TYPES
    )

    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Contact Model

class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
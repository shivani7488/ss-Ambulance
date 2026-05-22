from django.contrib import admin
from .models import Booking, Contact


# Booking Admin

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'phone',
        'emergency_type',
        'booking_date'
    )

    search_fields = (
        'name',
        'phone',
        'emergency_type'
    )

    list_filter = (
        'emergency_type',
        'booking_date'
    )

    ordering = ('-booking_date',)


# Contact Admin

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'created_at'
    )

    search_fields = (
        'name',
        'email'
    )

    list_filter = (
        'created_at',
    )

    ordering = ('-created_at',)
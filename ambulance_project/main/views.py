from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Booking

def booking(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        phone = request.POST.get('phone')

        pickup_location = request.POST.get('pickup_location')

        emergency_type = request.POST.get('emergency_type')

        Booking.objects.create(

            name=name,
            phone=phone,
            pickup_location=pickup_location,
            emergency_type=emergency_type

        )

        return redirect('/')

    return render(request, 'booking.html')

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def gallery(request):
    return render(request,'gallery.html')

def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    return render(request,'home.html')

def hero(request):
    return render(request,'hero.html')
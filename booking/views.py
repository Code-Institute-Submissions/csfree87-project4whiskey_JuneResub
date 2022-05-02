from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')


def bookings(request):
    return render(request, 'bookings.html')

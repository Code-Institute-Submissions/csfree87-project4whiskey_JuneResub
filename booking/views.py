from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')


def bookings(request):
    return render(request, 'bookings.html')


def detail(request):
    return render(request, 'booking_detail.html')


def form(request):
    return render(request, 'booking_form.html')


def list(request):
    return render(request, 'booking_list.html')

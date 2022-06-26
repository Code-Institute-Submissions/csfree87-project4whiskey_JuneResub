from django.shortcuts import render
from django.db import models
from booking.models import GuestInfo
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from unicodedata import normalize


def home(request):
    return render(request, 'home.html')


def menu(request):

    return render(request, 'menu.html')


def bookings(request):

    return render(request, 'bookings.html')

def confirmation(request):

    return render(request, 'confirmation.html')


def contact(request):

    return render(request, 'contact.html')


from .forms import UserModelForm

# add to your views

def GuestInfo(request):
    form = UserModelForm()
    args = {}
    if request.method == 'POST':
        form = UserModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            users = GuestInfo.objects.all()

            return render(request, 'confirmation.html', {'users': users})


    else:
        form_class = UserModelForm
    args['form'] = form

    return render(request, 'booking.html', args)

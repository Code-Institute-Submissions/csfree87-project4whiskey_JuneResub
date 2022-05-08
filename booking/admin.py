from django.contrib import admin
from booking.models import GuestInfo
from booking.forms import UserModelForm

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    fields = ['BookingName', 'Guests', 'Day', 'Email']

admin.site.register(GuestInfo, BookingAdmin)

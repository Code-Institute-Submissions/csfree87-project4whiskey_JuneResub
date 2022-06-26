from django import forms
from django.forms import ModelForm
from booking.models import GuestInfo
from unicodedata import normalize
from django.core.exceptions import ValidationError

class UserModelForm(forms.ModelForm):

    class Meta:
        model = GuestInfo
        fields = ['BookingName', 'Guests', 'Day', 'Email']

    def clean_BookingName(self):
        BookingName = self.cleaned_data.get('BookingName')

        if ('BookingName' == ''):
            raise ValidationError('Please enter a booking name.')

        return BookingName

    def clean_Guests(self):
        Day = self.cleaned_data.get('Day')
        Guests = self.cleaned_data.get('Guests')

        if (Day == ""):
            raise ValidationError("Please select a day.")

        if (Guests == ""):
            raise ValidationError("Please enter number of guests.")

        return Day

from django.forms import ModelForm
from booking.models import GuestInfo
from django import forms
from unicodedata import normalize
from django.core.exceptions import ValidationError

class UserModelForm(ModelForm):

    class Meta:
        model = GuestInfo
        fields = ['BookingName', 'Guests', 'Day', 'Email']
        
    def clean_BookingName(self): 
        BookingName = self.cleaned_data.get('BookingName')

        if ('BookingName' == ''):
            raise ValidationError('Please enter a booking name.')

        for instance in GuestInfo.objects.all():
            if instance.BookingName == BookingName:
                raise ValidationError(BookingName + ' already has a booking.')
        return BookingName

    def clean_Guests(self):
        Day = self.cleaned_data.get('Day')
        Guests = self.cleaned_data.get('Guests')
      
        if (Day == ""):
            raise ValidationError("Please select a day.")

        if (Guests == ""):
            raise ValidationError("Please enter number of guests.")

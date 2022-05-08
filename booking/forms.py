from django.forms import ModelForm
from booking.models import UserDetails

class UserModelForm(ModelForm):

    class Meta:
        model = UserDetails
        fields = ['BookingName', 'Guests', 'Day', 'Email']

    if (BookingName == ""):
        raise ValidationError('Please enter a booking name.')

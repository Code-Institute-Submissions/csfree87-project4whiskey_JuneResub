from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


DAY_CHOICES = (
    ('Wednesday', 'WEDNESDAY'),
    ('Thursday', 'THURSDAY'),
    ('Friday', 'FRIDAY'),
    ('Saturday', 'SATURDAY'),
)


class GuestInfo(models.Model):

    BookingName = models.CharField(max_length=100,help_text='Probably the surname of your party.',blank=True)
    Guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)],default='1',help_text='Due to current government reulations this has a maximum value of 6.',blank=True)
    Email = models.EmailField(max_length=254,help_text='Please provide email in case of cancellation.')
    Day = models.CharField(max_length=9,choices=DAY_CHOICES,blank=True)


    def __str__(self):
        return self.BookingName

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class GuestInfo(models.Model):
    BookingName = models.CharField(max_length=100,help_text='Probably the surname of your party.',blank=True)
    Guests = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)],default='1',blank=True)
    Email = models.EmailField(max_length=254,help_text='Please provide email for confirmation.')
    Day = models.DateField(null=False, blank=False)


    def __str__(self):
        return self.BookingName

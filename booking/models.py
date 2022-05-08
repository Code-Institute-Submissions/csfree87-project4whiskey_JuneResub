from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


DAY_CHOICES = (
    ('Wednesday', 'WEDNESDAY'),
    ('Thursday', 'Thursday'),
    ('Friday', 'FRIDAY'),
    ('Saturday', 'SATURDAY'),
)

class UserDetails(models.Model):

    BookingName = models.CharField(max_length=100,help_text='Recommended use of Surname.',blank=True)
    Guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)],default='1',blank=True)
    Email = models.EmailField(max_length=254,help_text='Confirmations of reservations will be made by 12:00 noon of \
        each open day. Tables provided on a first come first serve basis.')
    Day = models.CharField(max_length=9,choices=DAY_CHOICES,blank=True)


    def __str__(self):
        return self.BookingName

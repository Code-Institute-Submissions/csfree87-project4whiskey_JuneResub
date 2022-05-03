from django.urls import path
from. import views

urlpatterns = [

    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('bookings/', views.bookings, name='bookings'),
    path('booking_detail/', views.detail, name='booking_detail'),
    path('booking_form/', views.form, name='booking_form'),
    path('booking_list/', views.list, name='booking_list'),

]

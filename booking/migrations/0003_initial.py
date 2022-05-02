# Generated by Django 4.0.4 on 2022-05-02 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0002_auto_20220502_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barbershop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Barbershopname', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('area', models.CharField(max_length=100, null=True)),
                ('service', models.CharField(choices=[('Only haircuts', 'Only haircuts'), ('all services', 'all services')], max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('email', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time', models.CharField(choices=[('Morning', 'Morning'), ('Lunch Time', 'Lunch Time'), ('Evening', 'Evening'), ('Night', 'Night')], max_length=200, null=True)),
                ('status', models.CharField(choices=[('Haircut and Shaving 10$', 'Haircut and Shaving 10$'), ('Haircut and Trimming 8$', 'Haircut and Trimming 8$'), ('Haircut 7$', 'Haircut 7$')], max_length=200, null=True)),
                ('barbershop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.barbershop')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.customer')),
            ],
        ),
    ]

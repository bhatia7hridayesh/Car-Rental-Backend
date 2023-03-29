# Generated by Django 4.1.7 on 2023-03-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_bookings_log',
            name='booked_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='vehicle_bookings_log',
            name='returned_on',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
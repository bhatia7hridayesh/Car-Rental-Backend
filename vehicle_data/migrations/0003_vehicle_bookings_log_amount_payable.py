# Generated by Django 4.1.7 on 2023-03-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_data', '0002_vehicle_bookings_log_booked_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_bookings_log',
            name='amount_payable',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
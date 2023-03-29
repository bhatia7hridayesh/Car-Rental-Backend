from django.db import models
from authentication_app.models import User
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import pre_save
# Create your models here.


class Vehicle(models.Model):
    agency = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Vehicle_model = models.CharField(max_length=50)
    Vehicle_number = models.CharField(max_length=15, unique=True)
    seating_capacity = models.IntegerField(default=5)
    rent_per_day = models.IntegerField()
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return self.Vehicle_number

class Vehicle_Bookings_Log(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    booked_on = models.DateTimeField(default=timezone.now)
    returned_on = models.DateTimeField(null=True, blank=True, default=None)
    amount_payable = models.IntegerField(null=True, blank=True)
    class  Meta:
        verbose_name = "Vehicle's Bookings Log"
        verbose_name_plural = "Vehicle's Bookings Logs"



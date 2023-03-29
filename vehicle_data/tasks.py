from .models import Vehicle_Bookings_Log
from django.utils import timezone
def delete_expired_discounts():
    current_time = timezone.now()
    end_of_rent = Vehicle_Bookings_Log.objects.filter(returned_on = current_time)
    for log in end_of_rent:
        vehicle = log.vehicle
        vehicle.is_booked = False
        vehicle.save()
    
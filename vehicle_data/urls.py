from django.urls import path
from .views import *
urlpatterns = [
    #Agency URLS
    path("create/", Create_Vehicle.as_view()),
    path("agency-vehicles/", My_Vehicles.as_view()),
    path("booking-history/", Bookings_history.as_view()),
    path("update-vehicle/<int:pk>", Update_Vehicle.as_view()),
    #User URLS
    path("rent-vehicle/", Rent_Vehicle.as_view()),
    path("user-bookings/", My_Bookings.as_view()),
    #Common URLS
    path("", Available_Vehicles.as_view()),
    
]

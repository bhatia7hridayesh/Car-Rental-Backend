from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from .serializers import *
from authentication_app.permissions import *
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import * 
from django.utils import timezone
# Create your views here.

#Agency APIs
class Create_Vehicle(CreateAPIView):
    serializer_class = VehicleCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsAgency]

class My_Vehicles(ListAPIView):
    queryset = Vehicle.objects.filter(is_booked=False)
    serializer_class = MyVehiclesSerializer
    permission_classes = [permissions.IsAuthenticated, IsAgency]

class Bookings_history(APIView):
    serializer_class = VehicleLogSerializer
    permission_classes = [permissions.IsAuthenticated, IsAgency]
    def get(self, request):
        queryset = Vehicle_Bookings_Log.objects.filter(vehicle__agency=request.user)    
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Common APIs
class Available_Vehicles(ListAPIView):
    queryset = Vehicle.objects.filter(is_booked=False)
    serializer_class = AvailableVehiclesSerializer
    permission_classes = [permissions.AllowAny]



#User APIs
class Rent_Vehicle(APIView):
    permission_classes = [permissions.IsAuthenticated ,IsUser]
    def put(self, request):
        user = request.user
        vehicle_number = request.data["vehicle_number"]
        days = request.data["days"]
        vehicle = Vehicle.objects.get(Vehicle_number=vehicle_number)
        if vehicle.is_booked:
            return Response("Already Booked", status=status.HTTP_400_BAD_REQUEST)
        vehicle.is_booked = True
        vehicle_log = Vehicle_Bookings_Log(
            vehicle = vehicle,
            user = user,
            amount_payable = vehicle.rent_per_day*days,
            booked_on = timezone.now,
            returned_on = timezone.now + datetime.timedelta(days=days)
        )
        vehicle_log.save()
        serializer = UserVehicleLogSerializer(vehicle_log)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class My_Bookings(APIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    serializer_class = UserVehicleLogSerializer
    def get(self, request):
        queryset = Vehicle_Bookings_Log.objects.filter(user=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

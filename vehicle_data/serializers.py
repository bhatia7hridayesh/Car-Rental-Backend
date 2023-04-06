import pytz
from rest_framework import serializers

from .models import Vehicle, Vehicle_Bookings_Log

class VehicleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['Vehicle_model', 'Vehicle_number', 'seating_capacity', 'rent_per_day']
    
    def create(self, validated_data):
        agency = self.context.get('request').user
        vehicle = Vehicle(
            agency = agency,
            Vehicle_model = validated_data['Vehicle_model'],
            Vehicle_number = validated_data['Vehicle_number'],
            seating_capacity = validated_data['seating_capacity'],
            rent_per_day = validated_data['rent_per_day'],
            is_booked = False
        )
        vehicle.save()

        return vehicle
    
class AvailableVehiclesSerializer(serializers.ModelSerializer):
    agency = serializers.SerializerMethodField()
    def get_agency(self, obj):
        return obj.agency.full_name
    class Meta:
        model = Vehicle
        fields = ['Vehicle_model', 'Vehicle_number', 'seating_capacity', 'rent_per_day', 'agency']

class VehicleLogSerializer(serializers.ModelSerializer):
    vehicle = serializers.SerializerMethodField()
    booked_on = serializers.SerializerMethodField()
    returned_on = serializers.SerializerMethodField()
    def get_vehicle(self,obj):
        res = {}
        res["vehicle_model"] = obj.vehicle.Vehicle_model
        res["vehicle_number"] = obj.vehicle.Vehicle_number
        res["booked_by"] = obj.user.full_name
        return res
    def get_booked_on(self, obj):
        return obj.booked_on.astimezone(pytz.timezone('Asia/Calcutta')).strftime("%d-%b-%y %H:%M")
    def get_returned_on(self, obj):
        return obj.returned_on.astimezone(pytz.timezone('Asia/Calcutta')).strftime("%d-%b-%y %H:%M")
    class Meta : 
        model = Vehicle_Bookings_Log
        fields = ["id" ,"booked_on","returned_on","amount_payable","vehicle"]

class UserVehicleLogSerializer(serializers.ModelSerializer):
    vehicle = serializers.SerializerMethodField()
    booked_on = serializers.SerializerMethodField()
    returned_on = serializers.SerializerMethodField()
    def get_returned_on(self, obj):
        return obj.returned_on.astimezone(pytz.timezone('Asia/Calcutta')).strftime("%d-%b-%y %H:%M")
    def get_vehicle(self,obj):
        res = {}
        res["vehicle_model"] = obj.vehicle.Vehicle_model
        res["vehicle_number"] = obj.vehicle.Vehicle_number
        res["agency"] = obj.vehicle.agency.full_name
        return res
    def get_booked_on(self, obj):
        return obj.booked_on.astimezone(pytz.timezone('Asia/Calcutta')).strftime("%d-%b-%y %H:%M")
    class Meta : 
        model = Vehicle_Bookings_Log
        fields = ["id" ,"booked_on","returned_on","amount_payable","vehicle"]


class MyVehiclesSerializer(serializers.ModelSerializer):
    agency = serializers.SerializerMethodField()
    def get_agency(self, obj):
        return obj.agency.full_name
    class Meta:
        model = Vehicle
        fields = ['id' , 'Vehicle_model', 'Vehicle_number', 'seating_capacity', 'rent_per_day', 'agency', 'is_booked']

class UpdateVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['Vehicle_model', 'Vehicle_number', 'seating_capacity', 'rent_per_day']
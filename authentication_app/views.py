from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer
from rest_framework import permissions
# Create your views here.



class UserRegistration(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    
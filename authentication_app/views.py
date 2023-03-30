from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserDetailsSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
# Create your views here.



class UserRegistration(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

class UserDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserDetailsSerializer

    def get(self, request):
        user= request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

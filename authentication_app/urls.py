from django.urls import path, include
from .views import UserRegistration, UserDetails
urlpatterns = [
    path("registration/", UserRegistration.as_view()),
    path("profile/", UserDetails.as_view()),
]

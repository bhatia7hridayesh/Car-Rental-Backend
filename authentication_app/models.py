from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager



USER_TYPE_CHOICES = (
    ('Admin','Admin'),
    ('User','User'),
    ('Agency', 'Agency')

)

class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=250,null=True,blank=True)
    email = models.EmailField(max_length=300,null=True,unique=True)
    phone = models.CharField(max_length=13,null=True, unique=True)
    user_type = models.CharField(max_length=20,choices=USER_TYPE_CHOICES,default="User")
    objects=UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        if not self.email:
            return ""
        return self.email

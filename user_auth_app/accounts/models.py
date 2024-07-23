from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)

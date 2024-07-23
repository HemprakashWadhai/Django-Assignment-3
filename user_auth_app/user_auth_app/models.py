from django.contrib.auth.models import Group, Permission
from django.db import models

class CustomUser(models.Model):
    # Fields and methods here
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True
    )

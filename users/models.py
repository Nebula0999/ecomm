from django.db import models
from django.contrib.auth.models import AbstractUser


ROLES = (
    ('admin', 'Admin'),
    ('customer', 'Customer'),
    ('vendor', 'Vendor'),
)

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=ROLES, default='customer')

    def __str__(self):
        return self.username
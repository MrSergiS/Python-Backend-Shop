from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    address = models.CharField(max_length=256, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.username
    
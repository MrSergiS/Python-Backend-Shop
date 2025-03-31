from django.db import models
from shops_backend.models.custom_user_model import CustomUser


class Goods(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=False)
    cost = models.SmallIntegerField(null=False)
    
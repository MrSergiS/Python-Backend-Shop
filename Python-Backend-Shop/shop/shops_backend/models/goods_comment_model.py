from django.db import models
from shops_backend.models.goods import Goods
from shops_backend.models.custom_user_model import CustomUser
from django.core.validators import MaxValueValidator


class GoodsComment(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, blank=False, null=False)
    evaluator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    comment = models.TextField(blank=True)
    rating = models.SmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    
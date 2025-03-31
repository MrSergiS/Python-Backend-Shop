from django.db import models
from shops_backend.models.goods import Goods


class GoodsImg(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, blank=False, null=False, related_name="images")
    img = models.ImageField()

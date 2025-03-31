from rest_framework import serializers
from shops_backend.models.goods_img_model import GoodsImg


class GoodsImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImg
        fields = ['id', 'img']
        
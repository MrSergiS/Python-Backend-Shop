from rest_framework import serializers
from shops_backend.models.goods import Goods
from shops_backend.serializers.goods_img_serializer import GoodsImgSerializer


class GoodsSerislizer(serializers.ModelSerializer):
    img = GoodsImgSerializer(many=True, read_only=True, source="images")    
    
    class Meta:
        model = Goods
        fields = ['id', 'owner', 'title', 'description', 'cost', 'img']
        
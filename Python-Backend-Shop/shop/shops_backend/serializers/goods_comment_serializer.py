from rest_framework import serializers
from shops_backend.models.goods_comment_model import GoodsComment


class GoodsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsComment
        fields = "__all__"
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from shops_backend.serializers.custom_user_serializer import CustomUserSerializer
from shops_backend.models.custom_user_model import CustomUser
from shops_backend.models.goods import Goods
from shops_backend.serializers.goods_serializer import GoodsSerislizer
from shops_backend.models.goods_comment_model import GoodsComment
from shops_backend.serializers.goods_comment_serializer import GoodsCommentSerializer
from shops_backend.permissions.is_owner_permission import IsOwner


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    

class GoodsView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Goods.objects.all()
    serializer_class = GoodsSerislizer
    

class GoodsCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Goods.objects.all()
    serializer_class = GoodsSerislizer
    

class GoodsDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated & IsOwner]
    queryset = Goods.objects.all()
    serializer_class = GoodsSerislizer
    
    
class GoodsCommentCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GoodsComment.objects.all()
    serializer_class = GoodsCommentSerializer


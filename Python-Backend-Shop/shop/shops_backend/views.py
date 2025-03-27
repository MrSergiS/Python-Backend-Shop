from rest_framework import generics
from rest_framework.permissions import AllowAny
from shops_backend.serializers.custom_user_serializer import CustomUserSerializer
from shops_backend.models.custom_user_model import CustomUser


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    
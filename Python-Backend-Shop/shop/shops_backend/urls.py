from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    UserRegistrationView,
    GoodsView,
    GoodsCreateView,
    GoodsDeleteView,
    GoodsCommentCreateView,
)

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("user/register/", UserRegistrationView.as_view(), name='user_register'),
    path('goods/', GoodsView.as_view(), name="goods"),
    path('goods/create/', GoodsCreateView.as_view(), name="create_goods"),
    path('goods/delete/<int:pk>/', GoodsDeleteView.as_view(), name="delete_goods"),
    path('goods/comment/create/', GoodsCommentCreateView.as_view(), name="create_goods_comment"),
]
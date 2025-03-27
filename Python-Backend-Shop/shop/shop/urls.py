from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('some/hidden/path/admin/', admin.site.urls),
    path('', include("shops_backend.urls"))
]

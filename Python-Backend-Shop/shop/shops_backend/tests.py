from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser

class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        url = reverse('user_register')
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "address": "123 Test Street",
            "phone": "1234567890",
            "password": "testpassword123",
            "password2": "testpassword123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(username="testuser").exists())
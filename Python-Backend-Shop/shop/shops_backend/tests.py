from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser
from shops_backend.models.goods import Goods
from shops_backend.models.goods_comment_model import GoodsComment


class APITestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create(username="Test", password="testpassword")
        self.client.force_authenticate(user=self.user)
        data = {
            'owner': self.user,
            'title': 'Test goods',
            'description': 'Test description',
            'cost': 100
        }
        self.goods = Goods.objects.create(**data)
    
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
        
    def test_goods(self):
        url = reverse('goods')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_goods_create(self):
        data = {
            'owner': self.user.id,
            'title': 'New Test goods',
            'description': 'Test description',
            'cost': 100
        }
        url = reverse('create_goods')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Goods.objects.filter(title='New Test goods'))
        
    def test_goods_delete(self):
        url = reverse('delete_goods', kwargs={'pk': self.goods.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Goods.objects.count(), 0)
        
    def test_goods_comment_create(self):
        evaluator = CustomUser.objects.create(username='newUser', password="NewPassword")
        url = reverse('create_goods_comment')
        data = {
            'goods': self.goods.id,
            'evaluator': evaluator.id,
            'comment': 'Hello world!',
            'rating': 10
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GoodsComment.objects.count(), 1)
        
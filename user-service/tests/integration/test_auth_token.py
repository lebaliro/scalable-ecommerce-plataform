from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class AuthTokenTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            first_name='Jorge',
            last_name='Venas',
            username='Jorge123',
            email='jorger@admin.com',
            password='jorger123!@'
        )

        return super().setUp()
    

    def test_get_jwt_token(self):
        url = reverse('auth_token:get_token')
        payload = {
            'username': 'Jorge123',
            'password': 'jorger123!@'
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_refresh_jwt_token(self):
        url = reverse('auth_token:refresh_token')
        refresh = RefreshToken.for_user(self.user)
        
        response = self.client.post(url, {"refresh": str(refresh)})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

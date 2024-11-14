from django.urls import reverse
from django.contrib.auth.models import User

from utils import response_patterns

from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken



class TestUser(APITestCase):
    def setUp(self) -> None:
        self.render_object = JSONRenderer()
        self.user = User.objects.create_user(
            first_name='Jorge',
            last_name='Venas',
            username='Jorge123',
            email='jorger@admin.com',
            password='jorger123!@'
        )
        return super().setUp()


    def login(self):
        refresh = RefreshToken.for_user(self.user)
        access_token = f'Bearer {str(refresh.access_token)}'
        self.client.credentials(HTTP_AUTHORIZATION=access_token)


    def test_create_user_success(self):
        count_users = User.objects.count()
        url = reverse('users:create')

        payload = {
            'first_name': 'Levi',
            'last_name': 'Bastos',
            'username': 'lebaliro',
            'email': 'lebaliro@admin.com',
            'password': 'testando123!@'
        }

        response = self.client.post(url, payload, format='json')

        message_response = self.render_object.render(
            data=response_patterns.response_user_create_success
        )

        self.assertEqual(response.content, message_response)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), count_users + 1)

    def test_detail_user_success(self):
        url = reverse('users:detail', kwargs={'pk': self.user.pk})
        self.login()

        response = self.client.get(url)

        print(response.content)

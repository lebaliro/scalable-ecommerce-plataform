import os
import requests

from clients.keycloak import KeycloakClient

from rest_framework.test import APITestCase


class KeycloakClientTest(APITestCase):
    def test_autenticate(self):
        keycloak_client = KeycloakClient()
        data = keycloak_client.create_user()

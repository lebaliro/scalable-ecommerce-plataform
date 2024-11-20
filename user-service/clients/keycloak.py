import os
import json
import requests


class KeycloakClient():
    def __init__(self, account=None):
        self.__BASE_URI = os.getenv('KEYCLOAK_URL')
        self.__CLIENT_ID = os.getenv('CLIENT_ID')
        self.__CLIENT_SECRET = os.getenv('CLIENT_SECRET')
        self.__account_credentail = account if account is not None else self.__admin_account_credential()
        self.__access_token = self.__get_token()

    def __admin_account_credential(self):
        return {
            "username": "admin",
            "password": "admin",
            "grant_type": "password",
            "client_id": "admin-cli",
        }
               
    def __get_token(self):
        url = f'{self.__BASE_URI}/login'
        
        response = requests.post(url=url, data=self.__account_credentail)

        print(response.content)
        
        access_token = json.loads(response.content).get('access_token')

        return access_token
    
    def create_user(self):
        create_user_url = "http://keycloak:8080/admin/realms/scalable-ecommerce/users"
        
        keycloak_user_payload = {
            "username": 'lebaliro',
            "email": 'lebaliro@gmail.com',
            "enabled": True,
            "credentials": [{"type": "password", "value": "lebaliro", "temporary": False}],
        }

        headers = {"Authorization": f"Bearer {self.__access_token}", "Content-Type": "application/json"}
        response = requests.post(create_user_url, json=keycloak_user_payload, headers=headers)

        print(response)


    # def __verify_token(self, keycloak_data):
    #     url = f'{self.__BASE_URI}/auth'

    #     data = {
    #         'client_id': self.__CLIENT_ID,
    #         'client_secret': self.__CLIENT_SECRET,
    #         'token': keycloak_data.get('access_token')
    #     }

    #     response = requests.post(url='http://nginx:80/auth', data=data)

    #     return response.content

    # def login(self):
    #     keycloak_data = self.__get_token()
    #     # keycloak_data_verified = self.__verify_token(keycloak_data)

    #     return keycloak_data

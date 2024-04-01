


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class GetTokenListViewTests(APITestCase):
    def setUp(self):
      self.payload = {
        "email": "test@mail.com",
        "password": "password",
        "first_name": "first",
        "last_name": "last",
        "username": "test@mail.com",
      }
      self.user = User.objects.create_user(**self.payload)



    def test_get_token(self):
        url = "/api/token/" 
        response = self.client.post(url, {"username": self.payload['username'], "password": self.payload['password']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
        
    def test_get_token_invalid_credentials(self):
        url = "/api/token/" 
        response = self.client.post(url, {"username": self.payload['username'], "password": "invalid"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse('access' in response.data)
        self.assertFalse('refresh' in response.data)
  

class RefreshTokenTests(APITestCase):
    def setUp(self):
      self.payload = {
        "email": "test@mail.com",
        "password": "password",
        "first_name": "first",
        "last_name": "last",
        "username": "test@mail.com",
      }
      self.user = User.objects.create_user(**self.payload)

    def test_get_token_refresh(self):
       
      url = "/api/token/" 
      response = self.client.post(url, {"username": self.payload['username'], "password": self.payload['password']})
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertTrue('access' in response.data)
      self.assertTrue('refresh' in response.data)
      
      url = "/api/token-refresh/" 
      response = self.client.post(url, {"refresh": response.data['refresh']})
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertTrue('access' in response.data)
      self.assertFalse('refresh' in response.data)

    def test_get_token_refresh_invalid_token(self):
      url = "/api/token-refresh/" 
      response = self.client.post(url, {"refresh": "invalid"})
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
      self.assertFalse('access' in response.data)
      self.assertFalse('refresh' in response.data)
      

  
from django.test import TestCase
from django.contrib.auth.models import User


class CreateUserTestCase(TestCase):
  
    def test_create_user(self):

      payload = {
        "email": "",
        "password": "",
        "first_name": "",
        "last_name": "",
        "username": "",
      }


      #Should raise a validation error
      with self.assertRaises(ValueError):
        User.objects.create_user(**payload)
      
      payload = {
        "email": "test@mail.com",
        "password": "password",
        "first_name": "first",
        "last_name": "last",
        "username": "username",
      }

      user = User.objects.create_user(**payload)
      self.assertEqual(user.email, payload['email'])
      self.assertEqual(user.first_name, payload['first_name'])
      self.assertEqual(user.last_name, payload['last_name'])
      self.assertEqual(user.username, payload['username'])
      self.assertTrue(user.check_password(payload['password']))
      self.assertIsNotNone(user.id)
      self.assertIsNotNone(user.date_joined)
      
    
     
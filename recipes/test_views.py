from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Recipe
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class RecipesListCreateTests(APITestCase):
    def setUp(self):
        Recipe.objects.bulk_create([
            Recipe(description="pie", title="yummy pie"),
            Recipe(description="cake", title="protein cake"),
            Recipe(description="beef", title="protein beef"),
        ])
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)


    def test_get_recipes(self):
        url = "/recipes/" 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        # Testing filtering by description
        response = self.client.get(url, {'description': 'pie'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['description'], 'pie')

        # Testing filtering by title
        response = self.client.get(url, {'title': 'protein'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_create_recipe_and_get(self):
        url = "/recipes/" 
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        payload = {"description": "Second recipe", "title": "Fresh recipe"} 
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['description'], 'Second recipe')
        self.assertIsNotNone(response.data['id'])
        
        self.assertIsNotNone(response.data['created_at'])
        self.assertIsNotNone(response.data['updated_at'])


class RecipesViewUpdateDeleteTests(APITestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(description="pie", title="yummy pie")
        self.url = reverse('update', kwargs={'pk': self.recipe.id})
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

    def test_get_by_id(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'pie')
      
    
    def test_update_recipe(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        payload = {"description": "pie", "title": "yummy pie"}
        response = self.client.get(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'pie')
        self.assertEqual(response.data['title'], 'yummy pie')
    
    def test_delete_recipe(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
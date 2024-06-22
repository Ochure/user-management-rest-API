from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

User = get_user_model()

class UserTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.create_url = reverse('create_user')
        self.retrieve_url = reverse('retrieve_user')
        self.update_url_by_id = lambda pk: reverse('update_user_by_id', kwargs={'pk': pk})
        self.update_url_by_name = reverse('update_user_by_name')
        self.delete_url_by_id = lambda pk: reverse('delete_user_by_id', kwargs={'pk': pk})
        self.delete_url_by_name = reverse('delete_user_by_name')

    def test_create_user(self):
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='newuser').email, 'newuser@example.com')

    def test_retrieve_user_by_id(self):
        response = self.client.get(self.retrieve_url, {'id': self.user.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_retrieve_user_by_username(self):
        response = self.client.get(self.retrieve_url, {'username': 'testuser'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_update_user_by_id(self):
        data = {'username': 'updateduser'}
        response = self.client.put(self.update_url_by_id(self.user.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_update_user_by_username(self):
        data = {'username': 'updateduser'}
        response = self.client.put(self.update_url_by_name, data, format='json', QUERY_STRING='username=testuser')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_delete_user_by_id(self):
        response = self.client.delete(self.delete_url_by_id(self.user.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    def test_delete_user_by_username(self):
        response = self.client.delete(self.delete_url_by_name, format='json', QUERY_STRING='username=testuser')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)


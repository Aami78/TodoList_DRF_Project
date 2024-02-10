from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from todo.models import ToDoItem
from rest_framework.authtoken.models import Token

class UserTests(APITestCase):
    def setUp(self):
        # Create a user and a token for testing authenticated endpoints
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_registration(self):
        """
        Ensure we can create a new user.
        """
        url = reverse('register')
        data = {'username': 'newuser', 'password': 'newpassword123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """
        Ensure we can log in a user and receive a token.
        """
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_logout(self):
        """
        Ensure we can log out a user.
        """
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ToDoItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.todo = ToDoItem.objects.create(user=self.user, title='Test ToDo', description='A test todo')

    def test_list_create_todo_items(self):
        """
        Ensure we can list and create todo items.
        """
        # Test listing todos
        list_url = reverse('todo_list')
        list_response = self.client.get(list_url)
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)

        # Test creating a new todo
        create_data = {'title': 'New ToDo', 'description': 'A new todo item', 'completed': False}
        create_response = self.client.post(list_url, create_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_update_delete_todo_item(self):
        """
        Ensure we can retrieve, update, and delete a todo item.
        """
        detail_url = reverse('todo_detail', kwargs={'pk': self.todo.pk})

        # Test retrieving a todo
        retrieve_response = self.client.get(detail_url)
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)

        # Test updating a todo
        update_data = {'title': 'Updated ToDo', 'description': 'Updated description', 'completed': True}
        update_response = self.client.put(detail_url, update_data, format='json')
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

        # Test deleting a todo
        delete_response = self.client.delete(detail_url)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

from django.test import TestCase
from django.contrib.auth.models import User
from todo.models import ToDoItem

class ToDoItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(username='testuser', password='12345')
        ToDoItem.objects.create(title='First ToDo', user=test_user, description='A test todo')

    def test_title_label(self):
        todo = ToDoItem.objects.get(id=1)
        field_label = todo._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_creation(self):
        todo = ToDoItem.objects.get(id=1)
        self.assertTrue(isinstance(todo, ToDoItem))
        self.assertEquals(todo.__str__(), todo.title)

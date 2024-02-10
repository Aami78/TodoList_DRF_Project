from django.test import TestCase
from django.contrib.auth.models import User
from todo.models import ToDoItem
from todo.serializers import ToDoSerializer

class ToDoSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', password='test')
        self.todo_attributes = {
            'user': self.user,
            'title': 'Test ToDo',
            'description': 'Test ToDo Description',
            'completed': False,
        }
        self.todo = ToDoItem.objects.create(**self.todo_attributes)
        self.serializer = ToDoSerializer(instance=self.todo)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'description', 'completed', 'created_at', 'updated_at', 'user']))

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.todo_attributes['title'])

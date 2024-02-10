from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ToDoListView, ToDoDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('todos/', ToDoListView.as_view(), name='todo_list'),
    path('todos/<int:pk>/', ToDoDetailView.as_view(), name='todo_detail'),
]

from django.contrib.auth.models import User
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from .models import ToDoItem
from .serializers import UserSerializer, ToDoSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class LogoutView(views.APIView):
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ToDoListView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['completed', 'user']  # Allows filtering by 'completed' status and 'user'
    ordering_fields = ['created_at', 'updated_at']  # Allows sorting by 'created_at' and 'updated_at'
    
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ToDoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoSerializer

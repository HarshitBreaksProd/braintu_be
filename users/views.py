from django.contrib.auth import get_user_model, login, logout
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserLoginSerializer, UserRegistrationSerializer, UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    """
    Endpoint for user registration. Publicly accessible.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class LoginView(views.APIView):
    permission_classes= [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(UserSerializer(user).data)

class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated] # Ensure user is logged in to log out

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class SessionView(views.APIView):
    """
    A view to check the current session. If the user is authenticated,
    it returns user data. Otherwise, it will return a 403 Forbidden.
    """
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'isAuthenticated': False}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(UserSerializer(request.user).data)
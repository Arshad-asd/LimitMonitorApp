from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class UserAccountRegistrationView(generics.CreateAPIView):
    serializer_class = UserAccountSerializer
    permission_classes = [AllowAny]


class UserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

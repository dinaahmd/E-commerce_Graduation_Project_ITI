from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from base.models import  User

from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import UserRegisterSerializer
from rest_framework import permissions, status

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer 
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed




class UserLoginAPIView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        User = serializer.User
         # Raise an exception if the user is blocked

        token = serializer.validated_data
        return Response(token, status=status.HTTP_200_OK)

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer 
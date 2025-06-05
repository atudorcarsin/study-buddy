from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
import logging

logger = logging.getLogger(__name__)

class AuthRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password or not email:
            return Response(
                {
                    'error': 'Username and password are required'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if password != request.data.get('password_confirm'):
            return Response(
                {
                    'error': 'Passwords do not match'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response(
                {
                    'error': 'User already exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a new user
        user = User.objects.create_user(email=email, username=username, password=password)
        login(request, user)
        return Response(
            {
                'success': 'User created successfully'
            },
            status=status.HTTP_201_CREATED
        )

class AuthLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'error': 'Invalid credentials'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

class AuthLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(
            {
                'success': 'Logged out successfully'
            },
            status=status.HTTP_200_OK
        )

class AuthStatusView(APIView):
    # By default, only authenticated users can access this view
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
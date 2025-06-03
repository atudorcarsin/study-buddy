from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

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
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

class AuthLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'success': 'Logged out successfully'})

class AuthStatusView(APIView):
    # By default, only authenticated users can access this view
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
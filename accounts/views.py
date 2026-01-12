from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterUserSerializer
from .models import User


class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if not username or not password:
            return Response({'errors': 'Please complete all fields!'}, status=status.HTTP_400_BAD_REQUEST)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'errors': 'Password or username is incorrect'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': "You logged out"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message': 'Something was wrong'}, status=status.HTTP_400_BAD_REQUEST)


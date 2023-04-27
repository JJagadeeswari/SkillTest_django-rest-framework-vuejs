from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .utils import get_tokens_for_user
from .serializers import RegistrationSerializer, PasswordChangeSerializer, UserProfileSerializer
from users.models import MyUser
from django.http import Http404

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(CreateAPIView):
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')

        try:
            #user = CustomUser.objects.get(username=username)            
            my_data = request.data    
            print(my_data)
            user = MyUser.objects.get(email=my_data['email'])
            my_data['user_id'] = user.id
            print(my_data['user_id'])

            #serializer = self.serializer_class(data=request.data, context={'user_id': user.id})
            serializer = self.serializer_class(data=my_data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except MyUser.DoesNotExist:
            raise Http404


class LoginView(APIView):
    def post(self, request):

        if "email" not in request.data or "password" not in request.data:
            return Response({"msg": "Credentials missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({"msg": "Login Success", **auth_data}, status=status.HTTP_200_OK)
        return Response({"msg": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'username': user.username, 'email': user.email})


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(context={"request": request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


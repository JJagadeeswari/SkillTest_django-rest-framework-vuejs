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
from .serializers import RegistrationSerializer, PasswordChangeSerializer, UserProfileSerializer, MyUserSerializer
from users.models import MyUser
from quesapp.models.technologies import TechnologyList
from quesapp.serializers import TechnologySerializer
from .models import UserProfile

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
        #username = request.data.get('username')
        #email = request.data.get('email')

        try:
            #user = CustomUser.objects.get(username=username)
            my_data = request.data
            print(my_data)
            #user = MyUser.objects.get(email=my_data['email'])
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
        return Response({'id': user.id, 'email': user.email, })


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(context={"request": request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class profileInfo(APIView):

    def get(self, request):
        
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        #MyUserObject = MyUser.objects.get(id=request.user.id)
        MyUserObject = MyUser.objects.get(email=request.user.email)
        MyUserObject_serializer = RegistrationSerializer(MyUserObject)
        MyUser_serialized_data = {
            'email': MyUserObject_serializer.data['email'],
            'first_name': MyUserObject_serializer.data['first_name'],
            'last_name': MyUserObject_serializer.data['last_name']
        }
        
        UserProfileObject = UserProfile.objects.get(user_id=request.user.id)
        userProfile_serializer = UserProfileSerializer(UserProfileObject)

        data = {
            'MyUser_serialized_data' : MyUser_serialized_data,
            'UserProfileSerializer' : userProfile_serializer.data,
        }

        return Response(data)
    

    def put(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        my_user_object = MyUser.objects.filter(id=request.user.id).values()
        print(my_user_object)
        my_user_serializer = RegistrationSerializer(my_user_object, data=request.data, partial=True)
        print("my_user_serializer: ", my_user_serializer)
        if my_user_serializer.is_valid():
            my_user_serializer.save()
        
        user_profile_object = UserProfile.objects.get(user_id=request.user.id)
        user_profile_serializer = UserProfileSerializer(user_profile_object, data=request.data, partial=True)
        if user_profile_serializer.is_valid():
            user_profile_serializer.save()
        
        # return updated data
        return self.get(request)       

        """
        my_user_object = MyUser.objects.get(email=request.user.email)
        my_user_serializer = RegistrationSerializer(my_user_object, data=request.data, partial=True)
        if my_user_serializer.is_valid():
            my_user_serializer.save()
                
    
        """
    


class prefTech(APIView):
    def get(self, request):        
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        techObject = TechnologyList.objects.all()
        techObject_serializer = TechnologySerializer(techObject, many=True)

        data = {
            'techObject_serializer' : techObject_serializer.data,
            #'UserProfileSerializer': userProfile_serializer.data,
        }

        return Response(data)
    
    def put(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        user_profile_object = UserProfile.objects.get(user_id=request.user.id)
        user_profile_serializer = UserProfileSerializer(user_profile_object, data=request.data, partial=True)
        if user_profile_serializer.is_valid():
            user_profile_serializer.save()

        return Response(user_profile_serializer.data)
    

    
"""
    
    def put(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        user_profile_object = UserProfile.objects.get(user_id=request.user.id)
        user_profile_serializer = UserProfileSerializer(user_profile_object, data=request.data, partial=True)
        if user_profile_serializer.is_valid():
            user_profile_serializer.save()
        
        return self.get(request)   
    """    

                

"""
    def post(self, request, *args, **kwargs):
        testSessionInfoObject = getObject(TestSessionInfo)

        session_data = {
            'user_id' : request.user.id,
        }
        session_serializer = TestSessionInfoSerializer(data=session_data)
        if session_serializer.is_valid():
            session_serializer.save()
        
        session_id = testSessionInfoObject.filter(user_id=request.user).order_by('-updated_at').values_list('pk', flat=True).first()

        sessionItems_data=request.data
        sessionItems_data['session_id'] = session_id

        if 'user_video_path' in sessionItems_data:
            filename = sessionItems_data.get('user_video_path').name
            #since uploaded file is 'InMemoryUploadedFile' object, need to use 'name' function to access the file name
            extension = os.path.splitext(filename)[1]               

            if extension.lower() in ['.mp4', '.avi', '.mov', '.wmv', '.webm']:
                sessionItems_serializer= TestSessionItemsSerializer(data=sessionItems_data)
                if sessionItems_serializer.is_valid():
                    user_video_path = sessionItems_serializer.validated_data['user_video_path']
                    sessionItems_serializer.save()
                    return Response(sessionItems_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response(sessionItems_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise ValidationError('Unsupported file format')
"""
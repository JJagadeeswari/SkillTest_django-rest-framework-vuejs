from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import os

from skilltest.models.questions import Question
from skilltest.models.test_session import TestSessionInfo, TestSessionItems
from .serializers import QuestionsSerializer, TestSessionInfoSerializer, TestSessionItemsSerializer
from .utils import getObject

# Create your views here.

class helpPage(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #screening_question = Questions.objects.order_by("id")[:5]
        screening_question = getObject(Question).order_by("id")[:5]
        
        serializer = QuestionsSerializer(screening_question, many=True)
        return Response(serializer.data)


@api_view(('GET',))
def practiceScreening(request):
    #practice_question = Questions.objects.order_by("?").first()
    practice_question = getObject(Question).order_by("?").first()
    serializer = QuestionsSerializer(practice_question)
    return Response(serializer.data)


"""

class selfScreening(generics.CreateAPIView):
    serializer_class = TestSessionInfoSerializer
    queryset = [Questions.objects.all(), TestSessionInfo.objects.all()]

    def get(self, request):
        screening_question = Questions.objects.order_by("id")[:5]
        serializer = QuestionsSerializer(screening_question, many=True)

        #request.session['qid'] = screening_question.values('id')
        #request.session['username'] = username
        #uid_val = request.session.get('uid')

        return Response(serializer.data)

    def post(self, request):
        sess_id=3
        user = request.user
        print(user.id)

        session_data = {}
        session_data['user_id'] = user.id
        session_serializer = TestSessionInfoSerializer(data=session_data)
        if session_serializer.is_valid():
            session_serializer.save()
        
        #session_id = TestSessionInfo.objects.filter(user_id=user.id).order_by('-updated_at').first().user_id
        #session_id = TestSessionInfo.objects.filter(user_id=user.id).order_by('-updated_at').values_list('user_id__email', flat=True).first()
        session_id = TestSessionInfo.objects.filter(user_id=user).order_by('-updated_at').values_list('pk', flat=True).first()
     
        sessionItems_data=request.data
        sessionItems_data['session_id'] = session_id
        print('sessionItems_data:', sessionItems_data)

        sessionItems_serializer= TestSessionItemsSerializer(data=sessionItems_data)
        if sessionItems_serializer.is_valid():
            return Response(sessionItems_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sessionItems_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def create(self, request, args, *kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        video_file = serializer.validated_data.get("file", None)
        if video_file is None:
            return Response(
                {"file": "This field is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        if not self.is_video_file_valid(video_file):
            return Response(
                {"file": "Invalid video file."}, status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def is_video_file_valid(self, video_file):
        video_extensions = [".mp4", ".mov", ".avi", ".wmv", "webm"]
        return video_file.name.lower().endswith(tuple(video_extensions))




"""

#working

"""
class selfScreening(APIView):
    #parser_classes = [parsers.MultiPartParser]

    def get(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        user = request.user
        print(user.id)
        
        screening_question = Questions.objects.order_by("id")[:5]
        serializer = QuestionsSerializer(screening_question, many=True)

        #request.session['qid'] = screening_question.values('id')
        #request.session['username'] = username
        #uid_val = request.session.get('uid')

        return Response(serializer.data)

    def post(self, request):
        sess_id=3
        user = request.user
        print(user.id)

        session_data = {}
        session_data['user_id'] = user.id
        session_serializer = TestSessionInfoSerializer(data=session_data)
        if session_serializer.is_valid():
            session_serializer.save()
        
        #session_id = TestSessionInfo.objects.filter(user_id=user.id).order_by('-updated_at').first().user_id
        #session_id = TestSessionInfo.objects.filter(user_id=user.id).order_by('-updated_at').values_list('user_id__email', flat=True).first()
        session_id = TestSessionInfo.objects.filter(user_id=user).order_by('-updated_at').values_list('pk', flat=True).first()
        print(session_id)

        sessionItems_data=request.data
        sessionItems_data['session_id'] = session_id
        print('sessionItems_data:', sessionItems_data)
"""


"""

        if 'user_video_path' in sessionItems_data:
            #video_data = sessionItems_data['user_video_path']
            video_data = sessionItems_data.get('user_video_path')
            print(video_data)
            sessionItems_data['user_video_path'] = video_data
        else:
            print("no video")

        print('sessionItems_data2:', sessionItems_data)

"""


"""
        if 'user_video_path' in sessionItems_data:
            #filename = sessionItems_data.get('user_video_path')        #this will throw error since it is object file
            filename = sessionItems_data.get('user_video_path').name
            extension = os.path.splitext(filename)[1]  # Returns the extension, including the dot (e.g. ".webm")
            #extension_without_dot = extension[1:]  # Removes the dot from the extension

            if extension.lower() in ['.mp4', '.avi', '.mov', '.wmv', '.webm']:
                print("Video file")
                sessionItems_serializer= TestSessionItemsSerializer(data=sessionItems_data)
                if sessionItems_serializer.is_valid():
                    user_video_path = sessionItems_serializer.validated_data['user_video_path']
                    session_serializer.save()
                    return Response(sessionItems_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response(sessionItems_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                print("Not an expected file format")
"""
                
"""
        #screening_question = Questions.objects.order_by("id")[:5]
        #serializer = QuestionsSerializer(screening_question, many=True)
        #email = request.data['email'] 
        #
        #return Response(serializer.data)
        #return Response({'sesion-id':sess_id})     
"""


"""

class selfScreening(generics.ListCreateAPIView):
    #permission_classes =[AllowAny]
    serializer_class = TestSessionInfoSerializer
    #parser_class =[MultiPartParser,FormParser]

    def get(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        user = request.user
        print(user.id)
        
        screening_question = Questions.objects.order_by("id")[:5]
        serializer = QuestionsSerializer(screening_question, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        sess_id=3
        user = request.user
        print(user.id)

        session_data = {}
        session_data['user_id'] = user.id
        session_serializer = TestSessionInfoSerializer(data=session_data)
        if session_serializer.is_valid():
            session_serializer.save()
        
        session_id = TestSessionInfo.objects.filter(user_id=user).order_by('-updated_at').values_list('pk', flat=True).first()
        print(session_id)

        sessionItems_data=request.data
        sessionItems_data['session_id'] = session_id
        print('sessionItems_data:', sessionItems_data)

        
        if 'user_video_path' in sessionItems_data:
            filename = sessionItems_data.get('user_video_path').name
            extension = os.path.splitext(filename)[1]

            if extension.lower() in ['.mp4', '.avi', '.mov', '.wmv', '.webm']:
                print("Video file")
                sessionItems_serializer= TestSessionItemsSerializer(data=sessionItems_data)
                if sessionItems_serializer.is_valid():
                    user_video_path = sessionItems_serializer.validated_data['user_video_path']
                    session_serializer.save()
                    return Response(sessionItems_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response(sessionItems_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                print("Not an expected file format")
    

"""


class selfScreening(APIView):

    def get(self, request):
        questionsObject = getObject(Question)

        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        #defaultScreeningQuestion = Questions.objects.order_by("id")[:5]
        defaultScreeningQuestion = questionsObject.order_by("id")[:5]
        
        selectedQuestionId = []
        #selectedQuestionId = [5, 4, 3, 2, 1]
        selectedScreeningQuestions = []

        for id in selectedQuestionId:
            try:
                #ques = Questions.objects.get(id=id)
                ques = questionsObject.get(id=id)
                selectedScreeningQuestions.append(ques)
            except Question.DoesNotExist:
                raise ValueError(id, 'doesnt exist in selective model')
        
        if (len(selectedQuestionId)) == 0:
            serializeQues = defaultScreeningQuestion
        else:
            serializeQues = selectedScreeningQuestions

        screeningQuestionSerializer = QuestionsSerializer(serializeQues, many=True)

        return Response(screeningQuestionSerializer.data)

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
    def post(self, request, *args, **kwargs):
        sess_id=3
        user = request.user
        print(user.id)

        session_data = {}
        session_data['user_id'] = user.id
        session_serializer = TestSessionInfoSerializer(data=session_data)
        if session_serializer.is_valid():
            session_serializer.save()
        
        session_id = TestSessionInfo.objects.filter(user_id=user).order_by('-updated_at').values_list('pk', flat=True).first()
        print(session_id)

        sessionItems_data=request.data
        sessionItems_data['session_id'] = session_id
        print('sessionItems_data:', sessionItems_data)

        if 'user_video_path' in sessionItems_data:
            filename = sessionItems_data.get('user_video_path').name
            extension = os.path.splitext(filename)[1]

            if extension.lower() in ['.mp4', '.avi', '.mov', '.wmv', '.webm']:
                print("Video file")
                sessionItems_serializer= TestSessionItemsSerializer(data=sessionItems_data)
                if sessionItems_serializer.is_valid():
                    user_video_path = sessionItems_serializer.validated_data['user_video_path']
                    session_serializer.save()
                    return Response(sessionItems_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response(sessionItems_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                print("Not an expected file format")
    """


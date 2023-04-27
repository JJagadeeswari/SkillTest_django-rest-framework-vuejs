from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField
from skilltest.models.questions import Question
from skilltest.models.test_session import TestSessionInfo, TestSessionItems


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question']
        #fields = "__all__"


class TestSessionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSessionInfo
        fields = ['id', 'user_id']

#working
"""
class TestSessionItemsSerializer(serializers.ModelSerializer):
    #user_video_path = serializers.FileField()
    #user_video_path = FileField()

    class Meta:
        model = TestSessionItems
        fields = ['id', 'user_video_path', 'session_id']
"""


class TestSessionItemsSerializer(serializers.ModelSerializer):
    user_video_path = serializers.FileField()

    class Meta:
        model = TestSessionItems
        fields = ['id', 'user_video_path', 'session_id']


"""
class TestSessionItemsSerializer(serializers.ModelSerializer):
    user_video_path = serializers.ListField(child =serializers.FileField(max_length=100000,allow_empty_file =False,use_url =False))

    class Meta:
        model = TestSessionItems
        fields = ['id', 'user_video_path', 'session_id']

class TestSessionItemsDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model =TestSessionItems
        fields='__all__'

"""
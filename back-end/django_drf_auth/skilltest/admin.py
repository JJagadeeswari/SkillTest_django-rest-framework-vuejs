from django.contrib import admin
from skilltest.models.questions import Question, QAnswer
from skilltest.models.test_session import TestSessionInfo, TestSessionItems


# Register your models here.

#admin.site.register(Question)
@admin.register(Question)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'question')

@admin.register(QAnswer)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'question_id')

@admin.register(TestSessionInfo)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'user_id')

@admin.register(TestSessionItems)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'session_id', 'user_video_path', 'rating')




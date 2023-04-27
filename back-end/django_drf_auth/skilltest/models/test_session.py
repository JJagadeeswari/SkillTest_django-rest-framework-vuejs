from django.db import models
from .questions import Question
from users.models import MyUser

from skilltest.utils import user_directory_path


class TestSessionInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.user_id}'

    class Meta:
        db_table = 'TestSessionInfo'



class TestSessionItems(models.Model):

    Rating = (
        ('Null', '0'),
        ('Bad', '1'),
        ('Need_to_Improve','2'),
        ('Average', '3'),
        ('Good', '4'),
        ('Excelent','5')
    )
        

    id = models.AutoField(primary_key=True)
    session_id = models.OneToOneField(TestSessionInfo, on_delete=models.CASCADE)
    #question_id = models.ForeignKey(Questions, on_delete=models.CASCADE, blank=True)
    user_video_path = models.FileField(upload_to=user_directory_path)
    comments = models.TextField(blank=True, default="None")
    rating = models.CharField(max_length=25, choices=Rating, default=0)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.session_id}'

    class Meta:
        db_table = 'TestSessionItems'
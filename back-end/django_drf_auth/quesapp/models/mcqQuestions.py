from django.db import models
from .technologies import TechnologyList, Level


class McqQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    mcq_ques = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    technology = models.ForeignKey(TechnologyList, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null = True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.mcq_ques}, {self.answer}, {self.technology}, {self.level}'

    class Meta:
        db_table = 'McqQuestions'












"""

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.choice_text


class McqQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    mcq_ques = models.CharField(max_length=200, unique=True)
    mcq_choices = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'McqQuestion'


"""
from django.db import models

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #def __str__(self):
        #return f'{self.id}, {self.question}'

    class Meta:
        db_table = 'Question'


class QAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    keywords = models.TextField()
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.question_id}'

    class Meta:
        db_table = 'QAnswer'
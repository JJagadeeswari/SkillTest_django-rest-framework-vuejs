from django.db import models
from .technologies import TechnologyList, Level


class TechnicalQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    tech_ques = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255, blank=True)
    technology = models.ForeignKey(TechnologyList, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null = True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.tech_ques}, {self.technology}, {self.level}'

    class Meta:
        db_table = 'TechnicalQuestion'


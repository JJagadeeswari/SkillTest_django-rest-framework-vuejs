from django.db import models

class TechnologyList(models.Model):
    id = models.AutoField(primary_key=True)
    technology_name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.technology_name}'

    class Meta:
        db_table = 'TechnologyList'


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.level}'

    class Meta:
        db_table = 'Level'


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.type}'

    class Meta:
        db_table = 'Type'


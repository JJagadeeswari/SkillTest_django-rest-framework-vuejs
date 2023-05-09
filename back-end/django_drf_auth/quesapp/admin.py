from django.contrib import admin
from quesapp.models.technologies import TechnologyList, Level, Type
from quesapp.models.mcqQuestions import McqQuestions
from quesapp.models.technicalQuestions import TechnicalQuestion


# Register your models here.


@admin.register(TechnologyList)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'technology_name')


@admin.register(Level)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'level')


@admin.register(Type)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'type')


@admin.register(McqQuestions)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'mcq_ques', 'answer', 'technology', 'level')


@admin.register(TechnicalQuestion)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'tech_ques', 'technology', 'level')




#admin.site.register(McqQuestions)


"""

@admin.register(McqQuestion)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'mcq_ques')

"""


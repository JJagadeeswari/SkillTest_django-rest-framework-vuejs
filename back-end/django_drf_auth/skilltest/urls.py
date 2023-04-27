from django.urls import path, include
from . import views
from .views import selfScreening, helpPage


urlpatterns = [
    path('help-page/', helpPage.as_view(), name="help_page"),
    path('practice-screening/', views.practiceScreening, name='practice_screening'),
    #path('self-screening', views.selfScreening, name='self-screening'),
    path('self-screening/', selfScreening.as_view(), name="self_screening"),
    
]

from django.contrib import admin
from django.urls import path, include

from .views import List, survey_info, survey_process, survey_result


app_name = 'surveys'
urlpatterns = [
    path('', List, name='list'),
    path('<int:survey_id>/', survey_info, name='info'),
    path('<int:survey_id>/process', survey_process, name='process'),
    path('<int:survey_id>/result', survey_result, name='result'),
]
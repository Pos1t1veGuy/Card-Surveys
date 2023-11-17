from django.contrib import admin
from django.urls import path, include

from .views import List, survey_info, survey_process, survey_result, new_survey, your_surveys


app_name = 'surveys'
urlpatterns = [
    path('', List, name='list'),
    path('new/', new_survey.as_view(), name='new'),
    path('your_surveys/', your_surveys, name='your_surveys'),
    path('<int:survey_id>/', survey_info, name='info'),
    path('<int:survey_id>/process', survey_process, name='process'),
    path('<int:survey_id>/result', survey_result, name='result'),
]
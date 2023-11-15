from django.contrib import admin
from .models import Survey, Card

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'created_at']
    filter_horizontal = ['participants']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'survey', 'body', 'avatar']

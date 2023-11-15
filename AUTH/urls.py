from django.contrib import admin
from django.urls import path, include

from .views import login_or_register, info, anonimus


app_name = 'auth'
urlpatterns = [
    path('', info, name='info'),
    path('auth/', login_or_register, name='auth'),
    path('hello/', anonimus, name='anonimus'),
]
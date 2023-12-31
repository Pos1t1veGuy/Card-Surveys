from django.contrib import admin
from django.urls import path, include

from .views import login_or_register, info, anonimus, logout_view


app_name = 'auth'
urlpatterns = [
    path('', info, name='info'),
    path('auth/', login_or_register.as_view(), name='auth'),
    path('hello/', anonimus, name='anonimus'),
    path('logout/', logout_view, name='logout'),
]
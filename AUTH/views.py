from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

def login_or_register(request):
    return render(request, 'logorreg.html')

@login_required(login_url='auth:anonimus')
def info(request):
    return render(request, 'info.html', {'user': None})

def anonimus(request):
    return render(request, 'anonimus.html')

@login_required(login_url='auth:anonimus')
def logout(request):
    logout(request)
    return redirect('surveys:list')
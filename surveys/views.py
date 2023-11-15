from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

def List(request):
    return render(request, 'list.html', {'surveys': []})

def survey_info(request, survey_id: int):
    return render(request, 'survey_info.html', {'survey': None})

@login_required(login_url='auth:anonimus')
def survey_process(request, survey_id: int):
    return render(request, 'survey_process.html', {'survey': None})

@login_required(login_url='auth:anonimus')
def survey_result(request, survey_id: int):
    return render(request, 'survey_result.html', {'survey': None})

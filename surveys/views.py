from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Survey

import string


def List(request):
    return render(request, 'list.html', {'user': request.user, 'surveys': Survey.objects.all().order_by('-rate')[:10]})

def survey_info(request, survey_id: int):
    return render(request, 'survey_info.html', {'survey': get_object_or_404(Survey, id=survey_id), 'user': request.user})

@login_required(login_url='auth:anonimus')
def survey_process(request, survey_id: int):
    return render(request, 'survey_process.html', {'survey': get_object_or_404(Survey, id=survey_id), 'user': request.user})

@login_required(login_url='auth:anonimus')
def survey_result(request, survey_id: int):
    return render(request, 'survey_result.html', {'survey': get_object_or_404(Survey, id=survey_id), 'user': request.user})

@login_required(login_url='auth:anonimus')
def your_surveys(request):
    return render(request, 'your_surveys.html', {'surveys': request.user.created_surveys.all(), 'user': request.user})

class new_survey(View):
    template_name = 'new_survey.html'

    @method_decorator(login_required(login_url='auth:anonimus'))
    def get(self, request):
        return render(request, self.template_name, {'user': request.user})

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        avatar = request.POST.get('avatar')

        if FormUtils.is_survey_name(name):
            Survey.objects.create(name=name, description=description, avatar=avatar, author=request.user)
            return redirect('surveys:your_surveys')
        else:
            return render(request, self.template_name, {'reg_error': f'Неправильое имя опроса {name}. При составлении имени можно использовать a-z, A-Z, 0-9, _, -, при этом он должен быть от 1 до 45 символов.'})


class FormUtils:
    def is_survey_name(name: str) -> bool:
        enabled_chars = string.ascii_letters + string.digits + '_-'
        max_length = 45
        min_length = 1

        if len(name) > max_length or len(name) < min_length:
            return False

        for char in name:
            if not char in enabled_chars:
                return False

        return True
        
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

#from .models import Question


def index(request):
    context = {
        #'latest_question_list': latest_question_list,
    }
    template = loader.get_template('task_manager/login.html')
    
    return HttpResponse(template.render(context, request))

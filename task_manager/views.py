from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def index(request):
    context = {}
    template = loader.get_template('task_manager/login.html')
    
    return HttpResponse(template.render(context, request))

def register(request):
    request_username = request.POST['username']
    request_password = request.POST['password']

    try:
        User.objects.get(username=request_username)
    except User.DoesNotExist:
        user = User.objects.create_user(request_username, '', request_password)
        user.save()
        result = authenticate(username=request_username, password=request_password)
        if result is not None:
            return HttpResponseRedirect('task_manager')

    return HttpResponseBadRequest()

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # タスク表示画面にリダイレクト
        return HttpResponseRedirect("")
    context = {}
    return render(request, 'task_manager', context)

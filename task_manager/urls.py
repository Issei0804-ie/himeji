from django.urls import path

from . import views

app_name = 'task_manager'
urlpatterns = [
    # ex: /task_manager/
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]
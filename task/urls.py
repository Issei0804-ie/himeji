from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('delete/<list_id>', views.delete, name="delete"),
   path('complete/<list_id>', views.complete, name="complete"),
]
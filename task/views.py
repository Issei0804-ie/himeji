from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def index(request):
   if request.method == 'POST':
      form = ListForm(request.POST or None)
      if form.is_valid():
         form.save()
         all_items = List.objects.all
         messages.success(request, ('Item Has Been Added To List'))
         return render(request, 'task/index.html', {'all_items': all_items})
      else:
         messages.error(request, ('write anything'))
         all_items = List.objects.all
         return render(request, 'task/index.html', {'all_items': all_items})
   else:
      all_items = List.objects.all
      return render(request, 'task/index.html', {'all_items': all_items})
    
def delete(request, list_id):
   item = List.objects.get(pk=list_id)
   item.delete()
   messages.success(request, ('Item Has Been Deleted from List!'))
   return redirect('index')

def complete(request, list_id):
   item = List.objects.get(pk=list_id)
   item.completed = True
   item.save()
   messages.success(request, ('Item Has Been Complete'))
   return redirect('index')

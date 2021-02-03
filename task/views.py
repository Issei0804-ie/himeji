from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.db import models
from django.utils.dateparse import parse_date

@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        date_str = form.data.get("deadline")
        date = parse_date(date_str)
        print(date)
        data = List(user_id=request.user.id, item=form.data.get("item"), deadline=date,
                    completed=form.data.get("completed", False))

        if form.data.get("item") is not None and date is not None:
            data.save()
            print(request.user.id)
            all_items = List.objects.filter(user_id__in=str(request.user.id))
            messages.success(request, ('Item Has Been Added To List'))
            return render(request, 'task/index.html', {'all_items': all_items})
        else:
            print(request.user.id)
            messages.error(request, ('write anything'))
            all_items = List.objects.filter(user_id__in=str(request.user.id))
            return render(request, 'task/index.html', {'all_items': all_items})
    else:
        print(request.user.id)
        all_items = List.objects.filter(user_id__in=str(request.user.id))
        return render(request, 'task/index.html', {'all_items': all_items})


@login_required
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted from List!'))
    return redirect('index')


@login_required
def complete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request, ('Item Has Been Complete'))
    return redirect('index')

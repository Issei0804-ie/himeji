from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "deadline", "completed"]
        widgets = {
            'date_field': AdminDateWidget(),
        }

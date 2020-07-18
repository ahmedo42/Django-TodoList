from django import forms
from django.forms import ModelForm , DateTimeInput
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','due_date']
        widgets = {
            'due_date' : DateTimeInput()
        }
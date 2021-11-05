from django import forms
from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('Task')

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('Task')

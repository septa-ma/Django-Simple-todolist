from django import forms
from .models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    duration = forms.DurationField()
    status = forms.CharField()

# modelform use for makeing a form for a specific model
# useing nested class for makeing modelform
# if you want to make a form for all fields in model:
# fields = '__all__'
# for all except one:
# exclude = ['title']
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task_name', 'task_description', 'task_duration', 'task_status')
        
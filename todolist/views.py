from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoCreateForm, TodoUpdateForm

# Create your views here.
# write your controller functions here.
# all views must have request variable.
def todolist(request):
    all = Todo.objects.all()
    return render(request, 'todolist.html', {'todos': all})
    # return HttpResponse("Hello, world. You're at the polls index.")

def moreInfo(request, todoId):
    moInfore = Todo.objects.get(id=todoId)
    return render(request, 'moreInfo.html', {'todo': moInfore})

def delete(request, todoId):
    Todo.objects.get(id=todoId).delete()
    messages.add_message(request, messages.INFO, "item deleted succesfuly.")
    return redirect('todolist')

def createTodo(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Todo.objects.create(
                task_name=data['title'], 
                task_description=data['description'],
                task_duration=data['duration'],
                task_status=data['status']
            )
            messages.success(request, "item created succesfuly.")
            return redirect('todolist')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})

def updateTodo(request, todoId): 
    todo = Todo.objects.get(id=todoId)   
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()   
            messages.success(request, "item updated succesfuly.")
            return redirect('moreInfo', todoId)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})

# class Manager:
# A Manager is the interface through which database query operations
# are provided to Django models.
# Manager names:
# By default, Django adds a Manager with the name objects to every Django 
# model class. However, if you want to use objects as a field name, or if 
# you want to use a name other than objects for the Manager, you can rename 
# it on a per-model basis. To rename the Manager for a given class, define 
# a class attribute of type models.Manager() on that model.
# ex: 
# class Person(models.Model):
#...
# people = models.Manager()
# Using this example model, Person.objects will generate an AttributeError 
# exception, but Person.people.all() will provide a list of all Person objects.
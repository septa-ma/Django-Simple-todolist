from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username = data['username'],
                email = data['email'],
                password = data['password']
            )
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            messages.success(request, "user registered succesfuly.")
            return redirect('todolist')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "user logined succesfuly.")
                print('ok')
                return redirect('todolist')
            else:
                messages.error(request, "username or password is wrong.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    

def logoutUser(request):
    logout(request)
    messages.success(request, "user logined succesfuly.")
    return redirect('todolist')

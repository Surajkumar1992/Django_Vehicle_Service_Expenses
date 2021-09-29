from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError, InternalError
from django.contrib.auth import login, logout, authenticate


# HomePage
def home(request):
    return render(request, 'VehicleService/home.html')

def contact(request):
    return render(request, 'VehicleService/contact.html')

def about(request):
    return render(request, 'VehicleService/about.html')

# SignUp
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'VehicleService/signup.html', {'forms': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current')
            except IntegrityError:
                return render(request, 'VehicleService/signup.html', {'forms': UserCreationForm(), 'error': 'The Username is alrady taken'})
        else:
            return render(request, 'VehicleService/signup.html', {'forms': UserCreationForm(), 'error': 'Password Didn\'t Match, Please crosscheck'})


# Login
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'VehicleService/login.html', {'forms': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'todo/login.html', {'forms': AuthenticationForm(), 'error': 'Username and Password didnt match'})
        else:
            login(request, user)
            return redirect('current')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def current(request):
    return render(request, 'VehicleService/current.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "kallz_app/dashboard.html")

def classes(request):
    return render(request, "kallz_app/classes.html")

def userPage(request):
    context = {}
    return render(request, 'kallz_app/user.html', context)

def about(request):
    return render(request, "kallz_app/about.html")

def index(request):
    return render(request, "kallz_app/index.html")


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user )

            return redirect('login')

    context = {'form' : form}
    return render(request, 'kallz_app/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        #check if the user is there before redirect 

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')   
                #if information is wrong 
    context = {}
    return render(request, 'kallz_app/login.html', context)    

def logoutUser(request):
    logout(request)
    return redirect('login')



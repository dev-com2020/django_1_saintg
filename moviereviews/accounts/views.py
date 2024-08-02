from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .forms import UserCreateForm


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html',
                      {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupaccount.html',
                              {'form': UserCreateForm,
                               'error': 'user już jest!'})
        else:
            return render(request, 'signupaccount.html',
                          {'form': UserCreateForm,
                           'error': 'Hasła nie pasują'})


def logoutaccount(request):
    logout(request)
    return redirect('home')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html',
                      {'form': AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html',
                          {'form': AuthenticationForm(),
                           'error': 'nieprawidłowe dane'})
        else:
            login(request, user)
            return redirect('home')

# https://github.com/dev-com2020/django_1_saintg

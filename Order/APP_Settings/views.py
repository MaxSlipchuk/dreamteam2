from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def settings(request):
    return render(request, 'APP_Settings/APP_Settings.html')

def user_logout(request):

    logout(request)

    return redirect("login")

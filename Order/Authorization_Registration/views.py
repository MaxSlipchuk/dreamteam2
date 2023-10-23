from django.shortcuts import render

# Create your views here.

def registration(request):
    return render(request, "Authorization_Registration/Authorization_Registration.html")

def login(request):
    return render(request, "Authorization_Registration/login.html")
    
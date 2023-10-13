from django.shortcuts import render

# Create your views here.

def settings(request):
    return render(request, 'APP_Settings/APP_Settings.html')

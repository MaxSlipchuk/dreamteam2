from django.shortcuts import render,redirect
from Authorization_Registration.models import Registration
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from Authorization_Registration.models import UpdateUser

# Create your views here.

def registration(request):
    context = {}
    if request.method == 'POST':
        login = request.POST.get("login")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        password = request.POST.get("password")
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        confirm_password = request.POST.get("confirm_password")
        context["login"] = login
        context["name"] = name
        context["surname"] = surname
        context["password"] = password
        context['telephone'] = telephone
        context['email'] = email
        context["confirm_password"] = confirm_password
        # hashed_password = make_password(password)
        
        if login and name and surname and password and confirm_password and telephone:
            if len(password) >= 8:
                if password == confirm_password:
                    try:            
                        UpdateUser.objects.create_user(
                            username=login, 
                            password=password,
                            first_name=name, 
                            last_name=surname,
                            telephone = telephone,
                            email=email
                        )
                        
                        
                        return redirect('login')   
                    except IntegrityError:
                        context['error'] = 'Такий користувач вже існує'
                else:           
                    context['error'] = 'Паролі не співпадають'                        
            else:
                context['error'] = 'Кількість символів має бути довшою або дорівнювати 8'
        else:
            context['error'] = 'Заповніть всі поля'

    return render(request, 'Authorization_Registration/Authorization_Registration.html', context)

def login_view(request): 
    context = {}
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:
        context['error'] = 'Ти вже авторизувався'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
            else:
                context['error'] = 'Логін або пароль невірні'
        else:
            context['error'] = 'Заповніть всі поля'

    return render(request, "Authorization_Registration/login.html", context)
            # return redirect('main_page')
                
            # else:
            #     context['error'] = 'Логін або пароль невірні'
        # else:
        #     context['error'] = 'Заповніть всі поля'
    # return render(request, "Authorization_Registration/login.html", context)
    # return render(request, "login/", context)

# def user_logout(request):
#     #
#     logout(request)
#     #
#     return redirect("login")



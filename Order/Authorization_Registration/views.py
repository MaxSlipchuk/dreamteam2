from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

def registration(request):
    context = {}
    if request.method == 'POST':
        login = request.POST.get("login")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        password = request.POST.get("password")
        context["login"] = login
        context["name"] = name
        context["surname"] = surname
        context["password"] = password
        
        if login and name and surname and password:
            if len(password) >= 8:
                try:
                    User.objects.create_user(
                        username=login, 
                        password=password,
                        first_name=name, 
                        last_name=surname
                    )
                    return redirect('login')
                except IntegrityError:
                        context['error'] = 'Такий користувач вже існує'
            else:
                context['error'] = 'Кількість символів має бути довшою або дорівнювати 8'
        else:
            context['error'] = 'Заповніть всі поля'

    return render(request, 'Authorization_Registration/Authorization_Registration.html', context)

def login(request):
    context = {}
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
    # return render(request, "login/", context)



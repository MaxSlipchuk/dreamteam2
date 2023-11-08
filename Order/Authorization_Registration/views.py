from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError

# Create your views here.

def registration(request):
    context = {}
    if request.method == 'POST':
        login = request.POST.get("login")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        password = request.POST.get("password")
        telephone = request.POST.get('telephone')
        context["login"] = login
        context["name"] = name
        context["surname"] = surname
        context["password"] = password
        context['telephone'] = telephone
        
        if login and name and surname and password and telephone:
            if len(password) >= 8:
                try:
                    User.objects.create_user(
                        username=login, 
                        password=password,
                        first_name=name, 
                        last_name=surname,
                        # telephone = telephone
                    )
                    return redirect('login')
                except IntegrityError:
                        context['error'] = 'Такий користувач вже існує'
            else:
                context['error'] = 'Кількість символів має бути довшою або дорівнювати 8'
        else:
            context['error'] = 'Заповніть всі поля'

    return render(request, 'Authorization_Registration/Authorization_Registration.html', context)

def login_view(request): 
    context = {}
    if request.user.is_authenticated:
        context['error'] = 'Ти вже авторизувався'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request = request, user = user)
                return redirect('main_page')
            else:
                context['error'] = 'Логін або пароль невірні'
        else:
            context['error'] = 'Заповніть всі поля'
    return render(request, "Authorization_Registration/login.html", context)
    # return render(request, "login/", context)

def user_logout(request):
    #
    logout(request)
    #
    return redirect("login")



from django.shortcuts import render,redirect
from Authorization_Registration.models import Registration
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import check_password

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
                    user = Registration.objects.create(
                        login=login, 
                        password=password,
                        name=name, 
                        surname=surname,
                        phone_number = telephone
                    )
                    user.save()
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Отримати всіх користувачів з бази даних з вказаним логіном
        users = Registration.objects.filter(login=username)
        print(users)
        if users.exists() and check_password(password, users[0].password):
            try:
            # Якщо користувач існує і пароль вірний
                print()
                print(f"/n Успішний вхід для користувача: {username}")
                context['error'] = f'Успішний вхід для користувача: {username}'
            except:
                context['error'] = 'невдалося'
        else:
            # Якщо користувач не існує або пароль невірний
            print("Невірний логін або пароль")
            return redirect('main_page')
                
            # else:
            #     context['error'] = 'Логін або пароль невірні'
        # else:
        #     context['error'] = 'Заповніть всі поля'
    return render(request, "Authorization_Registration/login.html", context)
    # return render(request, "login/", context)

def user_logout(request):
    #
    logout(request)
    #
    return redirect("login")



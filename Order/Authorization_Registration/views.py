from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from Authorization_Registration.models import UserProfile
from shopping_cart_page.models import ShoppingCart

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
        
        if login and name and surname and password and confirm_password and telephone and email:
            if len(password) >= 8:
                if password == confirm_password:
                    try:   
                        UserProfile.create_user_profile(
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


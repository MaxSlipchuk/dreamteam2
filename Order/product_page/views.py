from django.shortcuts import render
from product_page.models import Perfum
from Authorization_Registration.models import *
from shopping_cart_page.models import ShoppingCart
# import shopping_cart_page.templates.shopping_cart_page.ShoppingCart

# Create your views here.

def product(request):
    perfums = Perfum.objects.all()

    context = {}
    context['perfums'] = perfums
    name = request.POST.get('perfum_name')
    price = request.POST.get('perfum_price')

    # print("Парфум:", name)
    # print("Ціна:", price)

    # if request.user.is_authenticated:
    #     user = request.user.username

        
    #     user_f = ShoppingCart.objects.get(username=user)
    #     user_f.perfum_name = name
    #     user_f.price = price
    #     user_f.save()
        # ShoppingCart.objects.all()
        # print(username)
        # print(user_f)
        # print()


        # user_f.perfum_name = name
        # user_f.price = price
    


        # login = request.POST.get("login")
        # name = request.POST.get("name")
        # surname = request.POST.get("surname")
        # password = request.POST.get("password")
        # telephone = request.POST.get('telephone')
        # email = request.POST.get('email')
        # confirm_password = request.POST.get("confirm_password")
        # context["login"] = login
        # context["name"] = name
    
    return render(request, 'product_page/product_page.html', context)
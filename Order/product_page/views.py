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
 
    response = render(request, 'product_page/product_page.html', context)

    if request.method == "POST":
        perfume_id = request.POST.get('perfume_id')
        cart = request.COOKIES.get('cart')
        if not cart:
            cart = perfume_id
        else:
            cart += " " + perfume_id

        response.set_cookie("cart", cart)
    
    return response
from django.shortcuts import render, redirect
from product_page.models import Perfum
from django.http import HttpResponse

# Create your views here.

def shopping(request):
    context = {}

    cart = request.COOKIES.get('cart')
    
    if not cart:
        return render(request, 'shopping_cart_page/shopping_cart_page.html', context)

    list_products_id = cart.split(' ')
    
    if request.method == 'POST':
        if 'clear' in request.POST:
            # Очищення корзини
            response = render(request, 'shopping_cart_page/shopping_cart_page.html', context)
            response.delete_cookie('cart')
            return response
        # знаходимо id продукту який збираємось видалити
        product_id = request.POST.get('perfume_id')
        # видалення 
        while product_id in list_products_id:
            list_products_id.remove(product_id)
    
    # рахунок для номеру в корзині
    numb = 1

    list_products = []

    # для того, щоб не було повторень
    set_products = set()

    for id in list_products_id:
        if id not in set_products:
            set_products.add(id)
            product = Perfum.objects.get(id = id)
            product.number_in_cart = numb
            product.count_in_cart = list_products_id.count(id)
            product.sum_in_cart = product.count_in_cart * product.price
            list_products.append(product)
            numb += 1

    context['all_perfumes'] = list_products

    response = render(request, 'shopping_cart_page/shopping_cart_page.html', context)

    response.set_cookie('cart', ' '.join(list_products_id))

    return response
        
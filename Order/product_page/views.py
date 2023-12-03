from django.shortcuts import render
from product_page.models import Perfum


# Create your views here.

def product(request):
    perfums = Perfum.objects.all()

    # context = {
    #     'perfums': perfums
    # }

    return render(request, 'product_page/product_page.html', context={'perfums': perfums})
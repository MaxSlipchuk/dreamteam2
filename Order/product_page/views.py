from django.shortcuts import render, redirect
from product_page.models import Perfum


# Create your views here.

def product(request):
    context = {}

    context['eau'] = Perfum.objects.get(name='eau')
    context['dune'] = Perfum.objects.get(name='dune')
    context['fahrenheit'] = Perfum.objects.get(name='fahrenheit')
    context['higher'] = Perfum.objects.get(name='higher')
    context['home'] = Perfum.objects.get(name='home')
    context['jules'] = Perfum.objects.get(name='jules')

    return render(request, 'product_page/product_page.html', context)
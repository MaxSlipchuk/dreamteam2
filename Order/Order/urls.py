"""
URL configuration for Order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contact_page import views as contact
from main_page import views as main
from product_page import views as product
from shopping_cart_page import views as shopping
from Authorization_Registration import views as registr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_page/', contact.contact, name = 'contact_page'),
    path('', main.main, name = 'main_page'),
    path('product_page/', product.product, name = 'product_page'),
    path('shopping_cart_page/', shopping.shopping, name = 'shopping_cart_page'),
    path('Authorization_Registration/', registr.registration, name='Authorization_Registration')

]

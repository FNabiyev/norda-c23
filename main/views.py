from django.shortcuts import render
from .models import *

def Home(request):
    categories = Categories.objects.all()
    products = Product.objects.all().order_by('-id')[0:20]
    context = {
        'categories':categories,
        'products':products
    }

    return render(request, 'home.html', context)


def AboutUs(request):
    return render(request, 'about-us.html')


def Kategoriya(request):
    return render(request, 'kategoriya.html')


def Blog(request):
    return render(request, 'blog.html')


def Contact(request):
    return render(request, 'contact.html')


def Cart(request):
    return render(request, 'cart.html')

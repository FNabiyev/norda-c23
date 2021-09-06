from django.shortcuts import render
from .models import *


def Home(request):
    categories = Categories.objects.all()
    products = Product.objects.all().order_by('-id')[0:20]
    bans = Banner.objects.all()
    context = {
        'categories':categories,
        'products':products,
        'banners':bans,
    }

    return render(request, 'home.html', context)


def AboutUs(request):
    return render(request, 'about-us.html')


def Kategoriya(request, pk):
    products = Product.objects.filter(category_id=pk)
    if len(products) == 0:
        products = 0
    categories = Categories.objects.all()
    context = {
        'products':products,
        'categories':categories,
    }

    return render(request, 'kategoriya.html', context)


def Blog(request):
    return render(request, 'blog.html')


def Contact(request):
    return render(request, 'contact.html')


def Cart(request):
    return render(request, 'cart.html')

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *


def Home(request):
    categories = Categories.objects.all()
    products = Product.objects.all().order_by('-id')[0:20]
    bans = Banner.objects.all()
    shopitems = ShopItem.objects.filter(shop__client=request.user, shop__status=0)

    context = {
        'categories':categories,
        'products':products,
        'banners':bans,
        'shopitems':shopitems,
    }

    return render(request, 'home.html', context)


def AboutUs(request):
    return render(request, 'about-us.html')


def Kategoriya(request, pk):
    products = Product.objects.filter(category_id=pk)
    if len(products) == 0:
        products = 0
    categories = Categories.objects.all()
    shopitems = ShopItem.objects.filter(shop__client=request.user, shop__status=0)

    context = {
        'products':products,
        'categories':categories,
        'shopitems': shopitems,
    }

    return render(request, 'kategoriya.html', context)


def Blog(request):
    return render(request, 'blog.html')


def Contact(request):
    return render(request, 'contact.html')


def Cart(request):
    shopitems = ShopItem.objects.filter(shop__client=request.user, shop__status=0)
    shop = Shop.objects.filter(client=request.user, status=0)
    context = {
        'shopitems':shopitems,
        'shop':shop,
    }

    return render(request, 'cart.html', context)

def BuyurtmaBerish(request):
    shop = Shop.objects.filter(client=request.user, status=0)
    shop0 = shop[0]
    shop0.status = 1
    shop0.save()
    print(shop0.status)

    return redirect('/')

def AddToCart(request, id):
    product = Product.objects.get(id=id)
    try:
        shop = Shop.objects.get(client=request.user, status=0)
    except:
        shop = Shop.objects.create(client=request.user, total=0)
    if product.discount:
        ShopItem.objects.create(shop=shop, product=product, total=product.discount)
        shop.total += product.discount
        shop.save()
    else:
        ShopItem.objects.create(shop=shop, product=product, total=product.price)
        shop.total += product.price
        shop.save()

    return redirect('/')


def CountSavatcha(request):
    count = ShopItem.objects.filter(shop__client=request.user, shop__status=0)
    s = 0
    for c in count:
        s += c.total
    data = {
        'count': count.count(),
        'total': s
    }

    return JsonResponse(data)

def DeleteCart(request, id):
    shopitem = ShopItem.objects.get(id=id)
    shopitem.delete()

    return redirect('/')
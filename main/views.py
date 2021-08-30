from django.shortcuts import render


def Home(request):
    return render(request, 'home.html')


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

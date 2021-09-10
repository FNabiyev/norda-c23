from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('aboutus/', AboutUs),
    path('kategoriya/<int:pk>/', Kategoriya),
    path('blog/', Blog),
    path('contact/', Contact),
    path('cart/', Cart),
    path('addtocart/<int:id>/', AddToCart),
    path('count-savatcha/', CountSavatcha),
    path('buyurtmaberish/', BuyurtmaBerish),
    path('deletecart/<int:id>/', DeleteCart)
]
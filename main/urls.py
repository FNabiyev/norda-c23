from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('aboutus/', AboutUs),
    path('kategoriya/', Kategoriya),
    path('blog/', Blog),
    path('contact/', Contact),
    path('cart/', Cart),
]
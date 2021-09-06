from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('aboutus/', AboutUs),
    path('kategoriya/<int:pk>/', Kategoriya),
    path('blog/', Blog),
    path('contact/', Contact),
    path('cart/', Cart),
]
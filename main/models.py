from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    photo = models.ImageField('product')
    description = models.TextField()

    def __str__(self):
        return self.name


class Banner(models.Model):
    index = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    text = models.TextField()
    photo = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title


class Shop(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class ShopItem(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)

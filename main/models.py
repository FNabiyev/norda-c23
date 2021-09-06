from django.db import models

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
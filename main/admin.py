from django.contrib import admin
from .models import *

admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Banner)
# admin.site.register(Shop)
# admin.site.register(ShopItem)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total', 'date', 'status')
    list_display_links = ('id', 'client')
    list_filter = ('status',)
    date_hierarchy = 'date'


@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop', 'product', 'quantity', 'total')
    list_display_links = ('id', 'shop')

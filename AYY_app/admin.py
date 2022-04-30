from django.contrib import admin

from .models import Product
# Register your models here.



class ProductAdmin(admin.ModelAdmin):

    list_display = ('name' ,'price', 'type' ,'reference' ,'image_url')


admin.site.register(Product,ProductAdmin)

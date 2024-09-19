from django.contrib import admin
from .models import Product

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'image')

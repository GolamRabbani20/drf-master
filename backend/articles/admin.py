from django.contrib import admin
from .models import Article

@admin.register(Article)
class AritcleAdmin(admin.ModelAdmin):
    list_display = [
        'user' ,
        'title' ,
        'body' ,
        'tags',
        'make_public',
        'publish_date' 
    ]

from django.contrib import admin
from .models import Category, Menu

# Register your models here.
class CatAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    

class MenuAdmin(admin.ModelAdmin):
    list_display = ['item', 'desc', 'price', 'category', 'image']

admin.site.register(Category, CatAdmin)
admin.site.register(Menu, MenuAdmin)
from django.contrib import admin

from .models import category, Product
@admin.register(category)   
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'stock', 'category', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('category', 'created_at', 'updated_at')
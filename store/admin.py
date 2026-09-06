from django.contrib import admin
from .models import Category, Product, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock', 'skin_type', 'is_active', 'created_at')
    list_filter = ('category', 'skin_type', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('price', 'stock', 'is_active')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'full_name', 'phone', 'address', 'quantity', 'created_at', 'is_completed')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('full_name', 'phone', 'address')
    list_editable = ('is_completed',)
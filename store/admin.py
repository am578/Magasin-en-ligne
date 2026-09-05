from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # يكتب الـ slug تلقائياً عند كتابة الاسم


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # الأعدة التي تظهر في جدول المنتجات
    list_display = ('title', 'category', 'price', 'stock', 'skin_type', 'is_active')

    # خيارات الفلترة السريعة على اليمين
    list_filter = ('category', 'skin_type', 'is_active')

    # البحث بالاسم والوصف
    search_fields = ('title', 'description')

    # تعديل الحالة والسعر مباشرة من القائمة
    list_editable = ('price', 'stock', 'is_active')
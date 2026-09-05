from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الفئة")
    slug = models.SlugField(unique=True, verbose_name="الرابط المختصر (Slug)")

    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"

    def __str__(self):
        return self.name


class Product(models.Model):
    SKIN_TYPES = [
        ('all', 'جميع أنواع البشرة'),
        ('dry', 'جافة'),
        ('oily', 'دهنية'),
        ('combination', 'مختلطة'),
        ('sensitive', 'حساسة'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="الفئة")
    title = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="الوصف والفوائد")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر (دج)")
    stock = models.PositiveIntegerField(default=0, verbose_name="الكمية المتوفرة")
    skin_type = models.CharField(max_length=20, choices=SKIN_TYPES, default='all', verbose_name="نوع البشرة المناسب")
    how_to_use = models.TextField(blank=True, null=True, verbose_name="طريقة الاستعمال")
    image = models.ImageField(upload_to='products/', verbose_name="صورة المنتج")
    is_active = models.BooleanField(default=True, verbose_name="متوفر للعرض")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.title
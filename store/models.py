from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")
    slug = models.SlugField(unique=True, verbose_name="الرابط (Slug)")

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"

    def __str__(self):
        return self.name

class Product(models.Model):
    SKIN_CHOICES = [
        ('all', 'جميع انواع البشرة'),
        ('oily', 'البشرة الدهنية'),
        ('dry', 'البشرة الجافة'),
        ('sensitive', 'البشرة الحساسة'),
    ]

    title = models.CharField(max_length=200, verbose_name="عنوان المنتج")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="القسم")
    description = models.TextField(verbose_name="وصف المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    stock = models.PositiveIntegerField(default=10, verbose_name="الكمية المتوفرة")
    skin_type = models.CharField(max_length=20, choices=SKIN_CHOICES, default='all', verbose_name="نوع البشرة المناسب")
    how_to_use = models.TextField(blank=True, null=True, verbose_name="طريقة الاستعمال")
    image = models.ImageField(upload_to='products/', verbose_name="صورة المنتج")
    is_active = models.BooleanField(default=True, verbose_name="متوفر للعرض")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.title

class Order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="المنتج")
    full_name = models.CharField(max_length=100, verbose_name="الاسم الكامل")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    address = models.CharField(max_length=200, verbose_name="الولاية والعنوان")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    is_completed = models.BooleanField(default=False, verbose_name="تم التوصيل")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"
        ordering = ['-created_at']

    def __str__(self):
        return f"طلب {self.product.title} - {self.full_name}"
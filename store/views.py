from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# View لجلب كل الفئات
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# View لجلب كل المنتجات (مع إمكانية البحث والفلترة)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

# View لجلب تفاصيل منتج واحد بـ ID
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

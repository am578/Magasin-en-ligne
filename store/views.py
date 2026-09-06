from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import generics
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer


# 1. Views الخاصة بـ REST API
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


# 2. Views الخاصة بالصفحات (Django Templates)
def store_home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/index.html', {'products': products})

def create_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity', 1)

        product = get_object_or_404(Product, id=product_id)

        Order.objects.create(
            product=product,
            full_name=full_name,
            phone=phone,
            address=address,
            quantity=quantity
        )

        messages.success(request, f'شكراً لك يا {full_name}! تم إرسال طلبك بنجاح وسنتصل بك قريباً للتأكيد.')
        return redirect('home')


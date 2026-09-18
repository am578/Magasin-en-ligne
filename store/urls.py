from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, about

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('about/', about, name='about'),
]
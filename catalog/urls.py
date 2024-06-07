from django.urls import path

from .views import HomeView, ProductDetailView, ContactView, CategoryDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('category/<int:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]

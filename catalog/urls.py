from django.urls import path
from django.views.decorators.cache import cache_page

from .views import HomeView, ProductDetailView, ContactView, CategoryDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionCreateView, VersionUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('category/<int:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('version/create/', VersionCreateView.as_view(), name='version_create'),
    path('version/update/<int:pk>/', VersionUpdateView.as_view(), name='version_update'),
]

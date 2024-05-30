# from django.urls import path, include
# from catalog.apps import NewappConfig
# from catalog.views import home, contacts, product_detail
#
# app_name = NewappConfig.name
#
# urlpatterns = [
#     path('', home, name='home'),
#     path('contacts/', contacts, name='contacts'),
#     path('product/<int:pk>/', product_detail, name='product_detail'),
# ]
from django.urls import path

from django.urls import path
from .views import HomeView, ProductDetailView, ContactView, CategoryDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('category/<int:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
]


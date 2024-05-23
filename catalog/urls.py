from django.urls import path, include
from catalog.apps import NewappConfig
from catalog.views import home, contacts, product_detail

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]

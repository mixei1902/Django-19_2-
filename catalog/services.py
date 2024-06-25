from django.core.cache import cache

from .models import Category, Product


def get_cached_categories():
    '''
    Функция для получения списка категорий с кешированием.
    '''
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.all()
        cache.set('categories', categories, 60)
    return categories


def get_cached_products():
    '''
    Функция для получения списка продуктов с кешированием.
    '''
    products = cache.get('products')
    if not products:
        products = Product.objects.all()
        cache.set('products', products, 60)
    return products

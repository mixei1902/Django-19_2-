from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'object_list': products, 'categories': categories}
    return render(request, 'catalog/home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'object': product}
    return render(request, 'catalog/product_detail.html', context)


def contact(request):
    return render(request, 'catalog/contact.html')


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'catalog/category_detail.html', {
        'category': category,
        'products': products,
        'categories': categories
    })

from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'object': product}
    return render(request, 'catalog/product_detail.html', context)


def home(request):
    products = Product.objects.all()
    context = {'object_list': products}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТел: {phone}\nСообщение: {message}')
    return render(request, 'contacts.html')
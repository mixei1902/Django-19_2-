from django.views.generic import ListView, DetailView, TemplateView

from blog.models import BlogPost
from .models import Product, Category


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['blog_posts'] = BlogPost.objects.filter(is_published=True)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'object'


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'
    pk_url_kwarg = 'category_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.get_object())
        context['categories'] = Category.objects.all()
        return context

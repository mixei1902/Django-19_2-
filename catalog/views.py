from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost
from .forms import ProductForm, VersionForm
from .models import Product, Category, Version


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['blog_posts'] = BlogPost.objects.filter(is_published=True)
        return context


class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        if self.request.user.has_perm('catalog.can_change_any_product_description'):
            return self.model.objects.all()
        return self.model.objects.filter(owner=self.request.user)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        current_version = product.versions.filter(is_current=True).first()
        context['current_version'] = current_version
        return context


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


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'
    success_url = reverse_lazy('home')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'
    success_url = reverse_lazy('home')

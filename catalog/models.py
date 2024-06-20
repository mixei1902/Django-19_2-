from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание ппродукта")
    image = models.ImageField(upload_to='products/', verbose_name="изображение", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена",null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products',default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=100)
    version_name = models.CharField(max_length=100)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.version_name} ({self.version_number})"
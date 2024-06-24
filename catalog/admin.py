from django.contrib import admin

from .models import Product, Category, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class VersionInline(admin.TabularInline):
    model = Version
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    inlines = [VersionInline]

    def create_moderator_group():
        product_content_type = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.filter(content_type=product_content_type)

        moderator_group, created = Group.objects.get_or_create(name='Moderators')
        for permission in permissions:
            moderator_group.permissions.add(permission)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_current')
    list_filter = ('product', 'is_current')
    search_fields = ('version_number', 'version_name')

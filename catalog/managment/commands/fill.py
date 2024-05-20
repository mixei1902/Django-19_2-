import json

from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('fixtures/categories.json', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('fixtures/products.json', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for category_data in Command.json_read_categories():
            category = category_data['fields']
            category_for_create.append(
                Category(id=category_data['pk'], name=category['name'], description=category['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for product_data in Command.json_read_products():
            product = product_data['fields']
            product_for_create.append(
                Product(
                    id=product_data['pk'],
                    name=product['name'],
                    description=product['description'],
                    image=product['image'],
                    category=Category.objects.get(pk=product['category']),
                    price=product['price'],
                    created_at=product['created_at'],
                    updated_at=product['updated_at']
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))

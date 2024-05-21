import json

from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    @staticmethod
    def json_read_categories():
        with open('fixtures/categories.json') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('fixtures/products.json') as file:
            return json.load(file)

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category_data in Command.json_read_categories():
            category = category_data['fields']
            category_for_create.append(
                Category(id=category_data['pk'], name=category['name'], description=category['description'])
            )

        Category.objects.bulk_create(category_for_create)

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

        Product.objects.bulk_create(product_for_create)
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))

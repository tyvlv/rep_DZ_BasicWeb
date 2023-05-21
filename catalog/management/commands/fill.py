import json

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        Product.objects.all().delete()

        with open('data.json', 'r') as file:
            data = json.load(file)

            product_objects = []
            for item in data:
                product_objects.append(Product(**item['fields']))

        Product.objects.bulk_create(product_objects)

import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.update_or_create(
                id=phone['id'],
                defaults={
                    'name': phone['name'],
                    'image': phone['image'],
                    'price': int(phone['price']),
                    'release_date': phone['release_date'],
                    'lte_exists': phone['lte_exists'].lower() in ('true', '1'),
                    'slug': slugify(phone['name'])
                }
            )

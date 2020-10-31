from book.models import Category

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):

    def handle(self, **options):
        fake = Faker()
        for _ in range(100):
            Category.objects.create(name=fake.last_name())

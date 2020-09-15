import random

from book.models import Book


from django.core.management.base import BaseCommand


from faker import Faker


class Command(BaseCommand):
    # help = 'Generate books'

    def add_arguments(self, parser):
        parser.add_argument('books_number', type=int, nargs='?', default=100)

    def handle(self, **options):
        fake = Faker()
        books_number = options['books_number']
        for _ in range(books_number):
            Book.objects.create(
                author=fake.last_name(),
                title=fake.first_name(),
                year=random.randint(1900, 2020),
            )

import random
from user.models import User

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    # help = 'generate random data'

    def add_arguments(self, parser):
        parser.add_argument('users_number', type=int, nargs='?', default=100)

    def handle(self, **options):
        fake = Faker()
        users_number = options['users_number']
        for _ in range(users_number):
            User.objects.create(
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(1, 100)
            )

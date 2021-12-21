import random
import secrets

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand  # , CommandError

from faker import Faker


def email(fake):
    domain = ['@icloud.com', '@gmail.com', '@outlook.com', '@yahoo.com']
    return fake.email().split('@')[0] + domain[random.randint(0, 3)]


class Command(BaseCommand):
    help = 'Creates the specified number of new users. You must specify a number in the range [1; 10]'      # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('add_users', nargs='+', type=int, choices=range(1, 10), help='The passed value of the '
                                                                                         'created users')

    def handle(self, *args, **options):
        for value in options['add_users']:
            for j in range(value):
                # try:
                fake = Faker()
                person = fake.name()
                first_name = person.split()[0] if person.split()[0][-1] != '.' else person.split()[1]
                last_name = person.split()[1] if person.split()[0][-1] != '.' else person.split()[1] + person.split()[2]
                user_name = [first_name, last_name][random.randint(0, 1)] + str(random.randint(1, 883322))
                user = User.objects.create_user(user_name, email(fake), secrets.token_urlsafe(32))
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                # except SomeError: idk.
                #   raise CommandError('We caught some Error')

                self.stdout.write(self.style.SUCCESS('Successfully added user "%s"' % user_name))
                """
                Alternative
                        for value in options['add_users']:
                            for j in range(value):
                                fake = Faker()
                                p = Person.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),
                                                            email=fake.email(), password=secrets.token_urlsafe(32),
                                                            username=some_user_name)
                self.stdout.write(self.style.SUCCESS('Successfully added user "%s"' % user_name))
                """  # noqa: E501

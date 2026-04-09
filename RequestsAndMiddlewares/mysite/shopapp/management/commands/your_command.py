from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username of the user')
        parser.add_argument('--delivery_address', type=str, help='Delivery address')
        parser.add_argument('--promocode', type=str, help='Promocode')

    def handle(self, *args, **options):
        username = options['username']
        delivery_address = options['delivery_address']
        promocode = options['promocode']

        if not username:
            self.stdout.write(self.style.ERROR('Please provide a username'))
            return

        user = User.objects.get(username=username)
        order, created = Order.objects.get_or_create(
            delivery_address=delivery_address or 'xxx',
            promocode=promocode or '12341234',
            user=user
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Order created for user {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'Order already exists for user {username}'))
from django.core.management import BaseCommand

from posts.models import Channel


def filldb():
    Channel.objects.update_or_create(
        username='test_phystechjob_parser',
        defaults=dict(name='test_phystechjob_parser', link='https://t.me/test_phystechjob_parser')
    )


class Command(BaseCommand):

    def handle(self, *args, **options):
        filldb()
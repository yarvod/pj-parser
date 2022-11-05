from django.conf import settings
from django.core.management import BaseCommand

from bot.models import Channel


def filldb():
    Channel.objects.update_or_create(
        username=settings.CHANNEL,
        defaults=dict(name=settings.CHANNEL, link=f'https://t.me/{settings.CHANNEL}', is_active=True)
    )


class Command(BaseCommand):

    def handle(self, *args, **options):
        filldb()

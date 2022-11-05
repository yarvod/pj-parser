import logging

from telethon.sync import events
from django.core.management import BaseCommand

from bot import tasks
from bot.client import client
from bot.models import Channel
from posts.serializers import MessageRawSeralizer

logger = logging.getLogger(__name__)


def main() -> None:
    client.start()

    @client.on(events.NewMessage(chats=list(Channel.objects.filter(is_active=True).values_list('username', flat=True))))
    async def newMessageListener(event):
        logger.info(f"Recieved from {event.chat.username} message {event.message.message}")
        tasks.process_message.apply_async(kwargs=dict(
            channel_username=event.chat.username,
            message=MessageRawSeralizer(event.message).data,
        ))

    with client:
        client.run_until_disconnected()


class Command(BaseCommand):

    def handle(self, *args, **options):
        main()

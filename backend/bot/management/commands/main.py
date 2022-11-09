import logging

from telethon import events
from django.core.management import BaseCommand

from bot import tasks
from bot.client import client
from posts.serializers import MessageRawSeralizer

logger = logging.getLogger(__name__)


def main() -> None:
    client.start()

    @client.on(events.NewMessage())
    async def newMessageListener(event):
        if hasattr(event.chat, 'username'):
            logger.info(f"Recieved from {event.chat.username} message {event.message.message}")
            tasks.process_message.apply_async(kwargs=dict(
                channel_username=event.chat.username,
                message=MessageRawSeralizer(event.message).data,
            ))
        else:
            logger.info(f"Received message NOT from channel/chat")

    with client:
        client.run_until_disconnected()


class Command(BaseCommand):

    def handle(self, *args, **options):
        main()

import logging

from backend.celery import app
from bot.models import Channel
from posts.models import RawPost, MessageEntity

logger = logging.getLogger(__name__)


@app.task
def process_message(channel_username: str, message: dict):
    logger.info("Start process message")
    try:
        channel = Channel.objects.get(username=channel_username)
    except Channel.DoesNotExist:
        logger.error(f"Channel {channel_username} NOT FOUND")
        return
    raw_post = RawPost.objects.create(channel=channel, text=message.get('message'))
    for entity in message.get('entities'):
        MessageEntity.objects.create(
            post=raw_post,
            type=entity['entity']['type'],
            text=entity['text'],
            offset=entity['entity']['offset'],
            length=entity['entity']['length'],
            url=entity['entity']['url']
        )
    # process raw_post
    # vacancy = some_nlp_funcion(raw_post.text)
    # Vacancy.objects.create(**vacancy)
    # POST Vacancy to phystechjob.ru

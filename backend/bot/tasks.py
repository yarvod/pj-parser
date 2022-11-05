import logging

from backend.celery import app
from bot.models import Channel
from posts.models import RawPost

logger = logging.getLogger(__name__)


@app.task
def process_message(channel_username: str, message: str):
    logger.info("Start process message")
    try:
        channel = Channel.objects.get(username=channel_username)
    except Channel.DoesNotExist:
        logger.error(f"Channel {channel_username} NOT FOUND")
        return
    raw_post, _ = RawPost.objects.create(channel=channel, text=message)
    # process raw_post
    # vacancy = some_nlp_funcion(raw_post.text)
    # Vacancy.objects.create(**vacancy)
    # POST Vacancy to phystechjob.ru

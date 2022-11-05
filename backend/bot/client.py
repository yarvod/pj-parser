from django.conf import settings
from telethon.sync import TelegramClient


def get_client():
    api_id = settings.API_ID
    api_hash = settings.API_HASH
    return TelegramClient('session', api_id, api_hash)


client = get_client()

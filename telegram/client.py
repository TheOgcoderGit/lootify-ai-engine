from telethon import TelegramClient
from settings import API_ID, API_HASH

client = TelegramClient(
    "lootify_session",
    int(API_ID),
    API_HASH
)

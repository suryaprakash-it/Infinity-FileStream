from telegram_client import bot
from config import Config

bot = Client(
    "InfinityFileStream",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)
from pyrogram import Client
from config import Config
from handlers import register_handlers

app = Client(
    "InfinityFileStream",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

register_handlers(app)

app.run()
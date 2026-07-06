from pyrogram import Client
from config import Config

bot = Client(
    "InfinityFileStream",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

from pyrogram import idle

bot.start()

print("🤖 Bot is waiting for updates...")

idle()

bot.stop()
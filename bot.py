from telegram_client import bot
from handlers import register_handlers

register_handlers(bot)

print("🤖 Infinity FileStream Bot Started!")

bot.run()
from telegram_client import telegram
from handlers import register_handlers

register_handlers(telegram)

print("🤖 Infinity FileStream Bot Started!")

telegram.run()
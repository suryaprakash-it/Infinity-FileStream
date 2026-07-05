from pyrogram import filters
from database import add_user

async def start_handler(client, message):
    await add_user(message.from_user.id)

    await message.reply_text(
        "👋 **Welcome to Infinity FileStream Bot!**\n\n"
        "📤 Send me any file.\n"
        "🔗 I'll generate a download link for you."
    )

def register(app):
    app.on_message(filters.command("start"))(start_handler)
from pyrogram import filters

async def start_handler(client, message):
    await message.reply_text(
        "👋 Welcome to Infinity FileStream Bot!\n\n"
        "📤 Send me any file to generate a download link."
    )

def register(app):
    app.on_message(filters.command("start"))(start_handler)
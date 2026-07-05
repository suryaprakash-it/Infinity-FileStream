from pyrogram import filters
from config import Config
from database import total_users, total_files

async def stats_handler(client, message):
    if message.from_user.id not in Config.ADMINS:
        return

    users = await total_users()
    files = await total_files()

    await message.reply_text(
        f"📊 **Bot Statistics**\n\n"
        f"👥 Users: `{users}`\n"
        f"📁 Files: `{files}`"
    )

def register(app):
    app.on_message(filters.command("stats"))(stats_handler)
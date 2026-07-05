import secrets
from pyrogram import filters
from database import add_file
from config import Config

async def upload_handler(client, message):
    media = (
        message.document
        or message.video
        or message.audio
        or message.photo
    )

    if not media:
        return

    file_code = secrets.token_urlsafe(8)

    data = {
        "_id": file_code,
        "file_id": media.file_id,
        "file_name": getattr(media, "file_name", "Unknown"),
        "file_size": media.file_size,
        "user_id": message.from_user.id
    }

    await add_file(data)

    link = f"{Config.BASE_URL}/file/{file_code}"

    await message.reply_text(
        f"✅ File uploaded successfully!\n\n🔗 {link}"
    )

def register(app):
    app.on_message(
        filters.document |
        filters.video |
        filters.audio |
        filters.photo
    )(upload_handler)
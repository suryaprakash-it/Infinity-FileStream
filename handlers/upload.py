from pyrogram import filters
from utils import generate_file_code, get_timestamp
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

    file_code = generate_file_code()

    file_name = getattr(media, "file_name", None)
    if not file_name:
        file_name = f"{media.file_unique_id}"

    data = {
        "_id": file_code,
        "file_id": media.file_id,
        "file_unique_id": media.file_unique_id,
        "file_name": file_name,
        "file_size": media.file_size,
        "chat_id": message.chat.id,
        "message_id": message.id,
        "uploaded_by": message.from_user.id,
        "uploaded_at": get_timestamp()
    }

    await add_file(data)

    link = f"{Config.BASE_URL}/file/{file_code}"

    await message.reply_text(
        f"✅ **File Uploaded Successfully!**\n\n"
        f"🔗 {link}"
    )


def register(app):
    app.on_message(
        filters.document
        | filters.video
        | filters.audio
        | filters.photo
    )(upload_handler)
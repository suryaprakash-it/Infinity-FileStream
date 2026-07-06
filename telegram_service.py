from telegram_client import telegram

async def get_file(file_id):
    return await telegram.get_messages(
        chat_id="me",
        message_ids=file_id
    )
from fastapi.responses import RedirectResponse
from telegram_client import bot

@app.get("/download/{file_code}")
async def download_file(file_code: str):

    file = await get_file(file_code)

    if not file:
        return HTMLResponse(
            "<h2>❌ File Not Found</h2>",
            status_code=404
        )

    tg_file = await bot.get_messages(
        file["chat_id"],
        file["message_id"]
    )

    media = (
        tg_file.document
        or tg_file.video
        or tg_file.audio
        or tg_file.photo
    )

    return RedirectResponse(
        media.file_id
    )
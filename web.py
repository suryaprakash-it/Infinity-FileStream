from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
from telegram_client import bot
from database import get_file
import os
from handlers import register_handlers

templates = Jinja2Templates(directory="templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🤖 Starting Bot...")

    register_handlers(bot)
    print("✅ Handlers Registered!")

    await bot.start()
    print("✅ Bot Started!")

    yield

    await bot.stop()


app = FastAPI(
    title="Infinity FileStream",
    version="1.0.0",
    lifespan=lifespan
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home():
    return {
        "status": "online",
        "project": "Infinity FileStream"
    }


@app.get("/file/{file_code}", response_class=HTMLResponse)
async def file_page(request: Request, file_code: str):

    file = await get_file(file_code)

    if not file:
        return HTMLResponse(
            "<h2>❌ File Not Found</h2>",
            status_code=404
        )

    return templates.TemplateResponse(
        request,
        "download.html",
        {
            "file_name": file["file_name"],
            "file_size": file["file_size"],
            "file_code": file_code
        }
    )


@app.get("/download/{file_code}")
async def download_file(file_code: str):

    file = await get_file(file_code)

    if not file:
        return HTMLResponse(
            "<h2>❌ File Not Found</h2>",
            status_code=404
        )

    msg = await bot.get_messages(
        file["chat_id"],
        file["message_id"]
    )

    os.makedirs("downloads", exist_ok=True)

    path = await bot.download_media(
        msg,
        file_name=f"downloads/{file['file_name']}"
    )

    return FileResponse(
        path=path,
        filename=file["file_name"],
        media_type="application/octet-stream"
    )
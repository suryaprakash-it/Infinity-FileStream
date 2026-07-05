from pyrogram import Client, filters

API_ID = 12345678
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

app = Client(
    "InfinityFileStreamBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Hello!\n\nWelcome to Infinity FileStream Bot.\n\nSend me any file and I'll generate a download link."
    )

@app.on_message(filters.document | filters.video | filters.audio | filters.photo)
async def receive_file(client, message):
    await message.reply_text("✅ File received! Link generation will be added next.")

print("Bot is starting...")

app.run()
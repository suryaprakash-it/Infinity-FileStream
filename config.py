import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    MONGO_URI = os.getenv("MONGO_URI")

    BOT_USERNAME = os.getenv("BOT_USERNAME")

    BASE_URL = os.getenv("BASE_URL")

    ADMINS = list(map(int, os.getenv("ADMINS", "").split())) if os.getenv("ADMINS") else []
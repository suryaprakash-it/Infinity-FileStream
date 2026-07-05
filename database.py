from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

client = AsyncIOMotorClient(Config.MONGO_URI)

db = client["InfinityFileStream"]

files = db["files"]
users = db["users"]


async def add_file(data: dict):
    await files.insert_one(data)


async def get_file(file_id: str):
    return await files.find_one({"_id": file_id})


async def add_user(user_id: int):
    if not await users.find_one({"_id": user_id}):
        await users.insert_one({"_id": user_id})


async def total_users():
    return await users.count_documents({})


async def total_files():
    return await files.count_documents({})




async def get_file(file_code: str):
    return await files.find_one({"_id": file_code})


async def delete_file(file_code: str):
    await files.delete_one({"_id": file_code})


async def update_file(file_code: str, data: dict):
    await files.update_one(
        {"_id": file_code},
        {"$set": data}
    )
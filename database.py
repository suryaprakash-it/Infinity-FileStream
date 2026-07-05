from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

client = AsyncIOMotorClient(Config.MONGO_URI)

db = client["InfinityFileStream"]

files = db["files"]
users = db["users"]


# ==========================
# FILES
# ==========================

async def add_file(data: dict):
    await files.insert_one(data)


async def get_file(file_code: str):
    return await files.find_one({"_id": file_code})


async def get_file_by_unique_id(file_unique_id: str):
    return await files.find_one(
        {"file_unique_id": file_unique_id}
    )


async def update_file(file_code: str, data: dict):
    await files.update_one(
        {"_id": file_code},
        {"$set": data}
    )


async def delete_file(file_code: str):
    await files.delete_one({"_id": file_code})


async def total_files():
    return await files.count_documents({})


# ==========================
# USERS
# ==========================

async def add_user(user_id: int):

    if await users.find_one({"_id": user_id}):
        return

    await users.insert_one(
        {
            "_id": user_id
        }
    )


async def total_users():
    return await users.count_documents({})
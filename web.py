from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {
        "status": "online",
        "bot": "Infinity FileStream"
    }

@app.get("/file/{file_id}")
async def get_file(file_id: str):
    return {
        "message": "Download system coming soon!",
        "file_id": file_id
    }
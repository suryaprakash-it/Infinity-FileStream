from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import get_file

app = FastAPI(
    title="Infinity FileStream",
    version="1.0.0"
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
        "download.html",
        {
            "request": request,
            "file_name": file["file_name"],
            "file_size": file["file_size"],
            "file_code": file_code
        }
    )
@app.get("/download/{file_code}")
async def download_file(file_code: str):

    file = await get_file(file_code)

    if not file:
        return HTMLResponse(
            "<h2>❌ File Not Found</h2>",
            status_code=404
        )

    return HTMLResponse(
        "<h2>🚧 Download system is being connected...</h2>"
    )
import os
import asyncio
import tempfile
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
import yt_dlp

app = FastAPI()

# HTML form for user input
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/download")
async def download_video(url: str = Form(...)):
    # Create a temporary file path
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "%(title)s.%(ext)s")

    ydl_opts = {
        'outtmpl': file_path,
        'format': 'mp4/bestaudio/best',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        downloaded_file = ydl.prepare_filename(info)

    # Schedule file deletion after 10 seconds
    asyncio.create_task(delete_after(downloaded_file, 10))

    return FileResponse(
        downloaded_file,
        filename=os.path.basename(downloaded_file),
        media_type="video/mp4"
    )

async def delete_after(path: str, delay: int):
    await asyncio.sleep(delay)
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted {path}")
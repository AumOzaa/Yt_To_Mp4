from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
import yt_dlp
import os
import uuid

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <form action="/download" method="post">
        <input type="text" name="url" placeholder="Enter video URL">
        <button type="submit">Download</button>
    </form>
    """

@app.post("/download")
def download(url: str = Form(...)):
    video_id = str(uuid.uuid4())
    filename = f"{video_id}.mp4"
    ydl_opts = {"outtmpl": filename, "format": "mp4"}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return FileResponse(filename, filename=filename, media_type="video/mp4")

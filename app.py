from fastapi import FastAPI, Form, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import yt_dlp
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/download")
def download_video(url: str = Form(...)):
    ydl_opts = {"quiet": True, "noplaylist": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get("formats", [info])
        mp4_formats = [f for f in formats if f.get("ext") == "mp4" and f.get("acodec") != "none"]
        if not mp4_formats:
            return {"error": "No suitable mp4 format found"}
        direct_url = mp4_formats[-1]["url"]

    # Stream video with headers
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(direct_url, headers=headers, stream=True)

    return StreamingResponse(
        r.iter_content(chunk_size=1024*1024),
        media_type="video/mp4",
        headers={"Content-Disposition": f'attachment; filename="{info["title"]}.mp4"'}
    )

YouTube to MP4 Downloader
A simple web application built with FastAPI to download YouTube videos as MP4 files. The user provides a YouTube video URL, and the server processes the download and serves the video file back to the user. The downloaded file is automatically deleted from the server after a short period to save space.

Features
Web Interface: Simple HTML form to input the YouTube video URL.

High-Quality Downloads: Downloads the best available MP4 format.

Temporary Storage: Files are stored temporarily and automatically deleted after 10 seconds to keep the server clean.

Asynchronous Operations: Uses asyncio for non-blocking file deletion.

Fast: Built on the high-performance FastAPI framework.

Technologies Used
Backend: Python, FastAPI

YouTube Downloader: yt-dlp

Web Server: Uvicorn

Getting Started
Follow these instructions to get a local copy up and running.

Prerequisites
Make sure you have Python 3.7+ and pip installed on your system. The project structure should include your main Python script and a templates directory containing index.html.

.
├── main.py
└── templates/
    └── index.html

Installation & Setup
Clone the repository:

git clone https://github.com/AumOzaa/Yt_To_Mp4.git
cd Yt_To_Mp4

Create and activate a virtual environment (recommended):

Windows:

python -m venv venv
.\venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Install the required dependencies:
Create a requirements.txt file with the following content:

fastapi
uvicorn[standard]
yt-dlp
python-multipart

Then, install the packages:

pip install -r requirements.txt

Running the Application
Start the server:
Run the following command in your terminal from the project's root directory. Replace main with the name of your Python file (e.g., app.py).

uvicorn main:app --reload

Open the application:
Open your web browser and navigate to http://127.0.0.1:8000.

API Endpoints
GET /
Description: Serves the main HTML page with a form to enter the YouTube URL.

Response: HTMLResponse containing the content of templates/index.html.

POST /download
Description: Handles the video download request.

Form Data:

url (string, required): The URL of the YouTube video to download.

Response: FileResponse that streams the downloaded MP4 file to the user. The file is then deleted from the server.

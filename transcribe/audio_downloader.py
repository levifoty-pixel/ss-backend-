import yt_dlp
import os
import uuid

def download_audio(youtube_url):
    # Create a unique filename so multiple users don't collide
    output_id = str(uuid.uuid4())
    output_path = f"downloads/{output_id}.mp3"

    # Make sure the downloads folder exists
    os.makedirs("downloads", exist_ok=True)

    # yt-dlp options for extracting audio
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": True
    }

    # Download the audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    return output_path


import yt_dlp

print("Paste your YouTube URL:")
link = input("")

# Download options
ydl_opts = {
            'format': 'bestaudio/best',  # Add any required yt_dlp options here
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
    print("Downloading...")



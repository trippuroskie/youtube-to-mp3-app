import streamlit as st
import yt_dlp

st.title("Youtube to MP3 Converter")

# Streamlit UI
link = st.text_input("Input your link here:")

if st.button("Download Audio"):
    # Placeholder for the "Downloading..." message
    status_placeholder = st.empty()
    status_placeholder.write("Downloading...")
    
    try:
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
        # Update the status once the download finishes
        status_placeholder.write(f"Finished downloading {link}")
    except Exception as e:
        # Handle and display errors
        status_placeholder.write(f"An error occurred: {e}")

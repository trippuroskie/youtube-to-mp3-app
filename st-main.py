import streamlit as st
import yt_dlp
import os

st.title("YouTube to MP3 Converter")

# Streamlit UI
link = st.text_input("Input your link here:")

if st.button("Download Audio"):
    # Placeholder for the "Downloading..." message
    status_placeholder = st.empty()
    status_placeholder.write("Downloading...")

    try:
        # Path to the Downloads folder
        download_folder = os.path.expanduser("~/Downloads")
        # Custom output template: Save as MP3 in the Downloads folder
        output_template = os.path.join(download_folder, "%(title)s.%(ext)s")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,  # Specify the output directory and file name
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        
        # Update the status once the download finishes
        status_placeholder.write(f"Download complete! File saved to {download_folder}")
    except Exception as e:
        # Handle and display errors
        status_placeholder.write(f"An error occurred: {e}")

import streamlit as st
import yt_dlp
from io import BytesIO
import os

st.title("YouTube to MP3 Converter")

# Streamlit UI
link = st.text_input("Input your YouTube link here:")

# Conversion state button (always visible)
convert_button_clicked = st.button("Convert to MP3")
status_placeholder = st.empty()  # Placeholder for the status message

# Proceed only if a link is provided and the button is clicked
if convert_button_clicked:
    if not link:
        status_placeholder.error("Please provide a valid YouTube link.")
    else:
        status_placeholder.text("Converting...")  # Display "Converting..." message

        try:
            # Prepare MP3 conversion function
            def convert_to_mp3():
                temp_file = BytesIO()  # Temporary in-memory file

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': 'temp_audio.%(ext)s',  # Save to a temporary file
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Extract and download audio
                    info_dict = ydl.extract_info(link, download=True)
                    mp3_title = info_dict.get('title', 'audio') + ".mp3"

                    # Read the downloaded file into memory
                    with open("temp_audio.mp3", "rb") as audio_file:
                        temp_file.write(audio_file.read())

                # Clean up temporary file
                os.remove("temp_audio.mp3")

                temp_file.seek(0)  # Reset buffer position for downloading
                return temp_file, mp3_title

            # Convert to MP3 and get file
            temp_file, mp3_title = convert_to_mp3()

            # Update the status message
            status_placeholder.text("Conversion complete! Ready for download.")

            # Show the download button
            if st.download_button(
                label="Download MP3",
                data=temp_file,
                file_name=mp3_title,
                mime="audio/mpeg",
            ):
                status_placeholder.text("Downloading...")  # Update to "Downloading..."

        except Exception as e:
            # Handle and display errors
            status_placeholder.text(f"An error occurred: {e}")

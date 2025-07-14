import streamlit as st
import yt_dlp
import uuid
import os

st.title("🎥 Video Downloader")

url = st.text_input("🔗 Enter Video URL")

if st.button("Download"):
    st.info("📥 Downloading... Please wait.")

    unique_filename = f"{uuid.uuid4()}.mp4"

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': unique_filename,
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open(unique_filename, "rb") as f:
            st.download_button("📂 Click here to Download", f, file_name=unique_filename)

        os.remove(unique_filename)

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

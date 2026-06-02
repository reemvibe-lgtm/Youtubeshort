import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Universal Downloader", page_icon="⬇️")

st.title("⬇️ Universal No-Watermark Downloader")
url = st.text_input("ضعي رابط المقطع هنا (تيك توك، انستغرام، تويتر، يوتيوب):")

if st.button("تحميل الفيديو"):
    if url:
        with st.spinner("جاري استخراج رابط الفيديو الخام..."):
            try:
                ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                st.success("تم التحميل بنجاح!")
                with open("video.mp4", "rb") as file:
                    st.download_button("📥 اضغطي هنا لحفظ المقطع في جهازك", file, "video.mp4")
                
                # تنظيف الملف بعد العرض
                os.remove("video.mp4")
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

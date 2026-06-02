import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Universal Downloader", page_icon="⬇️")

st.title("⬇️ Universal No-Watermark Downloader")
url = st.text_input("ضعي رابط المقطع هنا:")

if st.button("تحميل الفيديو"):
    if url:
        with st.spinner("جاري الاتصال.. (ننتحل شخصية متصفح حقيقي لتجاوز الحظر)"):
            try:
                # هذه الإعدادات تجعل السيرفر يظهر كمتصفح طبيعي (تتجاوز الحظر)
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'video.mp4',
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'quiet': True,
                    'no_warnings': True
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                st.success("تم التحميل بنجاح!")
                with open("video.mp4", "rb") as file:
                    st.download_button("📥 اضغطي هنا للحفظ", file, "video.mp4")
                
            except Exception as e:
                st.error(f"حدث خطأ: {e}. (قد يكون الرابط محظوراً أو يتطلب اشتراكاً)")

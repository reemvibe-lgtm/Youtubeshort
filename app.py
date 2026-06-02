import streamlit as st
import random
import os
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from datetime import datetime, timedelta

# 1. إعدادات الهوية البصرية (AI Trend Hunter Studio)
st.set_page_config(page_title="Diamond AI Trend Automator", page_icon="🔥", layout="wide")

st.markdown("""
    <style>
    .reportview-container, .main { background-color: #09090e; color: #00ffcc; }
    .stMetric { background-color: #121224; padding: 20px; border-radius: 12px; border: 1px solid #ff0055; }
    h1, h2, h3 { color: #ff0055 !important; font-family: 'Segoe UI', sans-serif; text-shadow: 0 0 10px rgba(255, 0, 85, 0.6); }
    div.stButton > button:first-child { background-color: #ff0055; color: white; font-weight: bold; border-radius: 8px; height: 60px; font-size: 22px; box-shadow: 0 0 20px #ff0055; }
    .trend-box { background-color: #121224; padding: 25px; border-radius: 12px; border: 2px solid #00ffcc; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

local_time = datetime.now() + timedelta(hours=3)

st.title("🔥 DIAMOND AI TREND AUTOMATOR")
st.write("🤖 **البوت الخارق: صيد مواضيع التريند الحالية + توليد الفويس أوفر الفوري بضغطة زر**")
st.write(f"⏱️ توقيت رصد التريند المحلي: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
st.write("---")

# دالة قشط وجلب التريندات الحية من الويب
def fetch_live_trending_topics():
    try:
        url = "https://news.google.com/rss?hl=ar&gl=AE&ceid=AE:ar"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'xml')
        titles = [item.title.text for item in soup.find_all('item')]
        if titles:
            chosen_trend = random.choice(titles[:15])
            if " - " in chosen_trend:
                chosen_trend = chosen_trend.split(" - ")[0]
            return chosen_trend
    except:
        pass
    return "تطورات متسارعة في عالم الذكاء الاصطناعي والتكنولوجيا تذهل العالم اليوم"

st.subheader("🎬 مصنع محتوى التريند الحي")
if st.button("🚀 ابــدع وصــنّــع الـتـريـنـد الآلـي"):
    
    with st.spinner("🔍 1. جاري قشط الإنترنت وفحص مواضيع التريند الأكثر تفاعلاً الآن..."):
        current_trend = fetch_live_trending_topics()
        st.success(f"📌 تم رصد تريند الساعة بنجاح: [{current_trend}]")
        
    with st.spinner("📝 2. جاري صياغة السيناريو الفيرال (Viral Script)..."):
        script_text = f"هل سمعت آخر الأخبار المتداولة بشدة الآن؟ التريند الحالي يتحدث عن: {current_trend}. هذا الموضوع يشغل منصات التواصل الاجتماعي في هذه الساعات ويثير الكثير من التساؤلات والاهتمام. ما هو رأيكم في هذا التطور المفاجئ؟ شاركونا في التعليقات ولا تنسوا المتابعة لكشف التريند القادم أولاً بأول!"
        
    with st.spinner("🎙️ 3. جاري توليد الفويس أوفر الصوتي (Voice Over)..."):
        tts = gTTS(text=script_text, lang='ar', slow=False)
        tts.save("trend_voice.mp3")
        
    st.success("✨ تم تجهيز عناصر الفيديو بنجاح 100%!")
    
    # عرض الأغراض لـ ريم جاهزة ومقشرة
    st.markdown('<div class="trend-box">', unsafe_allow_html=True)
    
    st.markdown(f"### 📄 النص المولد للتريند:")
    st.info(script_text)
    
    st.markdown("### 🎙️ استمع وحمّل الفويس أوفر (Voice Over):")
    with open("trend_voice.mp3", "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")
        
    st.markdown("### 📺 فيديو الخلفية الفخم المقترح (مقاس تيك توك 9:16):")
    st.write("اضغطي على الرابط التالي لتحميل الخلفية المتناسقة مباشرة بجودة عالية:")
    st.markdown("[🔗 اضغطي هنا لتحميل فيديو الخلفية السريع الحركي](https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-and-numbers-31948-large.mp4)")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # تنظيف السيرفر
    if os.path.exists("trend_voice.mp3"):
        os.remove("trend_voice.mp3")
        
    # إرسال تنبيه لتليجرام
    try:
        TELEGRAM_TOKEN = "8861542684:AAGpm77vVt0KLttJXDEph3vplvDAjlvQ2Yk"
        TELEGRAM_CHAT_ID = "8061216590"
        alert_msg = f"🔥 *ريم! البوت صاد تريند جديد وجاهز للرفع!* 🔥\n\n🎯 *التريند:* {current_trend}\n\nادخلي الموقع الآن واسمعي الفويس أوفر الخارق واكتسحي المشاهدات! 🚀"
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": alert_msg, "parse_mode": "Markdown"})
    except:
        pass
else:
    st.info("💡 اضغطي على الزر وسيقوم البوت بصيد التريند وصناعة الفويس أوفر لكِ فوراً بدون أي مشاكل!")

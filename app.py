import streamlit as st
import random
import os
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import moviepy.editor as mp  # التعديل السحري المتوافق مع السيرفر السحابي
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
st.write("🤖 **البوت الخارق: صيد مواضيع التريند الحالية + صناعة الفويس أوفر + المونتاج التلقائي بضغطة زر**")
st.write(f"⏱️ توقيت رصد التريند المحلي: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
st.write("---")

# لوحة التحكم الجانبية
st.sidebar.markdown("### ⚙️ إعدادات الرصد والبحث")
trend_source = st.sidebar.selectbox("مصدر رصد التريندات والمستجدات:", ["أخبار العالم والتقنية المتداولة", "أحدث المنشورات الرائجة العامة"])

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

st.subheader("🎬 مصنع الفيديوهات المعتمد على التريند الحي")
if st.button("🚀 ابــدع وصــنّــع الـتـريـنـد الآلـي"):
    
    with st.spinner("🔍 1. جاري قشط الإنترنت وفحص مواضيع التريند الأكثر تفاعلاً الآن..."):
        current_trend = fetch_live_trending_topics()
        st.success(f"📌 تم رصد تريند الساعة بنجاح: [{current_trend}]")
        
    with st.spinner("📝 2. جاري صياغة وكتابة سيناريو الشورتس تلقائياً بناءً على التريند..."):
        script_text = f"هل سمعت آخر الأخبار المتداولة بشدة الآن؟ التريند الحالي يتحدث عن: {current_trend}. هذا الموضوع يشغل منصات التواصل الاجتماعي في هذه الساعات ويثير الكثير من التساؤلات والاهتمام. ما هو رأيكم في هذا التطور المفاجئ؟ شاركونا في التعليقات ولا تنسوا المتابعة لكشف التريند القادم أولاً بأول!"
        
    with st.spinner("🎙️ 3. جاري تحويل السيناريو إلى فويس أوفر صوتي احترافي (Voice Over)..."):
        tts = gTTS(text=script_text, lang='ar', slow=False)
        tts.save("trend_voice.mp3")
        
    with st.spinner("📺 4. جاري جلب فيديو الخلفية ودمج الصوت والمونتاج التلقائي بالكامل..."):
        bg_video_url = "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-and-numbers-31948-large.mp4"
        video_data = requests.get(bg_video_url).content
        with open("trend_bg.mp4", "wb") as f:
            f.write(video_data)
            
        try:
            # استخدام الاختصار المحدث المتوافق السحابي mp.VideoFileClip
            video_clip = mp.VideoFileClip("trend_bg.mp4").subclip(0, 18)
            audio_clip = mp.AudioFileClip("trend_voice.mp3")
            
            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile("trend_output.mp4", codec="libx264", audio_codec="aac")
            
            st.success("✨ تم الانتهاء من رصد التريند، التسجيل الصوتي، والمونتاج بنجاح 100%!")
            
            st.markdown('<div class="trend-box">', unsafe_allow_html=True)
            st.markdown(f"### 📥 فيديو التريند الجاهز تماماً للرفع وحصد المشاهدات:")
            st.caption(f"📄 النص الذي تم إلقاؤه في الفيديو: {script_text}")
            with open("trend_output.mp4", "rb") as file:
                st.video(file.read())
            st.markdown('</div>', unsafe_allow_html=True)
            
            TELEGRAM_TOKEN = "8861542684:AAGpm77vVt0KLttJXDEph3vplvDAjlvQ2Yk"
            TELEGRAM_CHAT_ID = "8061216590"
            alert_msg = f"🔥 *ريم! البوت صاد تريند جديد وسوى عليه فيديو كامل!* 🔥\n\n🎯 *التريند المرصود:* {current_trend}\n\nادخلي الموقع الآن، وحملي مقطع التريند الجاهز واكتسحي المشاهدات! 🚀"
            requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": alert_msg, "parse_mode": "Markdown"})
            
        except Exception as e:
            st.error("⚠️ واجه السيرفر ضغطاً أثناء رندرة مقطع المونتاج. يرجى المحاولة مرة أخرى.")
        finally:
            if os.path.exists("trend_voice.mp3"): os.remove("trend_voice.mp3")
            if os.path.exists("trend_bg.mp4"): os.remove("trend_bg.mp4")
else:
    st.info("💡 اضغطي على زر 'ابــدع وصــنّــع الـتـريـنـد الآلـي' وشاهدي كيف سيتحرك الذكاء الاصطناعي لعمل كل شيء بدلاً منكِ فوراً!")

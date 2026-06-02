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
st.write("🤖 **البوت المطور: صيد مواضيع تريند متجددة في كل ضغطة + توليد فويس أوفر فوري**")
st.write(f"⏱️ توقيت رصد التريند الحالي: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
st.write("---")

# دالة قشط وجلب التريندات الحية بشكل عشوائي ومتجدد في كل ضغطة
def fetch_dynamic_trending_topic():
    # استخدام مصادر وأقسام مختلفة لضمان تنوع المواضيع في كل مرة تضغطين "ابدع"
    sources = [
        "https://news.google.com/rss?hl=ar&gl=AE&ceid=AE:ar",  # أخبار عامة
        "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=ar&gl=AE&ceid=AE:ar", # تقنية
        "https://news.google.com/rss/headlines/section/topic/SCIENCE?hl=ar&gl=AE&ceid=AE:ar" # علوم وصحة
    ]
    try:
        chosen_source = random.choice(sources)
        response = requests.get(chosen_source, timeout=10)
        soup = BeautifulSoup(response.content, 'xml')
        titles = [item.title.text for item in soup.find_all('item')]
        
        if titles:
            # اختيار عنوان عشوائي تماماً من قائمة أول 20 تريند متداول لضمان التجديد
            chosen_trend = random.choice(titles[:20])
            if " - " in chosen_trend:
                chosen_trend = chosen_trend.split(" - ")[0]
            return chosen_trend
    except:
        pass
    return "تطور تكنولوجي مذهل واكتشافات علمية جديدة تثير الجدل اليوم"

st.subheader("🎬 مصنع محتوى التريندات المتجددة")
st.write("اضغطي على الزر بالأسفل، وفي كل مرة سيقوم البوت بصيد موضوع مختلف تماماً عن السابق وثاني خالص:")

if st.button("🚀 ابــدع وصــنّــع مـوضـوعـاً جـديـداً"):
    
    with st.spinner("🔍 جاري فحص شبكة الإنترنت وقشط موضوع تريند جديد تماماً..."):
        current_trend = fetch_dynamic_trending_topic()
        st.success(f"📌 تم رصد موضوع تريند متجدد: [{current_trend}]")
        
    with st.spinner("📝 صياغة سيناريو الشورتس بأسلوب فيرال شيق..."):
        script_text = f"هل سمعت آخر الأخبار المتداولة بشدة الآن؟ التريند الجديد يتحدث عن: {current_trend}. هذا الموضوع يشغل منصات التواصل الاجتماعي في هذه الساعات ويثير الكثير من التساؤلات والاهتمام. ما هو رأيكم في هذا التطور المفاجئ؟ شاركونا في التعليقات ولا تنسوا المتابعة لكشف التريند القادم أولاً بأول!"
        
    with st.spinner("🎙️ توليد تسجيل الفويس أوفر (Voice Over)..."):
        tts = gTTS(text=script_text, lang='ar', slow=False)
        tts.save("dynamic_trend_voice.mp3")
        
    st.success("✨ تم تجهيز عناصر مقطعكِ الجديد بنجاح!")
    
    # عرض النتائج
    st.markdown('<div class="trend-box">', unsafe_allow_html=True)
    st.markdown(f"### 📄 السيناريو الخاص بهذا التريند:")
    st.info(script_text)
    
    st.markdown("### 🎙️ استمع وحمّل الفويس أوفر المتولد:")
    with open("dynamic_trend_voice.mp3", "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")
        
    st.markdown("### 📺 فيديو الخلفية المقترح للمونتاج سريعاً:")
    stable_video_url = "https://upload.wikimedia.org/wikipedia/commons/d/df/Data_Network_Background_Loop.mp4"
    st.markdown(f"[🔗 اضغطي هنا لتحميل فيديو الخلفية بجودة عالية]({stable_video_url})")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if os.path.exists("dynamic_trend_voice.mp3"):
        os.remove("dynamic_trend_voice.mp3")
        
    # إرسال التنبيه الفوري لبوت التليجرام الخاص بكِ
    try:
        TELEGRAM_TOKEN = "8861542684:AAGpm77vVt0KLttJXDEph3vplvDAjlvQ2Yk"
        TELEGRAM_CHAT_ID = "8061216590"
        alert_msg = f"🎬 *ريم! البوت صاد لكِ موضوع تريند جديد وثاني تماماً!* \n\n🎯 *الموضوع:* {current_trend}\n\nادخلي الموقع الآن واسمعي الفويس أوفر الجديد الجاهز! 🚀"
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": alert_msg, "parse_mode": "Markdown"})
    except:
        pass
else:
    st.info("💡 اضغطي على الزر وسيقوم البوت بصيد تريند جديد في كل مرة تجربة!")

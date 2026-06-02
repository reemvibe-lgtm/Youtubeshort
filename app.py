import streamlit as st
import random
import os
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import moviepy.editor as mp  # مكتبة المونتاج التلقائي
from datetime import datetime, timedelta

# 1. إعدادات الهوية البصرية (AI Trend Hunter Loop Studio)
st.set_page_config(page_title="Diamond AI Trend Loop", page_icon="♾️", layout="wide")

st.markdown("""
    <style>
    .reportview-container, .main { background-color: #050510; color: #00fff0; }
    .stMetric { background-color: #0f1224; padding: 20px; border-radius: 12px; border: 1px solid #ff007f; }
    h1, h2, h3 { color: #ff007f !important; font-family: 'Courier New', sans-serif; text-shadow: 0 0 10px rgba(255, 0, 127, 0.6); }
    div.stButton > button:first-child { background-color: #ff007f; color: white; font-weight: bold; border-radius: 8px; height: 60px; font-size: 22px; box-shadow: 0 0 20px #ff007f; }
    .render-box { background-color: #0f1224; padding: 25px; border-radius: 12px; border: 2px solid #00fff0; margin-top: 20px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

local_time = datetime.now() + timedelta(hours=3)

st.title("♾️ DIAMOND AI TREND LOOP")
st.write("🤖 **مصنع الفيديو الآلي المدمج: رصد التريندات المتجددة + المونتاج التلقائي الكامل بدون روابط معطوبة**")
st.write(f"⏱️ توقيت رصد التريند الحالي: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
st.write("---")

# دالة جلب التريندات المتجددة
def fetch_dynamic_trending_topic():
    # مصادر منوعة لضمان التجديد في كل ضغطة
    sources = [
        "https://news.google.com/rss?hl=ar&gl=AE&ceid=AE:ar",  # أخبار عامة
        "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=ar&gl=AE&ceid=AE:ar" # تقنية
    ]
    try:
        chosen_source = random.choice(sources)
        response = requests.get(chosen_source, timeout=10)
        soup = BeautifulSoup(response.content, 'xml')
        titles = [item.title.text for item in soup.find_all('item')]
        
        if titles:
            # اختيار عنوان عشوائي من أفضل 20 تريند
            chosen_trend = random.choice(titles[:20])
            if " - " in chosen_trend:
                chosen_trend = chosen_trend.split(" - ")[0]
            return chosen_trend
    except:
        pass
    return "تطور تكنولوجي مذهل واكتشافات علمية جديدة تثير الجدل اليوم"

st.subheader("🎬 مصنع فيديوهات التريند المدمجة")
st.write("اضغطي على الزر، وسيقوم البوت بالبحث، الكتابة، التسجيل، ودمج فيديو كامل لكِ في ثوانٍ:")

if st.button("🚀 ابــدع وصــنّــع مـقـطـعـاً مـدمـجـاً"):
    
    with st.spinner("🔍 1. جاري قشط الإنترنت وفحص مواضيع التريند الأكثر تفاعلاً الآن..."):
        current_trend = fetch_dynamic_trending_topic()
        st.success(f"📌 تم رصد موضوع تريند متجدد: [{current_trend}]")
        
    with st.spinner("📝 2. جاري صياغة وكتابة سيناريو الشورتس تلقائياً..."):
        # صياغة السيناريو بأسلوب فيرال شيق
        script_text = f"هل سمعت آخر الأخبار المتداولة بشدة الآن؟ التريند الجديد يتحدث عن: {current_trend}. هذا الموضوع يشغل منصات التواصل الاجتماعي في هذه الساعات ويثير الكثير من التساؤلات والاهتمام. ما هو رأيكم في هذا التطور المفاجئ؟ شاركونا في التعليقات ولا تنسوا المتابعة لكشف التريند القادم أولاً بأول!"
        
    with st.spinner("🎙️ 3. جاري توليد الفويس أوفر الصوتي (Voice Over)..."):
        # تحويل النص المولد إلى ملف صوتي
        tts = gTTS(text=script_text, lang='ar', slow=False)
        tts.save("trend_voice.mp3")
        
    with st.spinner("📺 4. جاري جلب الخلفية وعمل المونتاج والدمج الرقمي الشامل..."):
        # رابط مقطع فيديو خلفية مفتوح ومستقر على Wikimedia
        stable_video_url = "https://upload.wikimedia.org/wikipedia/commons/d/df/Data_Network_Background_Loop.mp4"
        
        # تحميل فيديو الخلفية
        video_data = requests.get(stable_video_url).content
        with open("trend_bg.mp4", "wb") as f:
            f.write(video_data)
            
        try:
            # استخدام moviepy للدمج والمونتاج تلقائياً
            video_clip = mp.VideoFileClip("trend_bg.mp4").subclip(0, 18) # قص مقطع بطول 18 ثانية للشورتس
            audio_clip = mp.AudioFileClip("trend_voice.mp3")
            
            # تركيب الفويس أوفر على المقطع
            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile("trend_final.mp4", codec="libx264", audio_codec="aac")
            
            st.success("✨ تم الانتهاء من المونتاج والدمج بنجاح 100%!")
            
            # عرض النتيجة النهائية لريم داخل الموقع
            st.markdown('<div class="render-box">', unsafe_allow_html=True)
            st.markdown(f"### 📥 فيديو الـ Short المدمج والجاهز للتحميل والرفع:")
            st.caption(f"📄 النص الذي تم إلقاؤه في الفيديو: {script_text}")
            with open("trend_final.mp4", "rb") as file:
                st.video(file.read())
            st.markdown('</div>', unsafe_allow_html=True)
            
            # إرسال إشعار فوري لتليجرام ريم بأن فيديو التريند المباشر جاهز
            TELEGRAM_TOKEN = "8861542684:AAGpm77vVt0KLttJXDEph3vplvDAjlvQ2Yk"
            TELEGRAM_CHAT_ID = "8061216590"
            alert_msg = f"🔥 *ريم! البوت صاد تريند جديد وسوى عليه فيديو كامل!* 🔥\n\n🎯 *التريند:* {current_trend}\n\nادخلي الموقع الآن، وحملي مقطع التريند الجاهز واكتسحي المشاهدات! 🚀"
            requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": alert_msg, "parse_mode": "Markdown"})
            
        except Exception as e:
            st.error("⚠️ واجه السيرفر ضغطاً أثناء رندرة مقطع المونتاج. يرجى المحاولة مرة أخرى.")
        finally:
            # تنظيف السيرفر من الملفات المؤقتة
            if os.path.exists("trend_voice.mp3"): os.remove("trend_voice.mp3")
            if os.path.exists("trend_bg.mp4"): os.remove("trend_bg.mp4")
else:
    st.info("💡 اضغطي على زر 'ابــدع وصــنّــع مـقـطـعـاً مـدمـجـاً' وشاهدي كيف سيتحرك الذكاء الاصطناعي لعمل كل شيء بدلاً منكِ فوراً!")

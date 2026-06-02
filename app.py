import streamlit as st
import random
from gtts import gTTS
import os

# إعدادات الواجهة
st.set_page_config(page_title="Diamond AI Trend", layout="wide")

# خلفية رقمية مدمجة (لا تحتاج روابط)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
    .content { background: rgba(0,0,0,0.6); padding: 30px; border-radius: 20px; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 DIAMOND AI TREND")

if st.button("🚀 ابدأ صيد التريند الجدلي"):
    # مواضيع مثيرة للجدل
    topics = ["غموض حادثة غامضة", "أسرار خلف قضية قضائية", "حقائق صادمة عن تريند اليوم"]
    trend = random.choice(topics)
    
    # توليد نص
    text = f"تخيلوا أن هذه القضية لا تزال تثير الجدل! نتحدث عن {trend}. شاركوني رأيكم!"
    tts = gTTS(text=text, lang='ar', slow=False)
    tts.save("audio.mp3")
    
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.write(f"### 📌 القضية: {trend}")
    with open("audio.mp3", "rb") as f:
        st.audio(f.read(), format="audio/mp3")
    st.write("✅ **جاهز!** قومي بتسجيل الشاشة الآن لتصوير الخلفية المتحركة خلف النص واستخدميها في مونتاجكِ.")
    st.markdown('</div>', unsafe_allow_html=True)

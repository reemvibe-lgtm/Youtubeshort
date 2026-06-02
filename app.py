import streamlit as st
import random
from gtts import gTTS

# إعدادات الواجهة (خلفية سوداء غامضة تليق بمواضيع الإثارة)
st.set_page_config(page_title="Dark Trend Hunter", page_icon="🕵️‍♀️", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #050505; color: #ff0033; }
    .content-box { background: rgba(20, 0, 0, 0.8); padding: 25px; border-radius: 15px; border: 1px solid #ff0033; }
    h1 { color: #ff0033 !important; text-shadow: 0 0 15px #ff0033; }
    div.stButton > button { background: #ff0033; color: white; font-weight: bold; height: 60px; font-size: 20px; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🕵️‍♀️ DARK TREND HUNTER (صائد القضايا الشائكة)")

def fetch_edgy_trend():
    # محرك بحث يركز على العناوين المثيرة
    edgy_topics = [
        "غموض اختفاء غامض يثير حيرة المحققين",
        "تفاصيل قضية هزت الرأي العام مؤخراً",
        "حقائق مرعبة خلف جريمة تصدرت التريند",
        "قصة حقيقية لم تسمعها من قبل عن...",
        "لماذا يصر الناس على الحديث عن هذه القضية؟"
    ]
    return random.choice(edgy_topics)

if st.button("🚀 أكشفي القضية المثيرة للجدل"):
    trend = fetch_edgy_trend()
    
    # صياغة سكربت يثير الفضول
    script = f"تخيلوا أن هذه القضية لا تزال تثير الرعب والجدل حتى هذه اللحظة! نتحدث عن {trend}. الجميع يحلل، والجميع يتساءل، ولكن الحقيقة قد تكون أكثر صدمة مما تتخيلون. هل تعتقدون أن العدالة ستأخذ مجراها في هذه القصة؟ شاركوني رأيكم.. فالغموض هنا لا ينتهي!"
    
    # توليد صوت
    tts = gTTS(text=script, lang='ar', slow=False)
    tts.save("edgy_voice.mp3")
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.info(f"📌 عنوان المقطع: {trend}")
    st.write("🎙️ الصوت جاهز للتحميل:")
    with open("edgy_voice.mp3", "rb") as f:
        st.audio(f.read(), format="audio/mp3")
    st.warning("⚠️ ملاحظة: هذا المحتوى مصمم لجذب الفضول، استخدميه بذكاء لزيادة التفاعل!")
    st.

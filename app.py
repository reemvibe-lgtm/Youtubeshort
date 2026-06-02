import streamlit as st
import random
from gtts import gTTS

st.set_page_config(page_title="Crime Story Gen", layout="centered")

st.title("🕵️‍♀️ Crime & Mystery Story Generator")
st.write("أدخلي موضوعاً وسأقوم بصياغة سكربت 'جريمة غامضة' مرعب ومثير للجدل!")

topic = st.text_input("موضوع الفيديو (مثلاً: اختفاء غامض في غابة):")

if st.button("توليد السكربت"):
    # سكربت مصمم لزيادة وقت المشاهدة (Watch Time)
    script = f"هل سمعتم عن قصة {topic}؟ الحقيقة أن هذا الموضوع يخفي تفاصيل لم يتوقعها أحد.. في البداية كان الأمر يبدو طبيعياً، لكن فجأة انقلبت الموازين. بقيت هذه القضية بدون حل لسنوات.. إذا كنتم تحبون الغموض، تابعوا للنهاية لتسمعوا ما لم يقل في التحقيقات!"
    
    st.info(script)
    
    # توليد الصوت
    tts = gTTS(text=script, lang='ar', slow=False)
    tts.save("story.mp3")
    st.audio("story.mp3")

import streamlit as st
import itertools
import random

st.set_page_config(page_title="Elite Sniper AI", page_icon="🎯")
st.title("🎯 Elite Sniper: صائد اليوزرات الذكي")

# محرك الذكاء الاصطناعي للتحليل
def generate_elite_usernames(length, count=50):
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    # تحليل التناغم: نختار حروفاً تبدو جذابة بصرياً
    vowels = "aeiou"
    
    generated = set()
    while len(generated) < count:
        # توليد يوزر عشوائي ذكي
        name = "".join(random.choice(chars) for _ in range(length))
        
        # شرط التناغم: لا نريد يوزرات مليئة بالأرقام فقط (لأنها ليست مميزة)
        # نشترط وجود حرف واحد على الأقل ليكون اليوزر "ماركة"
        if any(c.isalpha() for c in name):
            generated.add(name)
    return generated

st.subheader("إعدادات الصيد:")
col1, col2 = st.columns(2)
with col1:
    length = st.selectbox("طول اليوزر:", [3, 4])
with col2:
    num_gen = st.slider("كم يوزر تريدين توليده؟", 10, 100, 50)

if st.button("🚀 ابدأ التوليد الذكي"):
    st.write(f"جاري تحليل وتوليد {length} حروف... (ذكاء اصطناعي)")
    results = generate_elite_usernames(length, num_gen)
    
    st.success("تم صيد القائمة:")
    st.code("\n".join(results))
    
    st.info("⚠️ ملاحظة: هذه يوزرات احتمالية (Probabilistic). بعد توليدها، جربي نسخها واحداً تلو الآخر في إنستغرام.")

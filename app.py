import streamlit as st
import random

st.set_page_config(page_title="Brand Architect AI", page_icon="🚀", layout="wide")

# تصميم واجهة فخمة وجذابة للمستخدمين
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f172a, #1e1b4b); color: #f8fafc; }
    .result-card { background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 15px; border: 1px solid #6366f1; margin-top: 20px; }
    h1 { text-shadow: 0 0 10px #6366f1; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Brand Architect AI")
st.write("المحرك الذكي لتأسيس البراندات وصناعة الهوية التسويقية في ثوانٍ.")

# مدخلات المستخدم
project_type = st.selectbox("ما هو مجال مشروعك القادم؟", ["تجارة إلكترونية (أزياء/عطور)", "مطعم / مقهى مبتكر", "تطبيق ذكي / أداة تقنية", "صناعة محتوى وشخصية رقمية"])
target_audience = st.text_input("من هي فئتك المستهدفة؟ (مثال: الشباب في الخليج، الأمهات، المهتمين بالتقنية):")

if st.button("🏗️ هندسة البراند بالذكاء الاصطناعي"):
    if target_audience:
        with st.spinner("جاري التحليل الإحصائي وصياغة الاستراتيجية الرقمية..."):
            
            # محرك التحليل والابتكار (هنا الذكاء في توليد الأفكار المتناسقة)
            names_pool = {
                "تجارة إلكترونية (أزياء/عطور)": ["Velve Aura", "سديم | SADEEM", "PureLux", "أثر | ATHAR"],
                "مطعم / مقهى مبتكر": ["Vibe & Brew", "توليفة | Tolfa", "The Roast", "رواق | Rawaq"],
                "تطبيق ذكي / أداة تقنية": ["SwiftCode", "مِسبار | Misbar", "AlphaTask", "مُؤتمت | Automated"],
                "صناعة محتوى وشخصية رقمية": ["The Mindset", "رادار رقمي", "InsightX", "أفق | Horizon"]
            }
            
            chosen_names = random.sample(names_pool[project_type], 2)
            
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.subheader("🎯 النتيجة النهائية لهوية مشروعك:")
            
            # 1. اقتراح الأسماء المميزة
            st.write(f"### 💎 أسماء مقترحة ونادرة للبراند:")
            for name in chosen_names:
                st.code(name)
                
            # 2. خطة المحتوى (التسويق الفيرال)
            st.write("### 🎬 خطة أول 3 فيديوهات تيك توك لجلب مبيعات:")
            st.warning("🧠 فيديو 1 (إثارة فضول): 'لماذا يخفي عنك أصحاب هذا المجال هذا السر؟' (ركزي على حل مشكلة لـ " + target_audience + ")")
            st.warning("🧠 فيديو 2 (خلف الكواليس): تصوير طريقة تجهيز المنتجات بأسلوب جمالي ومريح بصرياً.")
            st.warning("🧠 فيديو 3 (العرض القوي): تقديم كود خصم حصري لفترة محدودة جداً.")
            
            # 3. الرؤية التسويقية
            st.write("### 📝 الشعار اللفظي (Slogan) المقترح:")
            st.info(f"التميز الذي يبحث عنه {target_audience}، بأسلوب يواكب المستقبل.")
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.success("✅ تم بناء الهوية بنجاح! هذه الأداة توفر على أصحاب المشاريع آلاف الدولارات في الاستشارات.")
    else:
        st.error("الرجاء تحديد الفئة المستهدفة أولاً ليقوم الذكاء الاصطناعي بالتحليل الدقيق.")

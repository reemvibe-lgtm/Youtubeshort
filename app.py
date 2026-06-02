import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Alpha Project AI", page_icon="🧠", layout="wide")

# إعداد الواجهة الاحترافية
st.markdown("""
    <style>
    .stApp { background: #0b0f19; color: #e2e8f0; }
    .content-box { background: rgba(255, 255, 255, 0.03); padding: 25px; border-radius: 15px; border: 1px solid #3b82f6; margin-top: 20px; }
    h1 { color: #3b82f6 !important; text-shadow: 0 0 15px rgba(59, 130, 246, 0.5); }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Alpha Project AI: المحلل الاستراتيجي الذكي")
st.write("أدخل فكرة مشروعك، ودع الذكاء الاصطناعي الحقيقي يحللها ويهندس لك خطة النجاح الفورية.")

# قائمة جانبية لإدخال المفتاح بخصوصية
st.sidebar.header("🔑 إعدادات الاتصال")
api_key = st.sidebar.text_input("أدخلي مفتاح Gemini API الخاص بكِ:", type="password")

user_idea = st.text_area("اشرح فكرة مشروعك أو متجرك بالتفصيل (كلما كتبت تفاصيل أكثر، كانت النتيجة أذكى):", height=150)

if st.button("🚀 ابدأ التحليل العميّق"):
    if not api_key:
        st.error("❌ خطأ: الرجاء إدخال الـ API Key في القائمة الجانبية لتفعيل عقل الموقع.")
    elif not user_idea:
        st.error("❌ خطأ: الرجاء كتابة فكرة المشروع أولاً ليقوم البوت بتحليلها!")
    else:
        with st.spinner("🧠 جاري إرسال البيانات إلى محرك الذكاء الاصطناعي وتحليلها..."):
            try:
                # تهيئة الاتصال
                genai.configure(api_key=api_key)
                
                # استخدام النموذج المستقر والسريع
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # صياغة الأمر الاحترافي (Prompt)
                prompt = f"""
                أنت مستشار أعمال خبير ومسوق رقمي محترف. 
                حلل فكرة المشروع التالية تحليلًا دقيقًا وعميقًا:
                "{user_idea}"
                
                أعطني خطة عمل متكاملة تحتوي على:
                1) تقييم حقيقي وصريح لجدوى الفكرة (نقاط القوة، العقبات المتوقعة وكيفية تجنبها).
                2) ميزة تنافسية خارقة تجعل هذا المشروع يتفوق على السوق فورًا.
                3) استراتيجية تسويق (Viral) على تيك توك: تشمل فكرة فيديو مبتكرة مع السكربت الحواري الكامل المكتوب باللهجة المحلية المناسبة للمشروع لجذب العملاء بدون دفع ريال واحد في الإعلانات.
                
                اجعل الأسلوب عمليًا، منظمًا، ومليئًا بالأسرار التجارية المفيدة باللغة العربية.
                """
                
                response = model.generate_content(prompt)
                
                # عرض النتيجة داخل تصميم فخم
                st.markdown('<div class="content-box">', unsafe_allow_html=True)
                st.subheader("🎯 الاستراتيجية الحصريّة لمشروعك:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
                st.success("✅ تم التحليل وصناعة الاستراتيجية بنجاح!")
                
            except Exception as e:
                st.error(f"⚠️ حدث خطأ في الاتصال: {e}")
                st.info("تأكدي من أن الـ API Key صحيح ومفعل من Google AI Studio.")

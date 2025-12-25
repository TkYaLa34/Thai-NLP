import streamlit as st
import openai

# การตั้งค่าหน้าจอ
st.set_page_config(page_title="Thai Code Prompt AI", layout="wide")

st.title("🇹🇭 Thai NLP to AI Coding Prompt")
st.subheader("แปลงภาษาไทยเป็น Prompt เขียนโค้ดระดับโปร")

# ดึง API Key จาก Secret ของ Streamlit
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("กรุณาตั้งค่า API Key ใน Streamlit Cloud Secrets")

# ส่วนรับข้อมูล
user_input = st.text_area("อธิบายสิ่งที่อยากให้ AI เขียนโค้ด (ภาษาไทย):", placeholder="เช่น: สร้างหน้าเว็บขายของหน้าแรกด้วย HTML/CSS แบบ Responsive")
tech_stack = st.text_input("Tech Stack ที่ต้องการ:", "React, Tailwind CSS")

if st.button("สร้าง Prompt"):
    if user_input:
        with st.spinner("กำลังประมวลผล..."):
            prompt = f"Act as a Senior Developer. Translate this Thai requirement into a detailed, technical English prompt for coding: {user_input}. Specific technologies: {tech_stack}. Format the output with clear sections: Role, Goal, Technical Steps, and Constraints."
            
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            st.code(result, language="markdown")
    else:
        st.warning("กรุณากรอกความต้องการก่อนครับ")

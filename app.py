import streamlit as st
import openai

# Configuration
st.set_page_config(page_title="Thai Code Prompt AI", layout="wide")

st.title("🇹🇭 Thai NLP to AI Coding Prompt")
st.subheader("Convert Thai requirements to Professional English Prompts")

# Load API Key from Streamlit Secrets
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("Please configure API Key in Streamlit Cloud Secrets")

# Input Section
user_input = st.text_area("Describe your requirement (Thai):", placeholder="เช่น: สร้างหน้าเว็บ Landing Page ด้วย HTML/CSS")
tech_stack = st.text_input("Preferred Tech Stack:", "React, Tailwind CSS")

if st.button("Generate Prompt"):
    if user_input:
        with st.spinner("Processing..."):
            # Meta-Prompt for the AI
            sys_message = "You are a Senior Software Architect. Translate the user's Thai requirement into a highly detailed, professional English prompt for AI coding assistants."
            user_message = f"Requirement: {user_input}\nTech Stack: {tech_stack}"
            
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": sys_message},
                        {"role": "user", "content": user_message}
                    ]
                )
                result = response.choices[0].message.content
                st.code(result, language="markdown")
                st.success("Prompt Generated! Copy this to your AI Code Editor.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter your requirement first.")

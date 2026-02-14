import streamlit as st
import os
from langchain_openai import ChatOpenAI

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Content Humanizer", layout="wide")
st.title("✍️ AI Content Humanizer")

st.write("Paste AI-generated text below and convert it into more natural, human-like writing.")

# ---------------- OPENAI KEY ----------------
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# ---------------- MODEL ----------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# ---------------- INPUT AREA ----------------
input_text = st.text_area(
    "Paste AI-generated content here:",
    height=250
)

# ---------------- OPTIONS ----------------
tone = st.selectbox(
    "Choose Tone:",
    ["Natural", "Professional", "Conversational", "Friendly", "Persuasive"]
)

rewrite_strength = st.slider(
    "Rewrite Strength",
    min_value=1,
    max_value=10,
    value=6,
    help="Higher value = more aggressive rewriting"
)

# ---------------- HUMANIZE BUTTON ----------------
if st.button("✨ Humanize Content"):

    if not input_text.strip():
        st.warning("Please paste some text first.")
    else:
        with st.spinner("Humanizing content..."):

            prompt = f"""
You are an expert editor.

Rewrite the following AI-generated text to sound more human, natural, and engaging.

Guidelines:
- Tone: {tone}
- Rewrite strength: {rewrite_strength}/10
- Avoid robotic phrasing
- Add natural sentence variation
- Keep original meaning intact
- Do not add new facts

Text:
{input_text}
"""

            response = llm.invoke(prompt)

            st.markdown("---")
            st.subheader("✅ Humanized Version")

            st.write(response.content)

            st.markdown("---")
            st.subheader("📊 Side-by-Side Comparison")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Original")
                st.write(input_text)

            with col2:
                st.markdown("### Humanized")
                st.write(response.content)

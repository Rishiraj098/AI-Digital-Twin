import os, sys
import streamlit as st

# Fix root path
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_PATH)

from ChatBot.consultant_bot import business_chat
from utils.style_loader import load_css

load_css()

st.title("🧠 AI Strategy Consultant")

st.markdown("""
Ask business questions like:

• Should we increase marketing?
• Is hiring more employees risky?
• How to maximize growth?
""")

# Input Sliders (Business Context)
marketing = st.slider("Marketing Spend", 5000, 100000, 30000)
employees = st.slider("Employees", 5, 100, 20)
time = st.slider("Days", 1, 365, 30)

# User Question
user_query = st.text_area("Ask AI Business Advisor")

# AI Button
if st.button("Ask AI"):

    response = business_chat(
        query=user_query,
        marketing=marketing,
        employees=employees,
        time=time
    )

    st.subheader("📊 AI Explanation")
    st.write(response["AI Explanation"])

    st.subheader("🎯 Strategic Advice")
    for adv in response["Strategic Advice"]:
        st.write("✔", adv)
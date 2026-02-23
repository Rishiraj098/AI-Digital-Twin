import sys
import os

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_PATH)

import streamlit as st
from ChatBot.consultant_bot import business_chat
from utils.style_loader import load_css

st.title("Business Simulator")

marketing = st.slider("Marketing Spend", 5000,100000,30000)
employees = st.slider("Employees",5,100,20)
time = st.slider("Days",1,365,30)

if st.button("Run Simulation"):
    result = business_chat(marketing,employees,time)

    st.metric("Predicted Sales",result["Predicted Sales"])
    st.metric("Risk Level",result["Risk Level"])

    st.subheader("AI Explanation")
    st.write(result["AI Explanation"])

    st.subheader("Strategic Advice")
    for adv in result["Strategic Advice"]:
        st.write("✔",adv)
        
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='glass-card'>
        <div class='kpi'>₹ 58,000</div>
        <div class='kpi-label'>Predicted Sales</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='glass-card'>
        <div class='kpi risk-medium'>Moderate</div>
        <div class='kpi-label'>Risk Level</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='glass-card'>
        <div class='kpi'>+12%</div>
        <div class='kpi-label'>Growth Potential</div>
    </div>
    """, unsafe_allow_html=True)
   
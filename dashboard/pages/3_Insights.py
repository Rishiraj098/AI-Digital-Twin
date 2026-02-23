import streamlit as st
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.style_loader import load_css
load_css()


st.title("Business Intelligence")

st.info("""
AI analyzes workforce, marketing and time
to determine growth, risks and optimization paths.
""")

st.markdown("""
<div class='glass-card'>
<h3>Executive Insight</h3>
<p>Increasing marketing improves short-term sales visibility.</p>
<p>Workforce alignment required for long-term growth.</p>
</div>
""", unsafe_allow_html=True)
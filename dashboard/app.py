import streamlit as st
from utils import style_loader
style_loader.load_css()

st.set_page_config(layout="wide")


st.markdown("<h1 class='hero-title'>AI Powered Digital Twin</h1>", unsafe_allow_html=True)
st.markdown("### Sales Decision Intelligence Platform")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='glass-card'>
        <h3>Predict Sales</h3>
        <p>Forecast before decision</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='glass-card'>
        <h3>Simulate Strategy</h3>
        <p>Test before implementation</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='glass-card'>
        <h3>Reduce Risk</h3>
        <p>AI driven planning</p>
    </div>
    """, unsafe_allow_html=True)
    
    risk = "Moderate"
if risk == "Low":
    st.progress(0.3)
elif risk == "Moderate":
    st.progress(0.6)
else:
    st.progress(0.9)
    
    growth = 0.72
    st.metric("Growth Score", f"{growth*100:.1f}%")
    st.progress(growth)
    
    st.markdown("""
<div class='glass-card'>
<h3>Executive Insight</h3>
<p>Increasing marketing improves short-term sales visibility.</p>
<p>Workforce alignment required for long-term growth.</p>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("""
<div class="scorecard-title">Executive Decision Scorecard</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

s1.metric("Projected Growth", "+18%")
s2.metric("Risk Level", "Moderate")
s3.metric("Confidence", "82%")
s4.metric("Strategic Impact", "High")
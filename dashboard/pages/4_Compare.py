import streamlit as st
import os, sys
from utils.charts import risk_gauge, growth_meter, scenario_bar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.style_loader import load_css
import random
load_css()

st.title("Scenario Comparison")

col1, col2 = st.columns(2)

with col1:
    m1 = st.number_input("Marketing A", 5000)
    e1 = st.number_input("Employees A", 10)
    t1 = st.number_input("Time A", 30)

with col2:
    m2 = st.number_input("Marketing B", 6000)
    e2 = st.number_input("Employees B", 20)
    t2 = st.number_input("Time B", 30)

if st.button("Compare"):
    st.markdown("## AI Decision Snapshot")

k1, k2, k3 = st.columns(3)

with k1:
    st.markdown('<div class="glass"><b>Predicted Sales</b><br>₹ 58,000</div>', unsafe_allow_html=True)

with k2:
    st.markdown('<div class="glass"><b>Risk Index</b><br>Moderate</div>', unsafe_allow_html=True)

with k3:
    st.markdown('<div class="glass"><b>Growth Outlook</b><br>Positive</div>', unsafe_allow_html=True)

sales_a = random.randint(40000,90000)
sales_b = random.randint(40000,90000)

risk = random.randint(20,80)
growth = random.randint(30,90)

st.markdown("### Executive Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.plotly_chart(risk_gauge(risk), use_container_width=True)

with col2:
    st.plotly_chart(growth_meter(growth), use_container_width=True)

with col3:
    st.plotly_chart(scenario_bar(sales_a, sales_b), use_container_width=True)
import sys
import os

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_PATH)

import streamlit as st
from engine.simulator import predict_sales
from utils.style_loader import load_css

st.title("Business Simulator")

marketing = st.slider("Marketing Spend", 5000,100000,30000)
employees = st.slider("Employees",5,100,20)
time = st.slider("Days",1,365,30)

if st.button("Run Simulation"):

    result = predict_sales(marketing, employees, time)

    st.metric("Predicted Sales", result["Predicted Sales"])
    st.metric("Risk Level", result["Risk Level"])

    st.subheader("AI Explanation")

    explanation = f"""
    Marketing Spend: ₹{marketing}
    Employees: {employees}
    Time: {time} days

    Expected Sales: ₹{result['Predicted Sales']}
    Growth Rate: {result['Growth Rate']}%
    Risk Level: {result['Risk Level']}
    """

    st.write(explanation)

    st.subheader("Strategic Advice")

    if marketing < 60000:
        st.write("✔ Increase marketing for better growth")
    else:
        st.write("✔ Marketing is sufficient")

    if employees < 15:
        st.write("✔ Hiring more staff can improve operations")
    else:
        st.write("✔ Workforce is stable")

    if time < 30:
        st.write("✔ Longer planning horizon boosts impact")
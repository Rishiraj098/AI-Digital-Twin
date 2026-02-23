import streamlit as st
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.style_loader import load_css
load_css()

st.title("Login")

user = st.text_input("Username")
pwd = st.text_input("Password", type="password")

if st.button("Login"):
    if user == "admin" and pwd == "123":
        st.success("Login Successful")
    else:
        st.error("Invalid Credentials")
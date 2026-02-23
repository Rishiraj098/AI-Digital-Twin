import streamlit as st
from pathlib import Path

def load_css():
    # Always start from project root (NOT current page)
    project_root = Path(__file__).resolve().parent.parent
    
    css_path = project_root / "assets" / "style.css"

    try:
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass   # silent fail → no ugly warning on UI
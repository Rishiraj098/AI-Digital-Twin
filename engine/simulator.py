import joblib
import numpy as np
import os
import streamlit as st

MODEL_PATH = os.path.join("Models", "model.pkl")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

def predict_sales(marketing, employees, time):

    model = load_model()

    raw_pred = model.predict([[marketing, employees, time]])

    if isinstance(raw_pred, (list, np.ndarray)):
        prediction = raw_pred[0]
    else:
        prediction = raw_pred

    growth = round((prediction / 100000) * 100, 2)
    risk = "Moderate" if marketing < 60000 else "Low"

    return {
        "Predicted Sales": int(prediction),
        "Growth Rate": growth,
        "Risk Level": risk
    }
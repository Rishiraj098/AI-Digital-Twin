import pickle
import numpy as np

import streamlit as st
import joblib

@st.cache_resource
def load_model():
    return joblib.load("Models/model.pkl")

model = load_model()

def predict_sales(marketing, employees, time):
    input_data = np.array([[marketing, employees, time]])
    prediction = model.predict(input_data)
    return round(prediction[0], 2)
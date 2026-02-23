import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

@st.cache_resource
def load_embed_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_embed_model()

def embed_texts(texts):
    vectors = model.encode(texts)
    return np.array(vectors).astype("float32")
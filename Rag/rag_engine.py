from .embeddings import model, embed_texts
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import streamlit as st

@st.cache_resource
def load_knowledge():
    with open("data/knowledge_base.txt", "r") as f:
        return [k.strip() for k in f.readlines() if k.strip()]

knowledge = load_knowledge()
knowledge_vectors = embed_texts(knowledge)

# 🔥 SAFETY CHECK
if len(knowledge) == 0:
    raise ValueError("Knowledge base is empty. Add content to knowledge_base.txt")

knowledge_vectors = embed_texts(knowledge)

# 🔥 SAFETY CHECK
if knowledge_vectors.shape[0] == 0:
    raise ValueError("Embeddings failed — check knowledge_base.txt content")

def retrieve_advice(query):

    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    similarities = cosine_similarity(query_vector, knowledge_vectors)

    top_indices = similarities[0].argsort()[-2:][::-1]

    results = [knowledge[i] for i in top_indices]

    return results
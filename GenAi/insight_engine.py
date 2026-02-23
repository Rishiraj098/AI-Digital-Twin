from Rag.rag_engine import retrieve_advice

def generate_insight(marketing, employees, predicted_sales):

    # Base explanation
    if marketing > employees * 1000:
        explanation = "Sales are driven by strong marketing influence."
    elif employees * 1000 > marketing:
        explanation = "Sales are driven by workforce capacity."
    else:
        explanation = "Sales are driven by balanced investment."

    # Growth level
    if predicted_sales > 200000:
        growth = "This indicates strong business expansion."
    elif predicted_sales > 100000:
        growth = "This indicates moderate growth."
    else:
        growth = "This reflects limited growth."

    # RAG Advice
    query = "How to improve sales strategy?"
    advice = retrieve_advice(query)

    return {
        "Explanation": explanation,
        "Growth Insight": growth,
        "Strategic Advice": advice
    }
    @st.cache_data
    def generate_cached_insight(m,e,s):
     return generate_insight(m,e,s)
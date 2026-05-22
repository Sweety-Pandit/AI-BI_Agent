import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

st.title("Ask Business Questions")
question = st.text_input("Ask a question about your dataset")

if st.button("Analyze"):

    payload = {"question": question}
    response = requests.post(f"{API_BASE_URL}/query/", json=payload)

    if response.status_code == 200:
        data = response.json()
        st.subheader("AI Response")
        st.markdown(data["ai_response"])
        st.subheader("Analysis Result")
        st.json(data["analysis"])

    else:
        st.error("Failed to process question")
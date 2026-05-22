import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

st.title("AI Business Insights")

if st.button("Generate AI Insights"):
    with st.spinner("Analyzing Dataset..."):

        response = requests.get(f"{API_BASE_URL}/chat/insights")

        if response.status_code == 200:
            insights = response.json()["insights"]
            st.subheader("Executive Insights")
            st.markdown(insights)

        else:
            st.error("Failed to generate insights")
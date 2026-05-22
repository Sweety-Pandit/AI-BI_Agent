import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://127.0.0.1:8000"

st.title("Analytics Dashboard")

response = requests.get(
    f"{API_BASE_URL}/analytics/summary"
)

if response.status_code == 200:
    data = response.json()
    st.subheader("Dataset Overview")
    st.json(data["overview"])
    st.subheader("Basic Statistics")
    st.json(data["statistics"])
    st.subheader("Missing Value Analysis")
    st.json(data["missing_values"])
    st.subheader("Correlation Analysis")
    correlation_data = data["correlation"]

    if correlation_data:
        corr_df = pd.DataFrame(correlation_data)

        st.dataframe(corr_df)

else:
    st.warning("No dataset available")
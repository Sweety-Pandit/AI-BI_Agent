import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"


st.title("Upload Dataset")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "text/csv"
        )
    }

    response = requests.post(f"{API_BASE_URL}/upload/csv", files=files)

    if response.status_code == 200:
        data = response.json()
        st.success("Dataset Uploaded Successfully")
        st.subheader("Dataset Information")
        st.json(data)

    else:
        st.error("Upload Failed")
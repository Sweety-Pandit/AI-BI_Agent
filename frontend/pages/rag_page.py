import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"
st.title("Business Knowledge RAG")
uploaded_file = st.file_uploader("Upload Business Document", type=["txt"])

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "text/plain"
        )
    }

    response = requests.post(f"{API_BASE_URL}/rag/upload-document", files=files)

    if response.status_code == 200:
        st.success("Document Indexed Successfully")
    else:
        st.error("Failed to upload document")

st.subheader("Ask Questions")

question = st.text_input(
    "Ask business knowledge questions"
)

if st.button("Ask RAG"):

    response = requests.get(f"{API_BASE_URL}/rag/query", params={"question": question})

    if response.status_code == 200:
        data = response.json()
        st.subheader("AI Response")
        st.markdown(data["response"])
        st.subheader("Retrieved Context")
        st.json(data["context"])

    else:
        st.error("Failed to retrieve answer")
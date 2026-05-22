import streamlit as st
from components.styles import load_custom_css
from components.sidebar import render_sidebar


st.set_page_config(page_title="AI BI Agent", layout="wide")

load_custom_css()
page = render_sidebar()

if page == "Dashboard":
    exec(open("frontend/pages/dashboard_page.py").read())

elif page == "Upload Dataset":
    exec(open("frontend/pages/upload_page.py").read())

elif page == "Analytics":
    exec(open("frontend/pages/analytics_page.py").read())

elif page == "AI Insights":
    exec(open("frontend/pages/insights_page.py").read())

elif page == "Business Query":
    exec(open("frontend/pages/query_page.py").read())

elif page == "Knowledge RAG":
    exec(open("frontend/pages/rag_page.py").read())
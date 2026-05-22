import streamlit as st

def render_sidebar():

    st.sidebar.title("🤖 AI BI Analyst")
    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Upload Dataset",
            "Analytics",
            "AI Insights",
            "Business Query",
            "Knowledge RAG"
        ]
    )

    st.sidebar.markdown("---")
    st.sidebar.info(
        """
        AI-Powered Business Intelligence Platform
        Features:
        - Automated EDA
        - AI Analytics
        - RAG
        - Visual Insights
        """
    )

    return page
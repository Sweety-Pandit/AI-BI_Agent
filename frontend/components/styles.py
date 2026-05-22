import streamlit as st


def load_custom_css():

    st.markdown(
        """
        <style>

        .main {
            background-color: #0E1117;
            color: white;
        }

        .stApp {
            background-color: #0E1117;
        }

        section[data-testid="stSidebar"] {
            background-color: #161B22;
        }

        .metric-card {
            background-color: #161B22;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #30363D;
            text-align: center;
        }

        .metric-title {
            font-size: 18px;
            color: #8B949E;
        }

        .metric-value {
            font-size: 28px;
            font-weight: bold;
            color: white;
        }

        .dashboard-title {
            font-size: 40px;
            font-weight: bold;
            color: white;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
import streamlit as st
from components.metrics import metric_card

st.markdown(
    """
    <div class="dashboard-title">
        AI Business Intelligence Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("")
col1, col2, col3 = st.columns(3)

with col1:
    metric_card("Datasets", "12")

with col2:
    metric_card("AI Insights Generated", "156")

with col3:
    metric_card("Analytics Queries", "89")

st.markdown("---")
st.subheader("Platform Overview")
st.markdown("""
This platform provides:

- Automated exploratory data analysis
- AI-generated business insights
- Trend analysis
- Visualization dashboards
- RAG-powered analytics
- Natural language business queries
""")
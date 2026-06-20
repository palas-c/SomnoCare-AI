"""
Dashboard page component for SomnoCare AI.
"""

import streamlit as st


def show_dashboard():
    """Display main application dashboard."""

    st.markdown(
        """
        <div style='text-align:center'>

        <h1>
        🌙 SomnoCare 
        <span style='color:#818cf8'>
        AI v2
        </span>
        </h1>

        <h3>
        AI Sleep Health Assistant
        </h3>

        <p>
        Machine Learning • Sleep Analysis • Health Insights
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown(
        """
        <div class='ai-card'>

        <h2>
        Welcome 👋
        </h2>

        <p>
        Analyze your sleep patterns and receive AI-powered insights.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    if st.button("Start New Analysis"):
        st.session_state.page = "New Analysis"
        st.rerun()


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "Total Analysis",
            "0"
        )


    with col2:
        st.metric(
            "Average Sleep Score",
            "--"
        )


    with col3:
        st.metric(
            "Risk Status",
            "Unknown"
        )


    st.markdown("---")


    st.subheader(
        "Analysis Features"
    )


    c1, c2, c3, c4 = st.columns(4)


    c1.info(
        "🌙 Sleep Disorder Prediction"
    )


    c2.info(
        "⭐ Sleep Quality Score"
    )


    c3.info(
        "🧬 Sleep Twin Profile"
    )


    c4.info(
        "👨‍⚕️ Doctor AI Insights"
    )
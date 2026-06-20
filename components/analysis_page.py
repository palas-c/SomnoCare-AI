"""
New analysis page component for SomnoCare AI.
"""

import streamlit as st

from components.input_panel import get_user_inputs
from components.prediction import show_prediction


def show_analysis_page():
    """Display sleep analysis input and prediction section."""

    st.markdown(
        """
        <div class="ai-card">

        <h1>🧠 Sleep Analysis</h1>

        <p>
        Enter your sleep and lifestyle information.
        <br>
        SomnoCare AI will analyze your sleep health.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    user_data = get_user_inputs()


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    show_prediction(
        user_data
    )
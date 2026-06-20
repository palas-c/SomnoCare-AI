"""
Doctor AI insights page component for SomnoCare AI.
"""

import streamlit as st

from utils.doctor_ai import generate_sleep_insights


def show_doctor_page():
    """Display AI-generated sleep health insights."""

    st.markdown(
        """
        <div class="ai-card">

        <h1>👨‍⚕️ Doctor AI Assistant</h1>

        <p>
        AI-powered sleep health interpretation.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    if "sleep_result" not in st.session_state:

        st.warning(
            "Please complete a sleep analysis first."
        )

        return


    result = st.session_state.sleep_result
    user_data = st.session_state.user_data


    if "doctor_insights" in st.session_state:

        doctor_report = st.session_state.doctor_insights

    else:

        with st.spinner(
            "Generating sleep insights..."
        ):

            doctor_report = generate_sleep_insights(
                result,
                user_data
            )


    st.markdown(
        """
        ## Health Summary
        """
    )


    st.success(
        doctor_report[
            "summary"
        ]
    )


    st.markdown(
        """
        ## Sleep Profile Analysis
        """
    )


    st.info(
        doctor_report[
            "sleep_profile"
        ]
    )


    st.markdown(
        """
        ## Recommendations
        """
    )


    for advice in doctor_report[
        "recommendations"
    ]:

        st.info(
            advice
        )
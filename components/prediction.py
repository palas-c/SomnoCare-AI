"""
Prediction component for SomnoCare AI.
Handles ML prediction, AI insights, and result storage.
"""

import streamlit as st

from utils.prediction_engine import predict_sleep_health
from utils.storage import save_analysis
from utils.doctor_ai import generate_sleep_insights


def show_prediction(user_data):
    """Run sleep analysis and display prediction preview."""

    analyze = st.button(
        "Analyze My Sleep"
    )


    if analyze:

        try:

            with st.spinner(
                "Analyzing sleep health data..."
            ):

                result = predict_sleep_health(
                    user_data
                )

                insights = generate_sleep_insights(
                    result,
                    user_data
                )


            # Store current analysis in session
            st.session_state.sleep_result = result
            st.session_state.user_data = user_data
            st.session_state.doctor_insights = insights


            # Save analysis history
            save_analysis(
                user_data,
                result,
                insights
            )


            st.success(
                "Analysis completed successfully"
            )


            st.info(
                "Results, insights, and history updated"
            )


            st.markdown(
                """
                ## Analysis Preview
                """
            )


            col1, col2, col3 = st.columns(3)


            with col1:

                st.metric(
                    label="Sleep Disorder",
                    value=result[
                        "sleep_disorder"
                    ]
                )


            with col2:

                st.metric(
                    label="Sleep Quality",
                    value=result[
                        "sleep_quality"
                    ]
                )


            with col3:

                st.metric(
                    label="Sleep Profile",
                    value=result[
                        "sleep_profile"
                    ]
                )


        except Exception as error:

            st.error(
                "Prediction failed"
            )

            st.exception(
                error
            )
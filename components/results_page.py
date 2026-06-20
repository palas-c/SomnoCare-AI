"""
Results dashboard component for SomnoCare AI.
"""

import streamlit as st


def show_results_page():
    """Display sleep analysis results."""

    st.markdown(
        """
        <div class="ai-card">

        <h1>📊 Sleep Intelligence Dashboard</h1>

        <p>
        Personalized sleep health analysis results.
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
            "No analysis found. Please run a sleep analysis first."
        )

        return


    result = st.session_state.sleep_result


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
            label="Sleep Quality Score",
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


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    st.markdown(
        """
        ## Health Evaluation
        """
    )


    score = result[
        "sleep_quality"
    ]


    if score >= 8:

        st.success(
            """
            Excellent Sleep Health

            Your sleep pattern looks strong.
            Maintain your current habits.
            """
        )


    elif score >= 6:

        st.warning(
            """
            Moderate Sleep Quality

            Some improvements in lifestyle and sleep routine
            may improve your sleep score.
            """
        )


    else:

        st.error(
            """
            Sleep Improvement Recommended

            Your sleep indicators suggest that lifestyle
            improvements may be beneficial.
            """
        )


    st.markdown(
        """
        ## Sleep Profile Analysis
        """
    )


    st.info(
        f"""
        SomnoCare classified your sleep pattern as:

        **{result["sleep_profile"]}**

        Future personalized recommendations can use
        this profile for deeper insights.
        """
    )
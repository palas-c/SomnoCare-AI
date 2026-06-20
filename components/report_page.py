"""
PDF report page component for SomnoCare AI.
"""

import streamlit as st

from utils.storage import load_history
from utils.report_generator import generate_report


def show_report_page():
    """Generate and download sleep analysis reports."""

    st.markdown(
        """
        <div class="ai-card">

        <h1>📄 Sleep Reports</h1>

        <p>
        Generate detailed sleep health analysis reports.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    history = load_history()


    if len(history) == 0:

        st.warning(
            "No analysis available for report generation."
        )

        return


    latest = history[-1]

    prediction = latest[
        "prediction"
    ]


    st.info(
        f"""
        Latest Analysis:

        Sleep Disorder: {prediction["sleep_disorder"]}

        Sleep Quality Score: {prediction["sleep_quality"]}

        Sleep Profile: {prediction["sleep_profile"]}
        """
    )


    if st.button(
        "Generate Sleep Report"
    ):

        path = generate_report(
            latest
        )


        with open(
            path,
            "rb"
        ) as file:

            st.download_button(
                label="Download Report",
                data=file,
                file_name="SomnoCare_Report.pdf",
                mime="application/pdf"
            )


        st.success(
            "Report generated successfully."
        )
"""
Analysis history page component for SomnoCare AI.
"""

import streamlit as st

from utils.storage import load_history


def show_history_page():
    """Display previous sleep analysis records."""

    st.markdown(
        """
        <div class="ai-card">

        <h1>📜 Analysis History</h1>

        <p>
        View previous sleep health analysis reports.
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
            "No previous analysis found."
        )

        return


    for record in reversed(history):

        prediction = record[
            "prediction"
        ]


        st.markdown(
            f"""
            <div class="ai-card">

            <h3>
            {record.get("timestamp", "Unknown Date")}
            </h3>


            <p>
            Sleep Disorder:
            <b>{prediction["sleep_disorder"]}</b>
            </p>


            <p>
            Sleep Quality:
            <b>{prediction["sleep_quality"]}</b>
            </p>


            <p>
            Sleep Profile:
            <b>{prediction["sleep_profile"]}</b>
            </p>


            </div>

            <br>
            """,
            unsafe_allow_html=True
        )
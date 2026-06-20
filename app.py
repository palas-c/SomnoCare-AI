"""
SomnoCare AI v2
Main Streamlit Application
"""

import streamlit as st

from components.sidebar import show_sidebar
from components.dashboard import show_dashboard
from components.account_panel import show_account_panel
from components.analysis_page import show_analysis_page
from components.results_page import show_results_page
from components.doctor_page import show_doctor_page
from components.history_page import show_history_page
from components.report_page import show_report_page


# App configuration
st.set_page_config(
    page_title="SomnoCare AI v2",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_css():
    """Load custom CSS styles."""

    with open(
        "assets/style.css",
        "r",
        encoding="utf-8"
    ) as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )


load_css()


# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


# Sidebar navigation
page = show_sidebar()


# Application layout
main_area, account_area = st.columns(
    [5, 1.2],
    gap="large"
)


# Page routing
with main_area:

    if page == "Dashboard":
        show_dashboard()

    elif page == "New Analysis":
        show_analysis_page()

    elif page == "Results":
        show_results_page()

    elif page == "Doctor AI":
        show_doctor_page()

    elif page == "History":
        show_history_page()

    elif page == "Reports":
        show_report_page()

    elif page == "Profile":
        st.markdown(
            """
            <div class="ai-card">

            <h1>👤 Profile</h1>

            <p>
            User profile management will be available in a future update.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    elif page == "Settings":
        st.markdown(
            """
            <div class="ai-card">

            <h1>⚙ Settings</h1>

            <p>
            Application settings will be available in a future update.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    elif page == "Logout":
        st.success("Demo mode active")


# Account panel
with account_area:
    show_account_panel()
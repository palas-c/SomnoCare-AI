"""
Sidebar navigation component for SomnoCare AI.
"""

import streamlit as st


def nav_item(icon, name):
    """Create a sidebar navigation item."""

    active = st.session_state.page == name

    if active:
        st.markdown(
            f"""
            <div class="selected-menu">
                {icon} {name}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        if st.button(
            f"{icon} {name}",
            key=name,
            use_container_width=True
        ):
            st.session_state.page = name
            st.rerun()


def show_sidebar():
    """Display application sidebar."""

    if "page" not in st.session_state:
        st.session_state.page = "Dashboard"

    menu_items = [
        ("🏠", "Dashboard"),
        ("🧠", "New Analysis"),
        ("📊", "Results"),
        ("👨‍⚕️", "Doctor AI"),
        ("📜", "History"),
        ("📄", "Reports"),
    ]

    with st.sidebar:

        st.markdown(
            """
            <div class="logo">

            🌙 SomnoCare AI

            <br>

            <span>
            AI Sleep Assistant
            </span>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            "<p class='menu-title'>MENU</p>",
            unsafe_allow_html=True
        )

        for icon, name in menu_items:
            nav_item(icon, name)

    return st.session_state.page
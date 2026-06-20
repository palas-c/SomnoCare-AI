"""
Account panel component for SomnoCare AI.
"""

import streamlit as st


def account_item(icon, name):
    """Create account navigation item."""

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
            key=f"account_{name}",
            use_container_width=True
        ):
            st.session_state.page = name
            st.rerun()


def show_account_panel():
    """Display user account section."""

    st.markdown(
        """
        <div class="account-card">

        <h3>👤 Demo User</h3>

        <p>
        SomnoCare User
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='menu-title'>ACCOUNT</p>",
        unsafe_allow_html=True
    )


    account_options = [
        ("👤", "Profile"),
        ("⚙️", "Settings"),
    ]


    for icon, name in account_options:
        account_item(icon, name)


    st.markdown(
        """
        <div class="sleep-card">

        🌙 <b>Better Sleep</b>

        <br>

        Better Life

        </div>
        """,
        unsafe_allow_html=True
    )


    account_item(
        "↪",
        "Logout"
    )
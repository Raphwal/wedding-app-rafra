import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Could not get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 150px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
    )
    
    with st.sidebar:
        st.title("Neda & Peter :bouquet:")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):
            st.page_link("pages/p01_startseite.py",     label="Startseite",     icon="❣️")
            st.page_link("pages/p02_ablaufplan.py",     label="Ablaufplan",     icon="⌚")
            st.page_link("pages/p03_unterkunft.py",     label="Unterkunft",     icon="🏡")
            st.page_link("pages/p04_speisekarte.py",    label="Speisekarte",    icon="🥢")
            st.page_link("pages/p05_ort.py",            label="Anfahrt",        icon="🚘")
            st.page_link("pages/p06_mitfahrboerse.py",  label="Mitfahrbörse",   icon="🚏")
            st.page_link("pages/p07_faq.py",            label="FAQ",            icon="❓")

            st.write("")
            st.write("")

            if st.button("Abmelden"):
                logout()

        elif get_current_page_name() != "main":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("main.py")



def collapse_sidebar():
    collapse_sidebar_js = """
        <script>
            setTimeout(function() {
                let sidebar = window.parent.document.querySelector("section[data-testid='stSidebar']");
                if (sidebar) { sidebar.style.display = 'none'; }
            }, 300);
        </script>
    """
    st.markdown(collapse_sidebar_js, unsafe_allow_html=True)


def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("main.py")

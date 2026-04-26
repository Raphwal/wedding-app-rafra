import streamlit as st
from time import sleep
from navigation import make_sidebar

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Initialisierung der session_states
if all(key not in st.session_state for key in ('pwd', 'pwd_correct', 'form_submitted', 'logged_in')):
    st.session_state['pwd'] = ""
    st.session_state['pwd_correct'] = False
    st.session_state['form_submitted'] = False
    st.session_state['logged_in'] = False


def check_login():
    """Check login credentials and update session state accordingly."""
    st.session_state['form_submitted'] = True

    if st.session_state['pwd'] == st.secrets['password']:
        st.session_state['pwd_correct'] = True
        st.session_state['logged_in'] = True
        st.session_state['pwd'] = ""
    else:
        st.session_state['pwd_correct'] = False


def display_login_form():
    """Display the login form."""
    with st.form("login_form"):
        st.text_input("Code", type="password", key="pwd")
        st.form_submit_button("Login", on_click=check_login)


# Sidebar navigation
make_sidebar()

st.title("Schön, dass Ihr hergefunden habt.")

if not st.session_state['logged_in']:
    st.warning('**Vorweg**: In der mobilen sowie in der Browser-Version dient der **linke Pfeil oben in der Ecke** zum Öffnen und Schließen der **Seitennavigation**. Nach erfolgreicher Anmeldung werden die Kategorien in der Navigation sichtbar.')
    st.write("Bitte den in der Einladung beigefügten Code eintragen, um fortzufahren")
    display_login_form()
    if st.session_state['form_submitted'] and not st.session_state['pwd_correct']:
        st.error("Code nicht gültig")
else:
    st.success("Du hast es geschafft ✨")
    sleep(0.5)
    st.switch_page("pages/p01_startseite.py")

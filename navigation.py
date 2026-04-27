import streamlit as st
from time import sleep

def logout():
    st.session_state.logged_in = False
    st.session_state.pwd_correct = False
    st.info("Abmeldung erfolgreich...")
    sleep(0.5)
    st.rerun()

def check_login():
    """Prüft das Passwort und setzt den Login-Status."""
    if st.session_state['pwd'] == st.secrets['password']:
        st.session_state['pwd_correct'] = True
        st.session_state['logged_in'] = True
    else:
        st.session_state['pwd_correct'] = False

def login_page():
    """Die Seite, die vor dem Login angezeigt wird."""
    st.title("Schön, dass Ihr hergefunden habt.")
    st.write("Bitte den in der Einladung beigefügten Code eintragen, um fortzufahren.")
    
    with st.form("login_form"):
        st.text_input("Code", type="password", key="pwd")
        if st.form_submit_button("Login", on_click=check_login):
            if st.session_state.logged_in:
                st.rerun()
    
    if "pwd_correct" in st.session_state and not st.session_state.pwd_correct:
        st.error("Code nicht gültig")

def get_navigation():
    """Erstellt die Navigationsstruktur basierend auf dem Login-Status."""
    
    # Definition der Seiten-Objekte
    p_login = st.Page(login_page, title="Login", icon="🔒")
    p_logout = st.Page(logout, title="Abmelden", icon="🚶")

    p1 = st.Page("views/p01_startseite.py",   title="Startseite",    icon="❣️")
    p2 = st.Page("views/p02_ablaufplan.py",   title="Ablaufplan",    icon="⌚")
    p3 = st.Page("views/p03_unterkunft.py",   title="Unterkunft",    icon="🏡")
    p4 = st.Page("views/p04_speisekarte.py",  title="Speisekarte",   icon="🥢")
    p5 = st.Page("views/p05_ort.py",          title="Anfahrt",       icon="🚘")
    p6 = st.Page("views/p06_mitfahrboerse.py", title="Mitfahrbörse",  icon="🚏")
    p7 = st.Page("views/p07_faq.py",           title="FAQ",           icon="❓")

    if st.session_state.get("logged_in", False):
        # Wenn eingeloggt: Zeige Top-Navigation
        # Die erste Seite in der Liste (p1) ist die Standard-Startseite
        return st.navigation(
            {
                "Neda & Peter 💐": [p1, p2, p3, p4, p5, p6, p7],
                "Optionen": [p_logout]
            }, 
            position="top" # <-- Hier passiert die Magie!
        )
    else:
        # Wenn nicht eingeloggt: Zeige nur die Login-Maske (ohne Menü)
        return st.navigation([p_login], position="hidden")

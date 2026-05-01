import streamlit as st
from streamlit_option_menu import option_menu

# 1. Konfiguration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 2. Login-Logik (wie gehabt)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def check_login():
    if st.session_state['pwd'] == st.secrets['password']:
        st.session_state['logged_in'] = True
    else:
        st.error("Code nicht gültig")

# 3. Anzeige der Navigation ODER Login
if not st.session_state.logged_in:
    st.title("Schön, dass Ihr hergefunden habt.")
    with st.form("login"):
        st.text_input("Code", type="password", key="pwd")
        st.form_submit_button("Anmelden", on_click=check_login)
else:
    # --- DIE TOP-NAVIGATION ---
    # Diese Leiste erscheint oben auf der Seite
    selected = option_menu(
        menu_title=None, 
        options=["Startseite", "Ablaufplan", "Unterkunft", "Anfahrt", "Abmelden"],
        icons=["house", "clock", "house-heart", "car-front", "box-arrow-right"], 
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#F5F3FF"},
            "icon": {"color": "#4A3B5C", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#EDE7F6"},
            "nav-link-selected": {"background-color": "#D1C4E9", "color": "#4A3B5C"},
        }
    )
    # horizontale Linie unter der Navigation
    st.markdown(
        """
        <hr style="border: 0; height: 1px; background: #D1C4E9; margin-top: 0; margin-bottom: 20px;">
        """,
        unsafe_allow_html=True
    )

    # 4. Routing: Welche Seite soll angezeigt werden?
    with st.container():
        if selected == "Startseite":
            with open("views/p01_startseite.py", encoding="utf-8") as f:
                exec(f.read())
                
        elif selected == "Ablaufplan":
            with open("views/p02_ablaufplan.py", encoding="utf-8") as f:
                exec(f.read())

        elif selected == "Unterkunft":
            with open("views/p03_unterkunft.py", encoding="utf-8") as f:
                exec(f.read())

        elif selected == "Anfahrt":
            with open("views/p05_ort.py", encoding="utf-8") as f:
                exec(f.read())

        elif selected == "Abmelden":
            st.session_state.logged_in = False
            st.rerun()
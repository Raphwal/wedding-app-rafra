import streamlit as st
from streamlit_option_menu import option_menu

# 1. Konfiguration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# CSS für Hintergrund-Textur, Schriftarten und Text-Schatten
st.markdown("""
    <style>
        /* Import der eleganten Serif-Schrift */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Montserrat:wght@700&display=swap');

        /* Hintergrund-Farbe und eine leichte Textur-Simulation */
        .stApp {
            background-color: #EEDC9A;
            background-image: url("https://www.transparenttextures.com/patterns/linen-paper.png");
        }

        /* Styling für die dunkelbraune Serif-Schrift (wie im Bild oben) */
        .serif-text {
            font-family: 'Playfair Display', serif;
            color: #3D2B1F;
            font-size: 32px;
            text-align: center;
            line-height: 1.4;
            margin-bottom: 20px;
        }

        /* Styling für die weiße Sans-Serif Schrift mit Schatten (wie im Bild unten) */
        .sans-white-text {
            font-family: 'Montserrat', sans-serif;
            color: #FFFFFF;
            font-size: 18px;
            text-align: center;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
            line-height: 1.2;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Login-Logik (wie gehabt)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def check_login():
    if st.session_state['pwd'] == st.secrets['password']:
        st.session_state['logged_in'] = True
    else:
        st.error("Passwort nicht gültig")

# 3. Anzeige der Navigation ODER Login
if not st.session_state.logged_in:
    st.title("Schön, dass Ihr hergefunden habt.")
    st.markdown('<div class="header-text">Wir heiraten und freuen uns darauf mit Euch gemeinsam zu feiern!</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Weitere Informationen findet ihr auf unserer Hochzeitswebsite unter:</div>', unsafe_allow_html=True)
    with st.form("login"):
        st.text_input('Passwort:', type="password", key="pwd")
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
            "container": {"padding": "0!important", "background-color": "#D4C285", "border-radius": "0px"},
            "icon": {"color": "#3D2B1F", "font-size": "18px"}, 
            "nav-link": {
                "font-family": "'Montserrat', sans-serif",
                "font-size": "14px", 
                "text-align": "center", 
                "margin":"0px", 
                "color": "#3D2B1F",
                "--hover-color": "#EEDC9A"
            },
            "nav-link-selected": {"background-color": "#3D2B1F", "color": "#EEDC9A"},
        }
    )
    # horizontale Linie unter der Navigation
    st.markdown('<hr style="border: 0; height: 1px; background: #3D2B1F; margin-top: 0;">', unsafe_allow_html=True)

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
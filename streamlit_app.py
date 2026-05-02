import streamlit as st
from streamlit_option_menu import option_menu
from utils import set_encrypted_bg

# 1. Konfiguration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# CSS für Hintergrund-Textur, Schriftarten und Text-Schatten
st.markdown("""
    <style>
        /* 1. Schriften importieren */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Montserrat:wght@700&display=swap');

        /* 2. Basis-Hintergrund (Nur Farbe als Fallback) */
        .stApp {
            background-color: #EEDC9A;
            /* Der background-image Teil wurde entfernt, 
               da dies jetzt von set_encrypted_bg übernommen wird */
        }

        /* 3. Styling für die Schriften (bleibt gleich) */
        .serif-text {
            font-family: 'Playfair Display', serif;
            color: #3D2B1F;
            font-size: 32px;
            text-align: center;
            line-height: 1.4;
            margin-bottom: 20px;
        }

        .sans-white-text {
            font-family: 'Montserrat', sans-serif;
            color: #FFFFFF;
            font-size: 18px;
            text-align: center;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.6); /* Schatten etwas verstärkt für Lesbarkeit */
            line-height: 1.2;
        }
        
        /* Optional: Macht die Boxen der App (Widgets) leicht transparent, 
           damit man das Hintergrundbild durchschimmern sieht */
        [data-testid="stVerticalBlock"] > div {
            background-color: rgba(238, 220, 154, 0.1); 
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

set_encrypted_bg("assets/Hintergrund.bin")

# 2. Login-Logik
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
    st.markdown('<div class="header-text">Bitte gebt das Passwort ein!</div>', unsafe_allow_html=True)
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
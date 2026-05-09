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
            background-color: #D6EAF8;
        }

        /* 3. Styling für die Schriften (bleibt gleich) */
        .serif-text {
            font-family: 'Playfair Display', serif;
            color: #2E4053; 
            font-size: 32px;
            text-align: center;
            text-shadow: 1px 1px 2px rgba(255,255,255,0.8); /* Heller Schatten für bessere Lesbarkeit */
        }

        /* Weißer Text (Untertitel) - Bleibt weiß, bekommt aber blauen Schatten */
        .sans-white-text {
            font-family: 'Montserrat', sans-serif;
            color: #FFFFFF;
            font-size: 18px;
            text-align: center;
            text-shadow: 1px 1px 4px rgba(46, 64, 83, 0.4); 
        }
        
        /* Optional: Macht die Boxen der App (Widgets) leicht transparent, 
           damit man das Hintergrundbild durchschimmern sieht */
        [data-testid="stVerticalBlock"] > div {
            background-color: rgba(255, 255, 255, 0.6); 
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
        options=["Startseite", "Ablaufplan", "Unterkunft", "Speisekarte", "Anfahrt", "FAQ", "Abmelden"],
        icons=["house", "clock", "house-heart", "clipboard2-heart", "car-front", "question-circle", "box-arrow-right"], 
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal",
        styles={
        "container": {"padding": "0!important", "background-color": "#EBF5FB", "border-radius": "0px"},
        "icon": {"color": "#5D6D7E", "font-size": "18px"}, 
        "nav-link": {
            "color": "#2E4053",
            "--hover-color": "#D6EAF8"
        },
        "nav-link-selected": {"background-color": "#5D6D7E", "color": "#FFFFFF"},
        }
        )
    # horizontale Linie unter der Navigation
    st.markdown('<hr style="border: 0; height: 1px; background: #2E4053; margin-top: 0;">', unsafe_allow_html=True)

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

        elif selected == "Speisekarte":
            with open("views/p04_speisekarte.py", encoding="utf-8") as f:
                exec(f.read())

        elif selected == "Anfahrt":
            with open("views/p05_ort.py", encoding="utf-8") as f:
                exec(f.read())

        elif selected == "FAQ":
            with open("views/p07_faq.py", encoding="utf-8") as f:
                exec(f.read())

        elif selected == "Abmelden":
            st.session_state.logged_in = False
            st.rerun()
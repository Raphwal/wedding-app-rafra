import streamlit as st
from streamlit_option_menu import option_menu
from utils import set_encrypted_bg

# 1. Konfiguration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# CSS für Hintergrund-Textur, Schriftarten und Text-Schatten
st.markdown("""
    <style>
        /* 1. Schriften & allgemeines Layout */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Montserrat:wght@700&display=swap');

        .stApp {
            background-color: #D6EAF8;
        }

        /* 2. Der allgemeine weiße Kasten für TEXT-Elemente */
        [data-testid="stVerticalBlock"] > div {
            background-color: rgba(255, 255, 255, 0.15); 
            border-radius: 15px;
            padding: 20px !important; /* Standard für Desktop */
            margin-bottom: 10px !important;
            
            /* Box-Modell absichern */
            box-sizing: border-box !important;
            display: block !important;
            width: 100% !important;
            max-width: 100% !important;
        }
            
        /* Wir zwingen ALLE Unterelemente (Texte, Links, Spans), 
           dass sie niemals breiter als ihre Eltern-Box werden dürfen. */
        [data-testid="stVerticalBlock"] > div * {
            max-width: 100% !important;
            overflow-wrap: break-word !important;
            word-wrap: break-word !important;
            word-break: break-word !important;
            white-space: normal !important; /* Verhindert das "Nicht-Umbrechen" von Links */
            box-sizing: border-box !important;
        }

        /* SPEZIAL-ANPASSUNG FÜR MOBILGERÄTE (Handys) */
        @media (max-width: 768px) {
            [data-testid="stVerticalBlock"] > div {
                padding: 12px !important; /* Weniger Padding auf dem Handy gibt dem Text mehr Platz */
            }
            
            /* Verhindert, dass Streamlit auf dem Handy zu viel Rand links/rechts lässt */
            .main .block-container {
                padding-left: 0.8rem !important;
                padding-right: 0.8rem !important;
                max-width: 100vw !important;
                overflow-x: hidden !important;
            }
            
            .serif-text {
                font-size: 26px !important; /* Titel etwas kleiner auf dem Handy */
            }
        }
        /* Spezial-Korrektur für Formulare und Eingabefelder, damit sie nicht wandern */
        [data-testid="stForm"], .stTextInput, .stButton {
            width: 100% !important;
            box-sizing: border-box !important;
        }
            
        /* NEU: Diese Regel entfernt die "Geister-Boxen" am Anfang der Seite */
        div[data-testid="stVerticalBlock"] > div:has(style), 
        div[data-testid="stVerticalBlock"] > div:empty {
            background-color: transparent !important;
            padding: 0px !important;
            margin: 0px !important;
            box-shadow: none !important;
        }    
        
        /* 3. AUSNAHME FÜR BILDER: Entfernt den weißen Kasten & die Ränder */
        /* Wir suchen Container, die ein Bild enthalten, und machen sie unsichtbar */
        div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stImage"]) {
            background-color: transparent !important;
            padding: 0px !important;
            box-shadow: none !important;
        }

        /* 4. BILD-STYLING (Zentrierung & Desktop-Größe) */
        [data-testid="stImage"] {
            display: flex;
            justify-content: center; /* Zentriert den Bild-Container */
        }

        [data-testid="stImage"] img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 15px; /* Schöne abgerundete Ecken direkt am Bild */
            box-shadow: 0 4px 15px rgba(46, 64, 83, 0.2); /* Eleganter Schatten */
        }

        /* Desktop-Beschränkung */
        @media (min-width: 1024px) {
            [data-testid="stImage"] img {
                max-width: 800px !important; /* Hier stellst du die Desktop-Breite ein */
                width: auto !important;
            }
        }

        /* Mobile-Ansicht (Handy) */
        @media (max-width: 1023px) {
            [data-testid="stImage"] img {
                width: 100% !important; /* Auf dem Handy volle Breite nutzen */
            }
        }

        /* 5. TEXT-SCHATTEN (Korrektur gegen das Verrutschen) */
        .serif-text {
            font-family: 'Playfair Display', serif;
            color: #2E4053; 
            font-size: 32px;
            text-align: center;
            text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.9), 0px 0px 5px rgba(255, 255, 255, 0.6);
        }

        .sans-white-text {
            font-family: 'Montserrat', sans-serif;
            color: #FFFFFF;
            font-size: 18px;
            text-align: center;
            text-shadow: 0px 0px 8px rgba(46, 64, 83, 0.6); 
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
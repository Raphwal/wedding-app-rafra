import streamlit as st
from utils import decrypt_text
from views.data import ENCRYPTED_CONTENT
from utils import load_decrypted_image


# --- (VERSCHLÜSSELT) ---
kontakt_name = decrypt_text(ENCRYPTED_CONTENT["name_trauzeugin"])
kontakt_telefon = decrypt_text(ENCRYPTED_CONTENT["tele_trauzeugin"])
date1 = decrypt_text(ENCRYPTED_CONTENT["date1"])
date2 = decrypt_text(ENCRYPTED_CONTENT["date2"])
location_name = decrypt_text(ENCRYPTED_CONTENT["location_name"])

img_data = load_decrypted_image("assets/Ablaufplan.bin")
st.image(img_data, caption="Foto von der Glücksburg")

# 1. Page-spezifisches CSS (Nur für das Layout der Boxen)
st.markdown(
    """
    <style>
        .subtitle {
            font-family: 'Playfair Display', serif;
            font-size: 28px;
            font-weight: bold;
            color: #2E4053;
            margin-top: 25px;
        }
        .event {
            font-size: 18px;
            margin: 12px 0;
            padding: 15px;
            background-color: rgba(255, 255, 255, 0.3); /* Etwas heller für bessere Lesbarkeit */
            border-left: 5px solid #2E4053;
            border-radius: 8px;
            color: #2E4053;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        }
        .contact-box {
            font-size: 18px;
            color: #2E4053;
            margin-top: 30px;
            padding: 25px;
            background-color: rgba(255, 255, 255, 0.6); 
            border: 2px dashed #2E4053;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(46, 64, 83, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel (Nutzt die Klasse aus deiner main.py)
#st.markdown('<h1 class="serif-text">Ablaufplan</h1>', unsafe_allow_html=True)

# --- Day 1 ---
st.markdown(f'<h2 class="subtitle">Freitag, <b>{date1}</b> </h2>', unsafe_allow_html=True)

events_day1 = [
    (f"Empfang im {location_name}", "ab 16:00 Uhr"),
    (f"Beginn der freien Trauung", "ab 16:30 Uhr"),
    (f"Fotos", "ab 17:00 Uhr"),
    (f"Eröffnung des Buffets", "ab 18:30 Uhr"),
    (f"Torte anschneiden & Dessert", "gegen 20:00 Uhr"),
    (f"Eröffnung der Tanzfläche", "gegen 21:00 Uhr"),
    (f"Mitternachtssnack", "gegen 23:30 Uhr")
]

for event, time in events_day1:
    st.markdown(f'<div class="event"><b>{time}</b>: {event}</div>', unsafe_allow_html=True)

st.divider()

# --- Day 2 ---
st.markdown(f'<h2 class="subtitle">Samstag, <b>{date2}</b> </h2>', unsafe_allow_html=True)

events_day2 = [
    (f"Frühstück im {location_name} Restaurant (für alle die wollen) - bitte Info geben", "08:00 bis 09:45 Uhr"),
    (f"Check-Out", "bis 10:00 Uhr")
]

for event, time in events_day2:
    st.markdown(f'<div class="event"><b>{time}</b>: {event}</div>', unsafe_allow_html=True)

st.divider()

# --- Kontakt-Box ---
st.markdown(
    f"""
    <div class="contact-box">
        💡 Möchtet ihr einen Programmpunkt beisteuern? <br>
        Meldet euch gerne bei <b>{kontakt_name}</b> unter {kontakt_telefon}.
    </div>
    """, unsafe_allow_html=True)
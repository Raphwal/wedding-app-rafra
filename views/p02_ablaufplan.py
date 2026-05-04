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
            color: #3D2B1F; /* Dunkelbraun wie im Bild */
            margin-top: 20px;
        }
        .event {
            font-size: 18px;
            margin: 10px 0;
            padding: 15px;
            background-color: rgba(61, 43, 31, 0.05); /* Sehr dezentes Braun */
            border-left: 5px solid #3D2B1F; /* Brauner Akzent-Balken */
            border-radius: 5px;
            color: #3D2B1F;
        }
        .contact-box {
            font-size: 18px;
            color: #3D2B1F;
            margin-top: 30px;
            padding: 15px;
            border: 1px dashed #3D2B1F;
            border-radius: 10px;
            text-align: center;
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
    (f"Buffet", "ab 18:30 Uhr"),
    (f"Torte anschneiden & Dessert", "gegen 20:00 Uhr"),
    (f"Eröffnung der Tanzfläche", "gegen 21:00 Uhr"),
    (f"Mitternachtssnack", "gegen 23:30 Uhr")
]

for event, time in events_day1:
    st.markdown(f'<div class="event"><b>{time}</b>: {event}</div>', unsafe_allow_html=True)

st.divider()

# --- Day 2 ---
#st.markdown(f'<h2 class="subtitle">Samstag, <b>{date2}</b> </h2>', unsafe_allow_html=True)

#events_day2 = [
#    (f"Frühstück im {location_name} Restaurant (für alle die wollen) - bitte Info geben", "09:00 bis 10:30 Uhr"),
#    (f"Check-Out", "bis 11:00 Uhr")
#]

#for event, time in events_day2:
#    st.markdown(f'<div class="event"><b>{time}</b>: {event}</div>', unsafe_allow_html=True)

#st.divider()

# --- Kontakt-Box ---
st.markdown(
    f"""
    <div class="contact-box">
        💡 Möchtet ihr einen Programmpunkt beisteuern? <br>
        Meldet euch gerne bei <b>{kontakt_name}</b> oder  unter {kontakt_telefon}
    </div>
    """, unsafe_allow_html=True)
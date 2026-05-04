import streamlit as st
import pandas as pd
from utils import decrypt_text
from views.data import ENCRYPTED_CONTENT

# Einleitung & Buchungsinfos
hotel_mail = decrypt_text(ENCRYPTED_CONTENT["mail_hotel"])
hotel_telefon = decrypt_text(ENCRYPTED_CONTENT["tele_hotel"])
location_name = decrypt_text(ENCRYPTED_CONTENT["location_name"])
couple_name = decrypt_text(ENCRYPTED_CONTENT["couple_name"])
hotel_name2 = decrypt_text(ENCRYPTED_CONTENT["hotel_name2"])
hotel_name3 = decrypt_text(ENCRYPTED_CONTENT["hotel_name3"])
hotel_name4 = decrypt_text(ENCRYPTED_CONTENT["hotel_name4"])
hotel_name5 = decrypt_text(ENCRYPTED_CONTENT["hotel_name5"])
hotel_name6 = decrypt_text(ENCRYPTED_CONTENT["hotel_name6"])

# 1. Page-spezifisches CSS
st.markdown(
    """
    <style>
        .subtitle {
            font-family: 'Playfair Display', serif;
            font-size: 28px;
            font-weight: bold;
            color: #3D2B1F;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .info-text {
            font-size: 18px;
            color: #3D2B1F;
            line-height: 1.6;
        }
        .contact-box {
            font-size: 18px;
            color: #3D2B1F;
            margin-top: 30px;
            padding: 20px;
            border: 1px dashed #3D2B1F;
            border-radius: 10px;
            text-align: center;
        }
        /* Styling für die Tabelle anpassen */
        .stDataFrame {
            border: 1px solid #3D2B1F;
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel (Nutzt die globale Klasse aus main.py)
st.markdown('<h1 class="serif-text">Unterkunft</h1>', unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="info-text">
        Direkt am <b>{location_name}</b> befindet sich das {location_name} Hotel, dieses hat jeweils 8 Economy und 10 Doppelzimmer, 
        die jeweils ein Doppelbett innehaben.<br>
        Wenn ihr ein Zimmer reservieren möchtet, meldet euch bitte direkt beim Stadtgut Hotel und schreibt eine Mail an 
        <b><a href="mailto:{hotel_mail}" style="color: #3D2B1F; font-weight: bold;">{hotel_mail}</a></b>
        mit dem Betreff „Hotelzimmerbuchung Hochzeit {couple_name}“. Hierbei gilt, nur so lange der Vorrat reicht! <br>
        Telefonisch erreicht ihr die Rezeption zwischen 9:00 Uhr und 18:00 Uhr unter der <b>{hotel_telefon}</b>.<br>
        Weiterhin sind mit einer ca. 10-minütigen Autofahrt auch folgende Hotels gut erreichbar: <br>
        {hotel_name2}<br>
        {hotel_name3}<br>
        {hotel_name4}<br>
        {hotel_name5}<br>
        {hotel_name6}<br>

        
        ??????????🐣 Kinderbetten gibt es auf Anfrage – gebt das einfach bei Eurer Buchung mit an?????????
    </div>
    """,
    unsafe_allow_html=True
)

# Zimmerkategorien Tabelle
#st.markdown('<h2 class="subtitle">Zimmerkategorien & Preise</h2>', unsafe_allow_html=True)

#zimmer_data = pd.DataFrame({
#    "Zimmerkategorie": ["Standard", "Komfort", "Premium", "Premium Plus", "Apartment"],
#    "Anzahl": [5, 7, 11, 2, 5],
#    "Preis (EZ / DZ, EUR)": ["99 / 129", "114 / 144", "134 / 164", "144 / 174", "154 / 184"],
#    "Max. Pers.": [2, 2, 2, 3, 5],
#    "Aufpreis Aufbettung": ["-", "-", "-", "30", "30"],
#    "Lage": [
#        "1. OG Vorderhaus", "Haupthaus", "1. OG Vorderhaus", "1. OG Vorderhaus", "Nebengebäude"
#    ]
#})

# Anzeige der Tabelle
#st.dataframe(zimmer_data, hide_index=True, use_container_width=True)

# Kontakt-Abschlussbox
st.markdown(
    """
    <div class="contact-box">
        Falls ihr Fragen zur Unterkunft habt oder Hilfe bei der Buchung braucht, <br>
        meldet euch gerne jederzeit bei uns! 🤍
    </div>
    """,
    unsafe_allow_html=True
)
import streamlit as st
import pandas as pd
from utils import decrypt_text
from views.data import ENCRYPTED_CONTENT

# Einleitung & Buchungsinfos
hotel_mail = decrypt_text(ENCRYPTED_CONTENT["mail_hotel"])
hotel_telefon = decrypt_text(ENCRYPTED_CONTENT["tele_hotel"])
location_name = decrypt_text(ENCRYPTED_CONTENT["location_name"])
link_location = decrypt_text(ENCRYPTED_CONTENT["link_location"])
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
            color: #2E4053;
            margin-top: 25px;
        }
        .info-text {
            font-size: 18px;
            color: #2E4053;
            line-height: 1.6;
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
        /* Styling für die Tabelle anpassen */
        .stDataFrame {
            border: 1px solid #2E4053;
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
        Direkt am <b>{location_name}</b> befindet sich das {location_name} Hotel. Dieses hat 18 Zimmer, die jeweils ein Doppelbett innehaben. 
        Das Hotel ist leider nicht barrierefrei. Haustiere sind nicht erlaubt. 
        Weitere Informationen zu den Zimmern und zum Hotel findet ihr unter 
        <a href="{link_location}" target="_blank" style="color: #2E4053; font-weight: bold;">{link_location}</a>.<br><br>
        Zimmerreservierungen sind voraussichtlich ab <b>Ende Juni 2026</b> möglich. Wenn ihr ein Zimmer reservieren möchtet, 
        meldet euch bitte direkt beim Stadtgut Hotel und schreibt eine Mail an 
        <b><a href="mailto:{hotel_mail}" style="color: #2E4053; font-weight: bold;">{hotel_mail}</a></b>
        mit dem Betreff „Hotelzimmerbuchung Hochzeit {couple_name}“ und der Angabe von Namen, Anschrift und Geburtsdaten.
        Die Buchung der Hotelzimmer erfolgt auf eigene Kosten, das Kontigent wird aktuell nur geblockt. <br>
        <br>
        Telefonisch erreicht ihr die Rezeption zwischen 9:00 Uhr und 18:00 Uhr unter der <b>{hotel_telefon}</b>.<br>
        🐣 Ein Babybett kann für 10 EUR pro Nacht dazugebucht werden. Gebt das einfach bei der Buchung mit an.<br>
        <br>
        Weiterhin sind mit einer ca. 10-minütigen Autofahrt auch folgende Hotels gut erreichbar: <br>
        <ul style="margin-top: 10px; padding-left: 40px; list-style-type: disc;">
            <li>{hotel_name2}</li>
            <li>{hotel_name3}</li>
            <li>{hotel_name4}</li>
            <li>{hotel_name5}</li>
            <li>{hotel_name6}</li>
        </ul>
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
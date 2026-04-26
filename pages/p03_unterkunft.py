from navigation import make_sidebar, collapse_sidebar
import streamlit as st
import pandas as pd

make_sidebar()

st.markdown(
    """
    <style>
        body {
            background-color: #F5F3FF;
            color: #4A3B5C;
            font-family: serif;
        }
        .title {
            color: #D1C4E9;
            font-size: 36px;
            font-weight: bold;
            text-align: left;
        }
        .subtitle {
            font-size: 24px;
            font-weight: bold;
            color: #6A4CA8;
            margin-top: 20px;
            text-align: left;
        }
        .text {
            font-size: 18px;
            text-align: left;
        }
        .contact {
            font-size: 18px;
            font-weight: bold;
            color: #4A3B5C;
            text-align: left;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel
st.markdown('<h1 class="title">Unterkunft</h1>', unsafe_allow_html=True)

# Einleitung
st.markdown(
    """
    <p class="text">
        Das folgende Zimmerkontingent ist für Euch bis zum <b>15.04.2025</b> reserviert. <br>
        Wenn ihr ein Zimmer buchen möchtet, meldet euch bei der <b>Alten Scheune</b> unter
        <a href="mailto:reservierung@alte-scheune.de">reservierung@alte-scheune.de</a>, um die Verfügbarkeiten abzufragen. <br><br>
        <b>Bitte gebt als Betreff:</b> "Hotelzimmerbuchung Hochzeit Neda & Peter" an.<br><br>
        Kinderbetten gibt es auf Anfrage – gebt das bitte in Eurer Anfrage an.
    </p>
    """,
    unsafe_allow_html=True
)

# Zimmerkategorien Tabelle
st.markdown('<h2 class="subtitle">Zimmerkategorien & Preise</h2>', unsafe_allow_html=True)

zimmer_data = pd.DataFrame({
    "Zimmerkategorie": ["Standard", "Komfort", "Premium", "Premium Plus", "Apartment"],
    "Anzahl": [5, 7, 11, 2, 5],
    "Preis (Einzel/Doppel, EUR)": ["99 / 129", "114 / 144", "134 / 164", "144 / 174", "154 / 184"],
    "Max. Kapazität": [2, 2, 2, 3, 5],
    "Aufpreis weitere Person": ["-", "-", "-", "30", "30"],
    "Lage": [
        "1. OG Vorderhaus", "-", "1. OG Vorderhaus", "1. OG Vorderhaus", "1. & 2. OG Nebengebäude"
    ]
})

st.dataframe(zimmer_data, hide_index=True, use_container_width=True)

# Kontaktinfo
st.markdown(
    """
    <p class="contact">
        🐣 Falls ihr Fragen habt, meldet euch gerne bei uns oder direkt bei der Alten Scheune 🐣
    </p>
    """,
    unsafe_allow_html=True
)
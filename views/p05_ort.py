import streamlit as st
from utils import load_decrypted_image, decrypt_text
from views.data import ENCRYPTED_CONTENT

adresse = decrypt_text(ENCRYPTED_CONTENT["adresse_kirche"])
st.write(f"Unsere Location: **{adresse}**")
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
            margin-bottom: 20px;
        }
        .contact {
            font-size: 20px;
            font-weight: bold;
            color: #4A3B5C;
            text-align: left;
            margin-top: 30px;
        }
        iframe {
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel
st.markdown('<h1 class="title">Anfahrt & Parken</h1>', unsafe_allow_html=True)

# Adresse
st.markdown('<h2 class="subtitle">📍 Adresse</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="text">
        Das Landhaus Alte Scheune findet ihr hier: <br>
        <b>Alt Erlenbach 44</b> <br>
        60437 Frankfurt / Nieder-Erlenbach
    </p>
    """,
    unsafe_allow_html=True
)

# Maps
st.markdown('<h2 class="subtitle">🗺️ Google Maps</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2517.089015978859!2d8.688071076252917!3d50.19111787142224!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47bdbbaea377b0a9%3A0x748b94ec3b93562c!2sAlt%20Erlenbach%2044%2C%2060437%20Frankfurt%20am%20Main!5e0!3m2!1sen!2sde!4v1706807000000"
        width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy">
    </iframe>
    """,
    unsafe_allow_html=True
)

# Öffentliche Verkehrsmittel
st.markdown('<h2 class="subtitle">🚆 Anfahrt mit den öffentlichen Verkehrsmitteln</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <ul class="text">
        <li><b>S6</b> bis Berkersheim Bahnhof</li>
        <li><b>Bus 25</b> bis Frankfurt (Main) Rathaus Nieder-Erlenbach</li>
    </ul>
    <p class="text">
        Ab der Bushaltestelle sind es nur <b>43m oder 1 Minute zu Fuß</b> zum Landhaus Alte Scheune.
    </p>
    """,
    unsafe_allow_html=True
)

# Anfahrt mit dem Auto
st.markdown('<h2 class="subtitle">🚗 Anfahrt mit dem Auto</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="text">
        Leider gibt es <b>keine Parkplätze</b> direkt am Landhaus Alte Scheune. <br>
        Hier könnt ihr stattdessen parken:
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="menu-section">🅿️ Bürgerhaus (Schotterplatz)</p>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="text">
        <b>Adresse:</b>
        **{adresse}** <br>
        Vom Parkplatz aus sind es <b>350m oder 5 Minuten zu Fuß</b> zum Landhaus Alte Scheune.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="text">
        In der Umgebung gibt es zudem weitere Parkmöglichkeiten.
    </p>
    """,
    unsafe_allow_html=True
)
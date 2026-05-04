import streamlit as st
from utils import load_decrypted_image, decrypt_text
from views.data import ENCRYPTED_CONTENT

google_maps_link = decrypt_text(ENCRYPTED_CONTENT["google_maps_link"])
location_name = decrypt_text(ENCRYPTED_CONTENT["location_name"])
adresse_location = decrypt_text(ENCRYPTED_CONTENT["adresse_location"])

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
    f"""
    <p class="text">
        Das {location_name} findet ihr hier: <br>
        <b> {adresse_location}</b> <br>
    </p>
    """,
    unsafe_allow_html=True
)

# Maps
st.markdown('<h2 class="subtitle">🗺️ Google Maps</h2>', unsafe_allow_html=True)

st.markdown(
    f"""
    <iframe
        src={google_maps_link}
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
        <li> Mit der <b>S2</b> könnt ihr bis zum S Bahnhof Buch fahren. </li>
        <li> Dann nochmal ca. 10-12 Minuten – je nach Schritttempo – laufen.</li>
    </ul>

    """,
    unsafe_allow_html=True
)

# Anfahrt mit dem Auto
st.markdown('<h2 class="subtitle">🚗 Anfahrt mit dem Auto</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="text">
        Es gibt mehr als genug Parkplätze direkt vor der Location. Schaut euch das genau auf dem Lageplan an.
    </p>
    """,
    unsafe_allow_html=True
)

# picture
st.markdown('<h2 class="subtitle">🗺️ Lageplan</h2>', unsafe_allow_html=True)
img_data = load_decrypted_image("assets/Lageplan.bin")
st.image(img_data)

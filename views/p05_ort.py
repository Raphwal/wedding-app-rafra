import streamlit as st
from utils import load_decrypted_image, decrypt_text
from views.data import ENCRYPTED_CONTENT

google_maps_link = decrypt_text(ENCRYPTED_CONTENT["google_maps_link"])
location_name = decrypt_text(ENCRYPTED_CONTENT["location_name"])
adresse_location = decrypt_text(ENCRYPTED_CONTENT["adresse_location"])

st.markdown(
    """
<style>
        /* 1. Titel & Überschriften im neuen Blau */
        .title {
            font-family: 'Playfair Display', serif;
            color: #2E4053;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-family: 'Playfair Display', serif;
            font-size: 26px;
            font-weight: bold;
            color: #2E4053;
            margin-top: 25px;
            text-align: left;
        }

        /* 2. Fließtext */
        .text {
            font-size: 18px;
            color: #2E4053;
            text-align: left;
            line-height: 1.6;
            margin-bottom: 20px;
            /* Optional: Leichter weißer Hintergrund für bessere Lesbarkeit über Blumen */
            background-color: rgba(255, 255, 255, 0.2);
            padding: 10px;
            border-radius: 8px;
        }

        /* 3. Die Kontakt-Box (Dashed Design passend zum Rest) */
        .contact-box {
            font-size: 18px;
            color: #2E4053;
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.6);
            border: 2px dashed #2E4053;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(46, 64, 83, 0.1);
        }

        /* 4. iFrames (z.B. Google Forms oder Maps) */
        iframe {
            border: 2px solid #2E4053 !important;
            border-radius: 15px !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
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
st.image(img_data, use_container_width=True)

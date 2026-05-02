import streamlit as st
import streamlit.components.v1 as components
from utils import load_decrypted_image, decrypt_text
from views.data import ENCRYPTED_CONTENT

forms_url = decrypt_text(ENCRYPTED_CONTENT["forms_url"])
location_name = decrypt_text(ENCRYPTED_CONTENT["location_name"])
adresse_location = decrypt_text(ENCRYPTED_CONTENT["adresse_location"])
link_location = decrypt_text(ENCRYPTED_CONTENT["link_location"])
couple_name = decrypt_text(ENCRYPTED_CONTENT["couple_name"])
date1 = decrypt_text(ENCRYPTED_CONTENT["date1"])
location_name = decrypt_text(ENCRYPTED_CONTENT["location_name"])

# picture
img_data = load_decrypted_image("assets/Hochzeit_teaser.bin")
st.image(img_data, caption="Foto aus Straßburg")

st.markdown(f"""
## Liebe Gäste,
wir freuen uns, am **{date1}** mit euch im {location_name} ({link_location}) unsere Hochzeit zu feiern!
Alle wichtigen Informationen haben wir hier zusammengestellt. Damit auch wir die beste Feier für euch planen können, bitten wir euch bis spätestens zum **31.12.2026** eure Rückmeldungen über folgendes [Google Formular]({forms_url}) zu geben.
Wir haben das Formular auch für euch eingebettet.

Solltet ihr versehentlich eine falsche Angabe gemacht haben, füllt das Formular einfach erneut aus. Wir werten die jüngste Rückmeldung aus.

**Liebe Grüße**<br>
{couple_name}
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
### Rückmeldeformular
""")

components.html(f"""
   <style>
        .responsive-iframe-container {{
            position: relative;
            width: 100%;
            height: 0;
            padding-bottom: 160%; /* Etwas mehr Platz für das Formular */
            overflow: hidden;
            background-color: transparent;
        }}
        .responsive-iframe-container iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            /* Rahmenfarbe auf dein Dunkelbraun angepasst */
            border: 2px solid #3D2B1F; 
            border-radius: 15px;
            /* Ein weicher Schatten lässt das Formular auf dem Papier "liegen" */
            box-shadow: 0 4px 12px rgba(61, 43, 31, 0.15);
        }}
    </style>

    <div class="responsive-iframe-container">
        <iframe
            src="{forms_url}"
            frameborder="0"
            marginheight="0"
            marginwidth="0">
            Lade Formular...
        </iframe>
    </div>
    """,
    height=1000, 
)

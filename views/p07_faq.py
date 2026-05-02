import streamlit as st
from utils import decrypt_text
from views.data import ENCRYPTED_CONTENT

# 1. Page-spezifisches CSS
st.markdown(
    """
    <style>
        .subtitle {
            font-family: 'Playfair Display', serif;
            font-size: 28px;
            font-weight: bold;
            color: #3D2B1F;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        /* Styling für die Expander (FAQ-Boxen) */
        .stExpander {
            background-color: rgba(61, 43, 31, 0.03);
            border: 1px solid rgba(61, 43, 31, 0.1);
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .stExpander p {
            color: #3D2B1F;
            font-size: 17px;
        }
        .contact-box {
            font-size: 18px;
            color: #3D2B1F;
            margin-top: 40px;
            padding: 20px;
            border: 1px dashed #3D2B1F;
            border-radius: 10px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel (Nutzt die globale Klasse aus main.py)
st.markdown('<h1 class="serif-text">FAQs</h1>', unsafe_allow_html=True)

st.markdown('<h2 class="subtitle">💡 Häufige Fragen</h2>', unsafe_allow_html=True)

# Daten entschlüsseln
kontakt_person = decrypt_text(ENCRYPTED_CONTENT["name_ansprechpartner"]) # z.B. "Eric Hensel"

# --- FAQ Einträge ---

with st.expander("🎁 Was dürfen wir euch schenken?"):
    st.write("Wir nehmen gerne Geldgeschenke an, da dies eine schöne Tradition in unseren elterlichen Kulturen ist.")

with st.expander("👔 Gibt es einen Dresscode?"):
    st.write("Werft Euch in tanzbare Schale – wir wollen mit euch feiern und das Parkett glühen lassen!")

with st.expander("🍷 Kann ich auch andere Getränke bekommen?"):
    st.write("Ja, alles außerhalb unserer Getränkekarte kann auf eigene Rechnung an der Bar bestellt werden. Kartenzahlung ist vor Ort möglich.")

with st.expander("🛏️ Gibt es Kinderbetten im Hotel?"):
    st.write("Ja, auf Anfrage. Bitte gebt direkt bei eurer Buchungsanfrage im Landhaus an, ob ihr ein Kinder- oder Beistellbett benötigt.")

with st.expander("🤱 Gibt es ein Stillzimmer?"):
    st.write(f"Ja, ein Raum hinter dem Bankettraum steht zur Verfügung. Bitte wendet euch vor Ort einfach an **{kontakt_person}**.")

with st.expander("👶 Wo finden wir einen Wickeltisch?"):
    st.write(f"Ein Wickeltisch befindet sich in der Herrentoilette am Bankettbereich. Bei Fragen hilft euch **{kontakt_person}** gerne weiter.")

# --- Abschluss Kontakt ---
st.markdown(
    """
    <div class="contact-box">
        ❓ Noch Fragen offen? <br>
        Schreibt uns einfach eine Nachricht auf <b>WhatsApp</b> oder ruft uns an!
    </div>
    """,
    unsafe_allow_html=True
)
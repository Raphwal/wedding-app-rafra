import streamlit as st
from utils import load_decrypted_image, decrypt_text, crop_image_top_bottom
from views.data import ENCRYPTED_CONTENT

# Daten entschlüsseln
kontakt_name_f = decrypt_text(ENCRYPTED_CONTENT["name_trauzeugin"])
tele_trauzeugin = decrypt_text(ENCRYPTED_CONTENT["tele_trauzeugin"])
kontakt_name_m = decrypt_text(ENCRYPTED_CONTENT["name_trauzeuge"])
tele_trauzeuge = decrypt_text(ENCRYPTED_CONTENT["tele_trauzeuge"])
forms_url = decrypt_text(ENCRYPTED_CONTENT["forms_url"])

img_data1 = load_decrypted_image("assets/cat.bin")
img_data2 = load_decrypted_image("assets/herz.bin")

img_data1 = crop_image_top_bottom(img_data1, top_percent=35, bottom_percent=15)


# 1. Page-spezifisches CSS
st.markdown(
    """
    <style>
        /* 1. Untertitel in Schieferblau */
        .subtitle {
            font-family: 'Playfair Display', serif;
            font-size: 28px;
            font-weight: bold;
            color: #2E4053;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        /* 2. Styling für die Expander (FAQ-Boxen) */
        /* Wir nutzen ein helles Weiß-Blau, damit sie über den Blumen schweben */
        .stExpander {
            background-color: rgba(255, 255, 255, 0.4); 
            border: 1px solid rgba(46, 64, 83, 0.1);
            margin-bottom: 10px;
            border-radius: 10px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        }

        /* Text innerhalb der Expander */
        .stExpander p {
            color: #2E4053;
            font-size: 17px;
        }

        /* 3. Die Kontakt-Box (Dashed & Clean) */
        .contact-box {
            font-size: 18px;
            color: #2E4053;
            margin-top: 40px;
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

# Titel (Nutzt die globale Klasse aus main.py)
st.markdown('<h1 class="serif-text">FAQs</h1>', unsafe_allow_html=True)

st.markdown('<h2 class="subtitle">💡 Häufige Fragen</h2>', unsafe_allow_html=True)

# --- FAQ Einträge ---

# --- FAQ Vor der Hochzeit ---
st.markdown('<h3 class="subtitle">Vor der Hochzeit</h3>', unsafe_allow_html=True)

with st.expander("👔 Gibt es einen Dresscode?"):
    st.write("Kommt auf jeden Fall so, dass ihr euch richtig wohlfühlt (Lasst die Jogginghose jedoch ruhig einen Abend Netflix-Pause machen). " \
    "Ein bisschen schicker darf es sein, ohne dass ihr euch verkleidet fühlt. Und wenn ihr später auf der Tanzfläche in „Party-Modus-Komfort“ " \
    "wechseln möchtet, packt euch gern etwas Bequemes zum Umziehen ein.")

with st.expander("🎁 Was dürfen wir euch schenken?"):
    st.write("Das größte Geschenk ist natürlich, dass ihr mit uns feiert. Wer uns darüber hinaus etwas Gutes tun möchte: " \
    "Wir freuen uns sehr über einen Beitrag zu unserem gemeinsamen Start ins Eheleben. ")

with st.expander("👶 Sind Kinder eingeladen?"):
    st.write("Ja, eure Kinder sind auf der Hochzeit herzlich willkommen.")

with st.expander("🛏️ Gibt es Kinderbetten im Hotel?"):
    st.write("Ja, ein Babybett kann für 10 EUR pro Nacht bereitgestellt werden und für Gäste ab 5 Jahren kann eine Aufbettung für 20 EUR pro Nacht gestellt werden. Bitte gebt das bei der Buchung mit an.")

with st.expander("🐶 Dürfen Haustiere mitgebracht werden?"):
    st.write("Vierbeinige Gäste (auch Achtbeinige) müssen leider draußen bleiben. Das gilt leider auch für Filou, der sicherlich auch wahnsinnig gern in der Menschenmenge verschwunden wäre. " \
    "Wir hoffen ein paar extra Leckerlis können die Situation lösen und bitten um euer Verständnis.  ")
    st.image(img_data1, caption="Echt jetzt?", use_container_width=True)
with st.expander("🎶 Können wir uns auch Songs wünschen? "):
    st.markdown(f"""Ihr habt einen Lieblingssong, der unbedingt auf die Tanzfläche muss? Sehr gern! Tragt eure Musikwünsche einfach im [Google Formular]({forms_url}) ein. 
                (Es gibt keine Garantie, dass alle Wünsche erfüllt werden können, aber wir geben unser Bestes 😉)
                """, unsafe_allow_html=True)

with st.expander("🎲 Sind Spiele und Aktionen erlaubt?"):
    st.write("Wenn ihr eine Überraschung, ein Spiel oder eine kleine Aktion für die Hochzeit plant stimmt euch bitte einmal kurz mit unseren " \
    f"Trauzeugen **{kontakt_name_m}** oder **{kontakt_name_f}** ab, damit alles gut zusammenpasst und niemand doppelt organisiert. ")

with st.expander("👯 Wie groß wird die Feier sein?"):
    st.write("Wir planen mit ca. 60 Personen.")

# --- FAQ Während der Hochzeit ---
st.markdown('<h3 class="subtitle">Während der Hochzeit</h3>', unsafe_allow_html=True)
with st.expander("⛈️ Was passiert bei schlechtem Wetter?"):
    st.write("Keine Sorge, es muss niemand im Regen stehen, es gibt einen trockenen Plan B.")
    st.image(img_data2, caption="Wir machen das beste draus!", use_container_width=True)

with st.expander("🎊 Dürfen Blumen/Konfetti oder ähnliches gestreut werden?"):
    st.write("Bitte nicht! Sowohl das streuen von Blüten, Konfetti als auch Reis im Innen- und Außenbereich sind nicht erlaubt und wird für uns teuer. ")

with st.expander("📸 Können wir Fotos hochladen? "):
    st.write("Ihr könnt eure Fotos, die ihr während der Hochzeit oder auch in Vorbereitung zur Hochzeit macht und gern auf Everlense hochladen. " \
    "Den Link hierzu laden wir ca. zwei Monate vor der Hochzeit auf die Seite. ")

#with st.expander("🤱 Gibt es ein Stillzimmer?"):
#    st.write(f"+Ja, ein Raum hinter dem Bankettraum steht zur Verfügung. Bitte wendet euch vor Ort einfach an **{kontakt_name_m}**.")

with st.expander("👶 Wo finden wir einen Wickeltisch?"):
    st.write(f"Ein Wickeltisch befindet sich in der Damentoilette. Bei Fragen hilft euch **{kontakt_name_m}** sehr gerne weiter.")

with st.expander("🍷 Kann ich auch andere Getränke bekommen?"):
    st.write("Ja, alles außerhalb unserer Getränkekarte kann auf eigene Rechnung an der Bar bestellt werden. Zahlung dann direkt in bar.")

# --- Abschluss Kontakt ---
st.markdown(
    f"""
    <div class="contact-box">
        ❓ Noch Fragen offen? <br>
        Bitte wendet euch an unsere kompetenten Trauzeugen <b>{kontakt_name_f}</b> unter der <b>{tele_trauzeugin}</b> oder <b>{kontakt_name_m}</b> unter <b>{tele_trauzeuge}</b>.
    </div>
    """,
    unsafe_allow_html=True
)
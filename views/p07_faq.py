import streamlit as st
from utils import load_decrypted_image, decrypt_text, crop_image_top_bottom
from views.data import ENCRYPTED_CONTENT

# Daten entschlüsseln
kontakt_name_f = decrypt_text(ENCRYPTED_CONTENT["name_trauzeugin"])
tele_trauzeugin = decrypt_text(ENCRYPTED_CONTENT["tele_trauzeugin"])
kontakt_name_m = decrypt_text(ENCRYPTED_CONTENT["name_trauzeuge"])
tele_trauzeuge = decrypt_text(ENCRYPTED_CONTENT["tele_trauzeuge"])
forms_url = decrypt_text(ENCRYPTED_CONTENT["forms_url"])
date1 = decrypt_text(ENCRYPTED_CONTENT["date1"])
date3 = decrypt_text(ENCRYPTED_CONTENT["date3"])
couple_family_name = decrypt_text(ENCRYPTED_CONTENT["couple_family_name"])

img_data1 = load_decrypted_image("assets/cat.bin")
img_data2 = load_decrypted_image("assets/herz.bin")

img_data1 = crop_image_top_bottom(img_data1, top_percent=35, bottom_percent=15)


# 1. Page-spezifisches CSS
st.markdown(
    """
    <style>
        /* 1. Die Untertitel */
        .subtitle {
            font-family: 'Playfair Display', serif;
            font-size: 28px;
            font-weight: bold;
            color: #2E4053;
            margin-top: 20px;
        }

        /* 2. DER GROSSE FAQ-BOX-FIX */
        
        /* Weißer Kasten für JEDEN Expander (verhindert das Verschwinden bei Bildern) */
        div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stExpander"]) {
            background-color: rgba(255, 255, 255, 0.15) !important;
            padding: 0px !important; /* Padding wird im Expander-Inhalt geregelt */
            border-radius: 15px !important;
            margin-bottom: 15px !important;
            box-sizing: border-box !important;
        }

        /* Expander-Hülle transparent machen */
        .stExpander {
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }

        /* DER ENTSCHEIDENDE TEIL: Padding für den Inhalt */
        /* Wir geben dem Inhaltsbereich (Details) ein festes Padding. 
           Das drückt Text UND Bild gleichmäßig vom Rand weg. */
        div[data-testid="stExpanderDetails"] {
            padding-left: 20px !important;
            padding-right: 20px !important;
            padding-bottom: 20px !important;
            padding-top: 0px !important;
        }

        /* Alle inneren Boxen (besonders die für Bilder) im Expander neutralisieren */
        div[data-testid="stExpanderDetails"] [data-testid="stVerticalBlock"] > div {
            background-color: transparent !important;
            padding: 0px !important;
            margin: 0px !important;
            box-shadow: none !important;
        }

        /* 3. SCHRIFT-ANPASSUNG (Standard 18px wie in der Main) */
        .stExpander p, .stExpander li, .stExpander span {
            color: #2E4053 !important;
            font-size: 18px !important; /* Hier auf deinen Standard angepasst */
            line-height: 1.6 !important;
        }
        
        /* Die Überschrift des Expanders (Frage) ebenfalls anpassen */
        .stExpander summary p {
            font-size: 19px !important; 
            font-weight: bold !important;
        }

        /* 4. KONTAKT-BOX */
        .contact-box {
            font-size: 18px;
            color: #2E4053;
            margin-top: 40px;
            padding: 25px;
            background-color: rgba(255, 255, 255, 0.6);
            border: 2px dashed #2E4053;
            border-radius: 15px;
            text-align: center;
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
    "Ein bisschen schicker darf es sein, ohne dass ihr euch verkleidet fühlt. Und wenn ihr später auf der Tanzfläche in den „Party-Modus-Komfort“ " \
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
    f"Trauzeugen **{kontakt_name_m}** ({tele_trauzeuge}) oder **{kontakt_name_f}** ({tele_trauzeugin}) ab, damit alles gut zusammenpasst und niemand doppelt organisiert. ")

with st.expander("👯 Wie groß wird die Feier sein?"):
    st.write("Wir planen mit ca. 60 Personen.")

with st.expander(f"💒  Findet am {date1} auch die standesamtliche Trauung statt?"):
    st.write(f"Nein, die standesamtliche Trauung findet im {date3} im kleinen Kreis statt. Wir sind von da an offiziell Familie {couple_family_name}. "\
             f"Am {date1} findet unsere freie Trauung statt. Wir freuen uns, unseren Hochzeitstag gemeinsam mit euch in großer Runde zu feiern! "
)

# --- FAQ Während der Hochzeit ---
st.markdown('<h3 class="subtitle">Während der Hochzeit</h3>', unsafe_allow_html=True)
with st.expander("⛈️ Was passiert bei schlechtem Wetter?"):
    st.write("Keine Sorge, es muss niemand im Regen stehen, es gibt einen trockenen Plan B.")
    st.image(img_data2, caption="Wir machen das beste draus!", use_container_width=True)

with st.expander("🎊 Dürfen Blumen/Konfetti oder ähnliches gestreut werden?"):
    st.write("Bitte nicht! Sowohl das Streuen von Blüten, Konfetti als auch Reis im Innen- und Außenbereich sind nicht erlaubt und wird für uns teuer. ")

with st.expander("📸 Können wir Fotos hochladen? "):
    st.write("Ihr könnt eure Fotos, die ihr während der Hochzeit oder auch in Vorbereitung zur Hochzeit macht, gern auf Everlense hochladen. " \
    " Den Link zu Everlense findet ihr ca. 2 Monate vor der Hochzeit auf der Seite. ")

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
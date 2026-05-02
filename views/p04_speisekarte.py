import streamlit as st
from utils import decrypt_text
from views.data import ENCRYPTED_CONTENT

# 1. Page-spezifisches CSS
st.markdown(
    """
    <style>
        .subtitle {
            font-family: 'Playfair Display', serif;
            font-size: 30px;
            font-weight: bold;
            color: #3D2B1F;
            margin-top: 35px;
            border-bottom: 1px solid #3D2B1F;
            padding-bottom: 5px;
        }
        .menu-section {
            font-family: 'Playfair Display', serif;
            font-size: 22px;
            font-weight: bold;
            color: #3D2B1F;
            margin-top: 25px;
            margin-bottom: 10px;
            font-style: italic;
        }
        .info-text {
            font-size: 18px;
            color: #3D2B1F;
            font-style: italic;
            text-align: center;
            padding: 10px;
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
        /* Styling für die Markdown-Listen */
        .stMarkdown ul {
            color: #3D2B1F;
            font-size: 18px;
            list-style-type: "◦ ";
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel
st.markdown('<h1 class="serif-text">Speisekarte</h1>', unsafe_allow_html=True)

# Einleitung
st.markdown(
    """
    <div class="info-text">
        Folgende Getränke sind für euch inklusive! Getränke darüber hinaus können auf eigene Rechnung
        an der (sehr gut sortierten) Bar bestellt werden.
    </div>
    """,
    unsafe_allow_html=True
)

# --- EMPFANG ---
st.markdown('<h2 class="subtitle">Empfang ab 16:00 Uhr</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="menu-section">🍹 Getränke</p>', unsafe_allow_html=True)
    st.markdown("""
    * Prosecco / alkoholfrei
    * Wasser (still & medium)
    * Holunderblütensirup
    * Orangensaft
    """)

with col2:
    st.markdown('<p class="menu-section">🥪 Fingerfood</p>', unsafe_allow_html=True)
    st.markdown("""
    * Canapé à la Bruschetta
    * Canapé mit Spinat & Feta
    * Wraps mit Avocado & Räucherlachs
    """)

# --- GETRÄNKE ---
st.markdown('<h2 class="subtitle">Getränke ab 17:30 Uhr</h2>', unsafe_allow_html=True)

st.markdown("""
* Wasser (still & medium)
* Verschiedene Softdrinks
* Frische Säfte aus der Wetterau
* Heißgetränke & Kaffeespezialitäten
""")

st.markdown('<p class="menu-section">🍷 Weine & Bier</p>', unsafe_allow_html=True)
st.markdown("""
* **Weiß**: Sauvignon Blanc, Grauburgunder oder Muskateller (Fam. Pfaffmann)
* **Schorle**: Die klassische Weißweinschorle
* **Rot**: Vollmundiger Tempranillo
* **Bier**: Ayinger vom Fass (Helles & Weizen), alkoholfreie Varianten aus der Flasche
* **Lokal**: Ebbelwoi (pur, süß oder sauer gespritzt)
""")

# --- BUFFET ---
st.markdown('<h2 class="subtitle">Grillbuffet ab 18:00 Uhr</h2>', unsafe_allow_html=True)

st.markdown('<p class="menu-section">🥗 Salate & Beilagen</p>', unsafe_allow_html=True)
st.markdown("""
* Römersalat - B o h n e n , R a d i e s c h e n , K a r o t t e n , F r ü h l i n g s l a u c h ,
P a l m e n h e r z e n , u n d A v o c a d o i n W a s a b i D r e s s i n g
* Caprese & klassischer Gurkensalat
* Mediterraner Spaghettisalat & Antipasti
* Kartoffelsalat mit Zwiebeln & Krautsalat
* Ofenkartoffeln mit Sour Cream & Brezelcher mit Spundekäs
""")

st.markdown('<p class="menu-section">🔥 Vom Grill</p>', unsafe_allow_html=True)
st.markdown("""
* Entrecôte & Schweinerollbraten (Idarer Art)
* Lammrückenspieße & feine Hähnchenspieße
* Saftiges Lachsfilet
* Gegrillter Fetakäse
""")

st.markdown('<p class="menu-section">🍰 Desserts</p>', unsafe_allow_html=True)
st.markdown("""
* Mousse au Chocolat
* Erfrischende Sorbets
* Klassische Crème brûlée
* Platte mit frischen Früchten der Saison
""")

# Abschluss
st.divider()
st.markdown('<p class="serif-text" style="font-size: 24px;">Bon Appétit!</p>', unsafe_allow_html=True)

# Kontakt-Abschlussbox
st.markdown(
    """
    <div class="contact-box">
        Falls ihr Fragen zum Essen haben (bspw. Allergene), meldet euch gerne jederzeit bei uns! 🤍
    </div>
    """,
    unsafe_allow_html=True
)
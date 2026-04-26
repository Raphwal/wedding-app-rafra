from navigation import make_sidebar, collapse_sidebar
import streamlit as st

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
            margin-bottom: 20px;
        }
        .menu-section {
            font-size: 20px;
            font-weight: bold;
            color: #6A4CA8;
            margin-top: 30px;
        }
        .menu-item {
            font-size: 18px;
            margin-left: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel
st.markdown('<h1 class="title">Speisekarte</h1>', unsafe_allow_html=True)

# Einleitung
st.markdown(
    """
    <p class="text">
        Folgende Getränke sind für euch inklusive! Getränke darüber hinaus können auf eigene Rechnung
        an der (sehr gut sortierten) Bar bestellt werden.
    </p>
    """,
    unsafe_allow_html=True
)

# Empfang
st.divider()
st.markdown('<h2 class="subtitle">Empfang ab 16:00 Uhr</h2>', unsafe_allow_html=True)

st.markdown('<p class="menu-section">🍹 Getränke</p>', unsafe_allow_html=True)
st.markdown("""
- Prosecco
- Prosecco (alkoholfrei)
- Wasser (still & medium)
- Holunderblütensirup
- Orangensaft
""")

st.markdown('<p class="menu-section">🥪 Fingerfood</p>', unsafe_allow_html=True)
st.markdown("""
- Canapé à la Bruschetta
- Canapé mit Spinat & Feta
- Wraps mit Avocado & Räucherlachs
""")

# Getränke ab 17:30Uhr
st.divider()
st.markdown('<h2 class="subtitle">Getränke ab 17:30 Uhr</h2>', unsafe_allow_html=True)

st.markdown("""
- Wasser (still & medium)
- Softdrinks
- Frische Säfte aus der Wetterau
- Heißgetränke & Kaffeespezialitäten
""")

st.markdown('<p class="menu-section">🍷 Weine & Bier</p>', unsafe_allow_html=True)
st.markdown("""
- 'Pälzische Woie' der Familie Pfaffmann (Sauvignon Blanc / Grauburgunder / Muskateller)
- Schoppe (Weißweinschorle)
- Rotwein (Tempranillo)
- Ayinger Bier (Helles & Weizenbier vom Fass / alkoholfreies Pils & Weizenbier aus der Flasche)
- Ebbelwoi (pur / süß / sauer)
""")

# Buffet ab 18:00Uhr
st.divider()
st.markdown('<h2 class="subtitle">Buffet ab 18:00 Uhr</h2>', unsafe_allow_html=True)

st.markdown('<p class="menu-section">🥗 Salate & Beilagen</p>', unsafe_allow_html=True)
st.markdown("""
- Blattsalate & Rohkostsalate (div. Dressings)
- Gurkensalat mit Joghurtdressing
- Caprese (Tomate & Mozzarella)
- Antipasti (vegetarisch)
- Mediterraner Spaghettisalat (vegetarisch)
- Kartoffelsalat mit Zwiebeln (vegetarisch)
- Krautsalat
- Spundekäs mit Brezelcher
- Ofenkartoffeln mit Sour Cream
""")

st.markdown('<p class="menu-section">🔥 Grillbuffet</p>', unsafe_allow_html=True)
st.markdown("""
- Entrecôte idarer Art
- Lammrückenspieße
- Hähnchenspieße
- Lachsfilet
- Schweinerollbraten idarer Art
- Fetakäse vom Grill
""")

st.markdown('<p class="menu-section">🍰 Desserts</p>', unsafe_allow_html=True)
st.markdown("""
- Mousse au Chocolat
- Verschiedene Sorbets
- Crème brûlée
- Obstplatte mit frischen Früchten
""")

# Schluss
st.markdown(
    """
    <p class="text">
        Bon Appétit!
    </p>
    """,
    unsafe_allow_html=True
)
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
        an der (sehr gut sortierten) Bar bestellt werden. Die Bezahlung muss dann direkt an der Bar in bar erfolgen.
    </div>
    """,
    unsafe_allow_html=True
)

# --- EMPFANG ---
st.markdown('<h2 class="subtitle">Empfang ab 16:00 Uhr</h2>', unsafe_allow_html=True)

#col1, col2 = st.columns(2)
#with col1:
#    st.markdown('<p class="menu-section">🍹 Getränke</p>', unsafe_allow_html=True)
#    st.markdown("""
#    *  Mineralwasser still | mit Kohlensäure 
#    *  Softdrinks (Cola, Cola Light, Fanta, Sprite, Fassbrause) 
#    *  Limobar 
#    *  Säfte/Saftschorlen (Apfel, Orange, Rhabarber) 
#    *  Sekt, Wein & Bier 
#    *  Kaffee, Kaffeespezialitäten & Tee 
#    """)
#
#with col2:
#    st.markdown('<p class="menu-section">🥪 Fingerfood</p>', unsafe_allow_html=True)
#    st.markdown("""
#    * Lasst euch überraschen!
#    """)

st.markdown("""
    *  Mineralwasser still | mit Kohlensäure 
    *  Softdrinks (Cola, Cola Light, Fanta, Sprite und Fassbrause) 
    *  Limobar 
    *  Säfte/Saftschorlen (Apfel, Orange, Rhabarber) 
    *  Sekt, Wein & Bier 
    *  Kaffee, Kaffeespezialitäten & Tee 
    """)

# --- GETRÄNKE ---
st.markdown('<h2 class="subtitle">Getränke ab 17:00 Uhr</h2>', unsafe_allow_html=True)

st.markdown("""
*  Alles was es schon ab 16:00 Uhr gab und noch mehr! 
""")

st.markdown('<p class="menu-section">🍷 Weine </p>', unsafe_allow_html=True)
st.markdown("""
* Riesling (weiß | feinherb) 
* Grauburgunder (weiß | trocken) 
* Rotling (rosé | fruchtig)  
* Merlot (rot | trocken) 
""")

st.markdown('<p class="menu-section">🍺 Biere </p>', unsafe_allow_html=True)
st.markdown("""
*  Pils vom Fass 
*  Alkoholfreies Bier 
*  Hefeweizen  
*  Alkoholfreies Hefeweizen  
*  Radler | Diesel 
""")

st.markdown('<p class="menu-section">🍸 Aperitifs </p>', unsafe_allow_html=True)
st.markdown("""
*  Lilly’s (Lillet Blanc | Wildberry | Beeren | Eis) 
*  Aperol Spritz (Aperol | Secco | Mineralwasser | Orange | Eis) 
*  Rosa’s Tonic (Ramazotti Aperitivo Rosato | Tonic | Limette | Eis) 
*  Limoncello (Limoncello | Secco | Zitrone | Eis) 
*  Orange Spritz alkoholfrei (Orangensirup | Tonic | Wasser | Orange | Eis) 
*  Virgin Hugo alkoholfrei (Holunderblütensirup | Ginger Ale | Wasser | Minze | Eis) 
""")

# --- BUFFET ---
st.markdown('<h2 class="subtitle">Buffet – American BBQ ab 18:30 Uhr</h2>', unsafe_allow_html=True)

st.markdown('<p class="menu-section">🥗 Salate & Vorspeisen</p>', unsafe_allow_html=True)
st.markdown("""
*  Römersalat  
*  Bohnen, Radieschen, Karotten, Frühlingslauch, Palmenherzen, und Avocado in Wasabi Dressing 
*  Klassischer Cole Slaw 
*  Salat von Wassermelone und Hirtenkäse mit Zitronenöl 
*  Chicken Caesar Wrap 
*  "Stadtgut" Kartoffelsalat mit Salatgurke, Apfel und Mini Boulette  
""")

st.markdown('<p class="menu-section">🔥 Vom Grill</p>', unsafe_allow_html=True)
st.markdown("""
*  Burger zum selber bauen: Brioche Buns, 125g Rindfleisch Patty, Pulled Pork,  Tomaten, Gewürzgurken, Eisberg, Zwiebeln,  Bacon, Cheddar 
*  Gebratenes Lachsfilet mit „Maldon“- Zitronensalz, Blattspinat und gebratener Polenta 
*  Kleine Medaillons vom Roastbeef 
*  Gemüsespieße 
""")

st.markdown('<p class="menu-section">🥔 Beilagen</p>', unsafe_allow_html=True)
st.markdown("""
*  Maiskolben, Süßkartoffel- Stampf, Pikante Kartoffel- Wedges 
*  Bohnen im Speckmantel 
*  Hausgemachtes Kräuter & Knoblauch Baguette 
""")

st.markdown('<p class="menu-section">🍲 Saucen</p>', unsafe_allow_html=True)
st.markdown("""
*  BBQ Sauce, Honig- Senf, Guacamole,  
*  Aioli, Senf, Ketchup 
*  Butter & Kräuterbutter 
""")

st.markdown('<p class="menu-section">🍰 Desserts</p>', unsafe_allow_html=True)
st.markdown("""
*  Florida Mango Mousse mit Himbeer Jelly 
*  Schokoladen Brownie 
*  Cheesecake 
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
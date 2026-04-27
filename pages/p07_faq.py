import streamlit as st


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
        .faq-section {
            font-size: 20px;
            font-weight: bold;
            color: #6A4CA8;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel
st.markdown('<h1 class="title">FAQs</h1>', unsafe_allow_html=True)

# FAQ
st.markdown('<h2 class="subtitle">💡 Häufige Fragen</h2>', unsafe_allow_html=True)

# FAQ 1: Geschenke
with st.expander("🎁 Was dürfen wir euch schenken?"):
    st.write("Wir nehmen gerne Geldgeschenke an, da das eine Tradition in unseren elterlichen Kulturen ist.")

# FAQ 2: Dresscode
with st.expander("👔 Gibt es einen Dresscode?"):
    st.write("Werft Euch in tanzbare Schale.")

# FAQ 3: Getränke
with st.expander("🍷 Kann ich auch andere Getränke bekommen?"):
    st.write("Ja, alles außerhalb unserer Getränkekarte kann auf eigene Rechnung an der Bar bestellt werden. "
             "Kartenzahlung an der Bar ist möglich.")

# FAQ 4: Kinderbetten/Beistellbetten
with st.expander("🛏️ Gibt es Kinderbetten/Beistellbetten in den Hotelzimmern?"):
    st.write("Ja, auf Anfrage. Bitte gebt in eurer Buchungsanfrage an, ob und mit wie vielen Kindern ihr anreist.")

# FAQ 5: Stillzimmer
with st.expander("🤱 Gibt es während der Veranstaltung ein Stillzimmer?"):
    st.write("Ja, hinter dem Bankettraum. Bitte bei Eric Hensel vor Ort anfragen.")

# FAQ 6: Wickeltisch
with st.expander("👶 Wo finden wir einen Wickeltisch?"):
    st.write("In der Herrentoilette am Bankett. Bitte bei Eric Hensel vor Ort anfragen.")


st.markdown(
    """
    <p class="faq-section">
        ❓ Noch Fragen? Schreibt uns gerne auf WhatsApp oder anderen Messenger Apps!
    </p>
    """,
    unsafe_allow_html=True
)
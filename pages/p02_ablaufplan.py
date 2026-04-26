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
        .event {
            font-size: 18px;
            margin: 10px 0;
            padding: 10px;
            background-color: #EDE7F6;
            border-left: 5px solid #D1C4E9;
            border-radius: 5px;
            text-align: left;
        }
        .contact {
            font-size: 18px;
            color: #4A3B5C;
            text-align: left;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel
st.markdown('<h1 class="title">Ablaufplan</h1>', unsafe_allow_html=True)

# Samstag
st.divider()
st.markdown('<h2 class="subtitle">Samstag, 27.09.2025</h2>', unsafe_allow_html=True)

events_saturday = [
    ("Check-In im Landhaus Alte Scheune", "ab 14:30 Uhr"),
    ("Empfang & Fotos", "ab 16:00 Uhr"),
    ("Zeremonie", "ab 17:00 Uhr"),
    ("Grillbuffet", "ab 18:00 Uhr"),
    ("Kleine Überraschung vor dem Dessert", "ca. 19:30 Uhr"),
    ("Karaoke & Dessertbuffet", "ab ca. 20:15 Uhr"),
    ("Eröffnung der Tanzfläche", "ab ca. 21:00 Uhr"),
    ("Mitternachtssnack", "ab ca. 23:30 Uhr")
]

for event, time in events_saturday:
    st.markdown(f'<div class="event"><b>{time}</b>: {event}</div>', unsafe_allow_html=True)

st.divider()

# Sonntag
st.markdown('<h2 class="subtitle">Sonntag, 28.09.2025</h2>', unsafe_allow_html=True)

events_sunday = [
    ("Frühstück", "08:00 bis 10:30 Uhr"),
    ("Check-Out", "bis 11:30 Uhr")
]

for event, time in events_sunday:
    st.markdown(f'<div class="event"><b>{time}</b>: {event}</div>', unsafe_allow_html=True)

st.divider()

# Ideensammlung
st.markdown(
    '<div class="contact">💡 Möchtet ihr einen Programmpunkt beisteuern? Meldet euch gerne bei <b>Eric Hensel</b> unter <a href="mailto:eric.hensel@alte-scheune.de">eric.hensel@alte-scheune.de</a></div>',
    unsafe_allow_html=True
)

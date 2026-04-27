import streamlit as st
import pandas as pd
import pydeck as pdk


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
        .contact {
            font-size: 20px;
            font-weight: bold;
            color: #4A3B5C;
            text-align: left;
            margin-top: 30px;
        }
        iframe {
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Define a PyDeck Layer
st.title("Mitfahrbörse")
st.markdown("""
### Du suchst eine Mitfahrgelegenheit oder möchtest Fahrer sein?
Wenn du Fahrer bist und Mitfahrer suchst oder selbst eine Mitfahrgelegenheit brauchst, dann melde dich bei uns!

Wir bringen Fahrer und Mitfahrer zusammen und helfen dabei, Fahrgemeinschaften zu bilden.
Bitte beachte jedoch, dass wir **nicht garantieren können**, dass jede Fahrt tatsächlich zustande kommt.

**Interesse? Dann kontaktiere uns auf den gängigen Messenger Apps.**
""")

st.divider()

# Karte-Info
st.markdown("""
### Wo gibt es die meisten Mitfahrgelegenheiten? 🔍
Die folgende Karte zeigt die Anzahl der Parteien, die in einer Stadt wohnen und potenziell an einer Mitfahrgelegenheit interessiert sind.

Je mehr Parteien in einer Stadt anzutreffen sind, desto höher die Chance, eine passende Fahrgemeinschaft zu finden. Wer Lust auf eine komplexere Fahrtenplanung hat, kann sich hier auch austoben.
""")

st.divider()

# City occurrences
city_list = [
    "Butzbach", "Butzbach", "Hettenrodt", "Mainz", "Mainz", "Butzbach",
    "Potsdam", "Brandenburg an der Havel", "Berlin", "Frankfurt am Main",
    "München", "Frankfurt am Main", "Berlin", "Frankfurt am Main",
    "Frankfurt am Main", "Darmstadt", "Meerbusch", "Frankfurt am Main",
    "Freigericht", "Berlin", "Berlin", "Braunschweig", "Berlin", "Berlin",
    "Berlin", "Groß-Gerau", "Mannheim", "Berlin", "München", "Nürnberg",
    "Berlin", "Zürich", "Berlin", "Berlin", "Berlin"
]

# Count occurrences of each city
city_counts = pd.Series(city_list).value_counts().to_dict()

# City coordinates
city_coordinates = {
    "Butzbach": (50.4371, 8.6711),
    "Hettenrodt": (49.7289, 7.2756),
    "Mainz": (49.9842, 8.2791),
    "Potsdam": (52.3906, 13.0645),
    "Brandenburg an der Havel": (52.4160, 12.5500),
    "Berlin": (52.5200, 13.4050),
    "Frankfurt am Main": (50.1109, 8.6821),
    "München": (48.1351, 11.5820),
    "Darmstadt": (49.8728, 8.6512),
    "Meerbusch": (51.2526, 6.6900),
    "Freigericht": (50.1450, 9.1436),
    "Braunschweig": (52.2689, 10.5268),
    "Groß-Gerau": (49.9225, 8.4828),
    "Mannheim": (49.4875, 8.4660),
    "Nürnberg": (49.4521, 11.0767),
    "Zürich": (47.3769, 8.5417),
}

# Create DataFrame with counts
df = pd.DataFrame([
    (city, *city_coordinates[city], city_counts.get(city, 0))
    for city in city_coordinates.keys()
], columns=["city", "lat", "lon", "count"])

# PyDeck Scatterplot Layer with count information
scatter_layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position=["lon", "lat"],
    get_radius=8000,  # Smaller red dots
    get_color=[255, 0, 0, 200],  # Red with transparency
    pickable=True,  # Enables tooltips
)

# Map View Settings (Centered between Germany & Switzerland)
view_state = pdk.ViewState(
    latitude=50.0,  # Centered for best visibility
    longitude=9.0,
    zoom=5.5,
    pitch=0  # No tilt
)

# Render PyDeck Map in Streamlit with a bright theme
st.pydeck_chart(pdk.Deck(
    layers=[scatter_layer],
    initial_view_state=view_state,
    tooltip={"text": "📍 {city}\n# Parteien: {count}\nφ: {lat}\nλ: {lon}"},
    map_style="light"  # Bright map style
))
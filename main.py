import streamlit as st
from navigation import get_navigation

# Grundkonfiguration (Sidebar einklappen, damit sie oben nicht stört)
st.set_page_config(layout="wide")

# Session State Initialisierung
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Navigation laden und ausführen
pg = get_navigation()
pg.run()

# Optional: CSS fix, um die Top-Bar optisch zu betonen
st.markdown("""
    <style>
        header[data-testid="stHeader"] {
            background-color: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
        }
    </style>
""", unsafe_allow_html=True)
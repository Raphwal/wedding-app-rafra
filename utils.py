import streamlit as st
from cryptography.fernet import Fernet
import io
import base64

def get_cipher():
    """Initialisiert den Cipher mit dem Key aus den Secrets."""
    # Wir nutzen den Key, den du in .streamlit/secrets.toml hinterlegt hast
    key = st.secrets["KEY"]
    # Sicherstellen, dass der Key als String vorliegt und dann in Bytes konvertiert wird
    if isinstance(key, str):
        key = key.encode()
    return Fernet(key)

def load_decrypted_image(file_path):
    """Lädt eine .bin Datei, entschlüsselt sie und gibt ein BytesIO-Objekt zurück."""
    cipher = get_cipher()
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    return io.BytesIO(decrypted_data)

def decrypt_text(encrypted_string):
    """Entschlüsselt einen einzelnen String."""
    if not encrypted_string:
        return "Keine Daten vorhanden."
    cipher = get_cipher()
    return cipher.decrypt(encrypted_string.encode()).decode()

def set_encrypted_bg(bin_file):
    """Entschlüsselt ein Bild und setzt es als Hintergrund."""
    try:
        # 1. Bild über deine Utility-Funktion entschlüsseln
        img_data = load_decrypted_image(bin_file)
        
        # 2. Die Bytes aus dem Stream lesen und in Base64 kodieren
        base64_image = base64.b64encode(img_data.getvalue()).decode()
        
        # 3. Das CSS mit dem Base64-String injizieren
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{base64_image}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            
            /* Optional: Ein leichter Overlay, damit der Text besser lesbar ist */
            .stApp::before {{
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(238, 220, 154, 0.4); /* Dein Beige mit 40% Transparenz */
                z-index: -1;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Hintergrund konnte nicht geladen werden: {e}")

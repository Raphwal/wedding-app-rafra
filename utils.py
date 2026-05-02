import streamlit as st
from cryptography.fernet import Fernet
import io

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
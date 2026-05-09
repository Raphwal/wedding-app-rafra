import streamlit as st
from cryptography.fernet import Fernet
import io
import base64
from PIL import Image

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
            

            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Hintergrund konnte nicht geladen werden: {e}")


def crop_image_top_bottom(image_data, top_percent, bottom_percent):
    """
    Schneidet ein Bild oben und unten um den angegebenen Prozentsatz zu.
    image_data: BytesIO Objekt (aus deiner Entschlüsselung)
    """
    img = Image.open(image_data)
    width, height = img.size
    
    # Berechne die Pixel-Koordinaten
    # (left, top, right, bottom)
    left = 0
    right = width
    top = height * (top_percent / 100)
    bottom = height * (1 - (bottom_percent / 100))
    
    # Der eigentliche Schnitt
    cropped_img = img.crop((left, top, right, bottom))
    
    # Wieder in einen Stream speichern, damit st.image es versteht
    buffer = io.BytesIO()
    cropped_img.save(buffer, format="JPEG")
    return buffer

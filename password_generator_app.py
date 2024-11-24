import random
import string
import streamlit as st

# Funzione per generare la password
def generate_password(length=16, use_uppercase=True, use_lowercase=True, use_numbers=True, use_specials=True):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        return "Errore: Seleziona almeno un tipo di carattere."
    
    return ''.join(random.choice(characters) for _ in range(length))

# Layout ottimizzato per mobile
st.set_page_config(page_title="Generatore di Password", layout="centered")

st.title("🔐 Generatore di Password Sicure")

with st.form("password_form"):
    st.subheader("Configura le impostazioni")
    length = st.slider("Lunghezza Password", min_value=4, max_value=64, value=16)
    use_uppercase = st.checkbox("Usa Maiuscole", value=True)
    use_lowercase = st.checkbox("Usa Minuscole", value=True)
    use_numbers = st.checkbox("Usa Numeri", value=True)
    use_specials = st.checkbox("Usa Caratteri Speciali", value=T

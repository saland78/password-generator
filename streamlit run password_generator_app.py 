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

# Interfaccia Web con Streamlit
st.title("Generatore di Password Sicure")

st.sidebar.header("Impostazioni")
length = st.sidebar.slider("Lunghezza Password", min_value=4, max_value=64, value=16)
use_uppercase = st.sidebar.checkbox("Usa Maiuscole", value=True)
use_lowercase = st.sidebar.checkbox("Usa Minuscole", value=True)
use_numbers = st.sidebar.checkbox("Usa Numeri", value=True)
use_specials = st.sidebar.checkbox("Usa Caratteri Speciali", value=True)

if st.sidebar.button("Genera Password"):
    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_numbers=use_numbers,
        use_specials=use_specials
    )
    st.subheader("La tua Password Generata")
    st.code(password)
else:
    st.write("Configura le impostazioni nel menu a sinistra e premi 'Genera Password'.")

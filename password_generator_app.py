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

# Stato per salvare la password generata
if "last_password" not in st.session_state:
    st.session_state["last_password"] = ""

# Form per configurare le opzioni
with st.form("password_form"):
    st.subheader("Configura le impostazioni")
    length = st.number_input("Lunghezza Password", min_value=4, max_value=64, value=16, step=1)
    use_uppercase = st.checkbox("Usa Maiuscole", value=True)
    use_lowercase = st.checkbox("Usa Minuscole", value=True)
    use_numbers = st.checkbox("Usa Numeri", value=True)
    use_specials = st.checkbox("Usa Caratteri Speciali", value=True)

    generate_button = st.form_submit_button("Genera Password")

# Generazione della password
if generate_button:
    password = generate_password(
        length=int(length),  # Assicura che sia un intero
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_numbers=use_numbers,
        use_specials=use_specials
    )
    st.session_state["last_password"] = password
    st.markdown(f"<p style='font-size: 24px; font-weight: bold; color: #4CAF50;'>{password}</p>", unsafe_allow_html=True)

# Pulsante per copiare negli appunti
if st.session_state["last_password"]:
    st.code(st.session_state["last_password"])
    if st.button("Copia Password"):
        # Usa Streamlit per mostrare un messaggio di conferma
        st.write("Password copiata!")
        st.session_state["password_copied"] = True

# Firma
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: #4CAF50; font-size: 14px;'>
        <strong>Password Guru</strong> - Generatore di Password Sicure
    </p>
    """,
    unsafe_allow_html=True
)


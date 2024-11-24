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
    use_specials = st.checkbox("Usa Caratteri Speciali", value=True)

    generate_button = st.form_submit_button("Genera Password")

if generate_button:
    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_numbers=use_numbers,
        use_specials=use_specials
    )
    st.subheader("La tua Password Generata:")
    # Mostra la password con uno stile più grande
    st.markdown(f"<p style='font-size: 24px; font-weight: bold; color: #4CAF50;'>{password}</p>", unsafe_allow_html=True)
    # Pulsante per copiare la password
    if st.button("Copia negli appunti"):
        st.code(password)
        st.session_state["password_copied"] = True  # Salva lo stato
        st.success("Password copiata negli appunti!")

st.markdown(
    """
    <style>
    /* Ottimizzazione per mobile */
    .css-1aumxhk { padding: 1rem; } /* Riduce i margini laterali */
    .css-1v0mbdj { font-size: 1rem; } /* Migliora la leggibilità */
    </style>
    """,
    unsafe_allow_html=True
)

import random
import string
import streamlit as st
import html  # Per la sanitizzazione dei caratteri speciali

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
    length = st.slider("Lunghezza Password", min_value=4, max_value=64, value=16)
    use_uppercase = st.checkbox("Usa Maiuscole", value=True)
    use_lowercase = st.checkbox("Usa Minuscole", value=True)
    use_numbers = st.checkbox("Usa Numeri", value=True)
    use_specials = st.checkbox("Usa Caratteri Speciali", value=True)

    generate_button = st.form_submit_button("Genera Password")

# Generazione della password
if generate_button:
    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_numbers=use_numbers,
        use_specials=use_specials
    )
    # Escapa i caratteri speciali per HTML e JavaScript
    sanitized_password = html.escape(password)
    st.session_state["last_password"] = sanitized_password
    st.markdown(f"<p style='font-size: 24px; font-weight: bold; color: #4CAF50;'>{sanitized_password}</p>", unsafe_allow_html=True)

# JavaScript per copiare negli appunti
if st.session_state["last_password"]:
    st.markdown(
        f"""
        <button id="copyButton" style="margin-top: 10px; padding: 8px 12px; background-color: #4CAF50; color: white; border: none; cursor: pointer; font-size: 16px;">Copia Password</button>
        <script>
        document.getElementById("copyButton").addEventListener("click", async function() {{
            try {{
                await navigator.clipboard.writeText("{st.session_state['last_password']}");
                alert("Password copiata!");
            }} catch (err) {{
                alert("Errore durante la copia: " + err);
            }}
        }});
        </script>
        """,
        unsafe_allow_html=True
    )

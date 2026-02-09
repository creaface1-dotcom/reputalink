import streamlit as st
import requests
import json
import os

# Configurazione base
st.set_page_config(page_title="ReputaLink 2026", page_icon="🛡️")

def chiedi_all_ia(prompt, api_key):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={{api_key}}"
    headers = {'Content-Type': 'application/json'}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
        if response.status_code == 200:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"Errore API: {{response.status_code}}"
    except requests.exceptions.Timeout:
        return "Errore: Timeout della richiesta. Riprova."
    except requests.exceptions.RequestException as e:
        return f"Errore di connessione: {{str(e)}}"
    except (KeyError, IndexError):
        return "Errore: Risposta API non valida. Controlla la tua API Key."
    except Exception as e:
        return f"Errore inaspettato: {{str(e)}}"

# Interfaccia
st.title("🛡️ ReputaLink 2026")
st.markdown("L'intelligenza artificiale al servizio della tua immagine.")

# Sidebar per i comandi
with st.sidebar:
    st.header("Configurazione")
    api_key = st.text_input("Google API Key", type="password", help="Inserisci la tua chiave API di Google Gemini")
    sezione = st.radio("Menu", ["🔍 Explorer Pubblico", "📈 Strategia Business"])

if sezione == "🔍 Explorer Pubblico":
    st.subheader("Analisi Reputazione")
    target = st.text_input("Chi vuoi analizzare?", placeholder="es. Fiat, Apple...")
    if st.button("Ottieni Voto IA"):
        if api_key and target:
            with st.spinner("L'IA sta leggendo il web 2026..."):
                res = chiedi_all_ia(f"Dai un voto da 1 a 100 alla reputazione di {{target}} a Febbraio 2026 e spiega perché in 3 punti.", api_key)
                st.info(res)
        else:
            st.error("Inserisci sia l'API Key che il nome!")

elif sezione == "📈 Strategia Business":
    st.subheader("Area Strategica")
    pwd = st.text_input("Password di accesso", type="password")
    if pwd == st.secrets.get("REPUTA_PASSWORD", "REPUTA2026"):
        brand = st.text_input("Inserisci il tuo Brand da proteggere:")
        if st.button("Genera Piano d'Azione"):
            if api_key and brand:
                with st.spinner("Calcolando contromisure SEO..."):
                    res = chiedi_all_ia(f"Crea una strategia di bonifica per {{brand}}. Fornisci 5 parole chiave e un titolo per un articolo riparatore.", api_key)
                    st.success(res)
            else:
                st.error("Inserisci sia l'API Key che il nome del brand!")
    else:
        st.warning("Inserisci la password corretta (REPUTA2026).")
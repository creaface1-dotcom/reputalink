# 🛡️ ReputaLink 2026

L'intelligenza artificiale al servizio della tua immagine.

## Descrizione

ReputaLink 2026 è un'applicazione Streamlit che utilizza Google Gemini AI per analizzare e gestire la reputazione online di brand e aziende.

### Funzionalità

#### 🔍 Explorer Pubblico
- Analizza la reputazione di brand e aziende
- Ricevi un voto da 1 a 100 con spiegazione
- Scopri i punti forti e deboli della tua immagine online

#### 📈 Strategia Business
- Area protetta con password
- Genera piani d'azione personalizzati
- Ricevi strategie SEO e parole chiave suggerite
- Crea titoli per articoli riparatori

## Installazione

1. **Clona il repository:**
```bash
git clone https://github.com/creaface1-dotcom/reputalink.git
cd reputalink
```

2. **Crea un ambiente virtuale:**
```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

3. **Installa le dipendenze:**
```bash
pip install -r requirements.txt
```

4. **Configura la API Key di Google:**
   - Crea un file `.streamlit/secrets.toml`
   - Aggiungi la tua API Key di Google Gemini:
```toml
GOOGLE_API_KEY = "la_tua_api_key_qui"
REPUTA_PASSWORD = "la_tua_password_qui"
```

5. **Avvia l'applicazione:**
```bash
streamlit run app.py
```

## Configurazione

### Google Gemini API
1. Visita [Google AI Studio](https://ai.google.dev/)
2. Crea una nuova API Key
3. Aggiungi la chiave ai tuoi secrets

### Password Area Business
La password predefinita è `REPUTA2026`. Cambiala nel file `secrets.toml` per una maggiore sicurezza.

## Utilizzo

### Explorer Pubblico
1. Seleziona "🔍 Explorer Pubblico" dal menu
2. Inserisci la tua Google API Key
3. Scrivi il nome del brand da analizzare
4. Clicca "Ottieni Voto IA"

### Strategia Business
1. Seleziona "📈 Strategia Business" dal menu
2. Inserisci la password di accesso
3. Inserisci il nome del tuo brand
4. Clicca "Genera Piano d'Azione"

## Sicurezza

- **Non** salvare le API Key nel codice
- Usa sempre `.streamlit/secrets.toml` per le credenziali
- Proteggi il file `secrets.toml` aggiungendolo a `.gitignore`
- Cambia la password predefinita

## Requisiti

- Python 3.8+
- Google Gemini API Key
- Connessione internet

## Licenza

MIT License - vedi LICENSE per i dettagli

## Autore

creaface1-dotcom

## Supporto

Per problemi o suggerimenti, apri un issue su GitHub.
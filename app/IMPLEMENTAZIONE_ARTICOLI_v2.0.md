# 🕐 Schedulatore Laser - Versione 2.0

Sistema completo di gestione ordini di lavorazione con tracciamento articoli per fase.

## 🎯 Novità Principali

### ✨ Tracciamento Articoli per Fase
- **Ogni articolo ha proprie fasi richieste** - Non più tutto l'ordine, ma singoli articoli
- **Auto-routing intelligente** - Il sistema sa quali articoli richiedono quale fase prossima
- **Dashboard intuitiva** - Vedi lo stato di ogni articolo e la prossima fase

### 📦 Gestione Ordini Avanzata
- **Caricamento automatico PDF** - Estrae cliente, data consegna, articoli
- **Articoli dinamici** - Aggiungi/rimuovi articoli prima di salvare l'ordine
- **Fasi personalizzabili** - Scegli quali fasi servono per questo ordine

### 📊 Dashboard Completo
- **Vista aggregata** - Tutti gli ordini in un colpo d'occhio
- **Dettagli per articolo** - Vedi per ogni articolo quali fasi sono completate e quale è prossima
- **Timeline processing** - Traccia quando è iniziata e completata ogni fase

### 🚀 Stazioni di Lavoro
- **Laser** - Articoli pronti per questa fase
- **Piega** - Articoli pronti per questa fase
- **Saldatura** - Articoli pronti per questa fase
- **Auto-update** - Schermo aggiornato ogni 5 secondi

## 📋 Struttura del Progetto

```
app/
├── backend/                 # Backend Flask + Database
│   ├── models.py           # Order model con articoli JSON
│   ├── database.py         # CRUD operations con OrderManager
│   ├── app.py              # Flask routes
│   ├── pdf_parser.py       # PDF data extraction
│   └── __init__.py         # Backend package init
│
├── frontend/               # UI HTML5
│   ├── welcome.html        # Caricamento ordini + articoli
│   ├── dashboard.html      # Dashboard ordini con modal dettagli
│   ├── laser.html          # Stazione laser
│   ├── piega.html          # Stazione piega
│   ├── saldatura.html      # Stazione saldatura
│   └── archive.html        # Ordini completati
│
├── database/               # SQLite database
│   └── scheduler.db        # Auto-creato
│
└── uploads/                # File upload
    ├── drawings/           # DXF files
    └── pdfs/              # PDF files
```

## 🚀 Come Avviare

### Opzione 1: Python Diretto

```bash
# Installa dipendenze (una volta)
pip install -r requirements.txt

# Avvia il backend
python run.py
```

### Opzione 2: Script Start (Windows)

```bash
# Doppio-click su
START_BACKEND.bat
```

Il backend sarà disponibile su: **http://localhost:5000**

## 📱 Accesso Frontend

### Caricamento Ordini
- **URL**: `file:///<percorso>/frontend/welcome.html`
- **Funzioni**:
  - Carica PDF ordine (estrazione automatica)
  - Aggiungi articoli dinamicamente
  - Seleziona fasi richieste (LASER, PIEGA, SALDATURA, PULIZIA)
  - Salva ordine nel database

### Dashboard
- **URL**: `file:///<percorso>/frontend/dashboard.html`
- **Funzioni**:
  - Visualizza tutti gli ordini
  - Modal con dettagli ordine
  - Vedi stato articoli e prossima fase
  - Timeline fasi

### Stazioni Lavoro
- **Laser**: `file:///<percorso>/frontend/laser.html`
- **Piega**: `file:///<percorso>/frontend/piega.html`
- **Saldatura**: `file:///<percorso>/frontend/saldatura.html`
- **Funzioni**:
  - Articoli pronti per questa fase
  - Pulsante "Inizia" per tracciare inizio
  - Pulsante "Completa" per marcare finito
  - Auto-update ogni 5 secondi

### Archivio
- **URL**: `file:///<percorso>/frontend/archive.html`
- **Funzioni**:
  - Visualizza ordini completati
  - Statistiche consegne
  - Filtri per cliente

## 🔄 Flusso di Lavoro

### Creazione Ordine
1. Apri **welcome.html**
2. Carica PDF (auto-estrae cliente + data consegna)
3. Aggiungi articoli:
   - Nome articolo  - Codice (opzionale)
   - Quantità
4. Seleziona fasi richieste (check boxes)
5. Clicca "Salva Ordine"

### Lavorazione
1. Operatore va su stazione (Laser, Piega, o Saldatura)
2. Vede articoli pronti per quella fase
3. Clicca "Inizia" quando prende il pezzo
4. Clicca "Completa" quando finisce
5. Sistema auto-calcola prossima fase per ogni articolo
6. Schermo auto-aggiorna ogni 5 secondi

### Tracciamento
1. Apri **dashboard.html**
2. Vedi tutti gli ordini
3. Clicca ordine per aprire modal
4. Nel modal vedi:
   - Per ogni articolo: fasi completate e prossima fase
   - Timeline con timestamps di inizio/fine per ogni fase ordine

## 💾 Modello Dati

### Order
```json
{
  "id": "uuid",
  "cliente": "Nome Cliente",
  "data_ricezione": "2024-01-15T10:30:00",
  "data_consegna": "2024-01-20T18:00:00",
  "status": "RICEVUTO | SPEDITO",
  "total_quantity": 150,
  "required_phases": ["LASER", "PIEGA", "SALDATURA"],
  "articles": [
    {
      "name": "Staffa A",
      "code": "SA-001",
      "qty": 50,
      "required_phases": ["LASER", "PIEGA", "SALDATURA"]
    },
    {
      "name": "Bracket B",
      "code": "BR-002",
      "qty": 100,
      "required_phases": ["LASER", "SALDATURA"]
    }
  ]
}
```

### ProcessingStep
```json
{
  "id": "uuid",
  "order_id": "parent_order_id",
  "fase": "LASER | PIEGA | SALDATURA | PULIZIA | SPEDIZIONE",
  "timestamp_inizio": "2024-01-15T11:00:00",
  "timestamp_fine": "2024-01-15T14:30:00",
  "operatore": "Giuseppe",
  "note": "Lavoro completato senza problemi"
}
```

## 🔌 API Backend

### Ordini
- `POST /api/orders` - Crea nuovo ordine
- `GET /api/orders` - Lista ordini (filtro cliente opzionale)
- `GET /api/orders/<order_id>` - Dettagli ordine con stato articoli
- `PUT /api/orders/<order_id>/articles` - Aggiorna articoli

### Fasi
- `POST /api/orders/<order_id>/phase/<phase>/start` - Inizia fase
- `POST /api/orders/<order_id>/phase/<phase>/complete` - Completa fase
- `GET /api/phase/<phase>/orders` - Ordini per fase (articoli pronti)

### File
- `POST /api/extract-pdf-data` - Estrae dati da PDF
- `POST /api/upload-drawing` - Carica disegno DXF

## ⚙️ Configurazione

### Variabili Database
- **Percorso**: `database/scheduler.db` (SQLite)
- **Auto-creato**: Al primo avvio
- **Schema**: Crea tables automaticamente

### Porte
- **Backend Flask**: `5000`
- **CORS**: Permette localhost

### Upload
- **DXF**: `uploads/drawings/`
- **PDF**: `uploads/pdfs/`

## 🐛 Troubleshooting

### "Connection refused localhost:5000"
- Assicurati che `run.py` sia in esecuzione
- Verifica porta 5000 non occupata: `netstat -ano | findstr 5000`

### "ModuleNotFoundError: backend"
- Installa dipendenze: `pip install -r requirements.txt`
- Assicurati di eseguire da cartella `app/`

### PDF non estratto
- Verifica che il PDF sia valido
- Controlla percorso assoluto file

### Ordine non appare in stazione laser
- Verifica che LASER sia in `required_phases` articolo
- Controlla che LASER sia stato già completato prima (altrimenti prossima fase è LASER)

## 📞 Supporto

Per problemi:
1. Controlla console Flask (run.py) per errori
2. Verifica Browser console (F12) per errori JavaScript
3. Controlla database/scheduler.db esiste

## 📝 Note

- Sistema usa SQLite - Nessun server DB esterno richiesto
- Frontend è HTML puro - Nessuno build step
- CORS abilitato - Permette richieste da file://
- PDF parsing usa PyPDF2 - Supporta PDF standard

---

**Schedulatore Laser v2.0** © 2024 - Sistema di gestione ordini con tracciamento articoli

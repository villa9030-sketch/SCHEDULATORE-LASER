# 🏭 SCHEDULATORE LASER - CARPENTERIA METALLICA

Applicazione web per la gestione automatizzata degli ordini di carpenteria metallica con focus su ottimizzazione del taglio laser.

## 🎯 Funzionalità Principali

### 1. **Caricamento Automatico Ordini**
- Upload di file PDF con gli ordini
- Parsing automatico del documento
- Estrazione dati essenziali:
  - Numero ordine
  - Cliente
  - Data di consegna
  - Tipo di lavorazioni
  - Note speciali

### 2. **Gestione File di Disegno**
- Upload di file DXF/DWG
- Analisi automatica dello spessore del materiale
- Estrazione dati tecnici dal disegno

### 3. **Tracciamento in Tempo Reale delle Lavorazioni** ⭐ NEW
- **Step Standard Automatici**: Laser cut → Sbavatura → Piegatura → Saldatura → Finitura → Assemblaggio → QC → Imballaggio
- **Timeline Visuale**: Visualizza lo stato di ogni step in tempo reale
- **Aggiornamento Progresso**: Aggiorna percentuale di completamento per ogni step
- **Assegnazione Operatore**: Traccia chi sta eseguendo il lavoro
- **Note e Osservazioni**: Registra problemi e soluzioni per ogni step
- **Cronologia Completa**: Storico di tutti i cambiamenti di stato
- **Stima Tempo Rimanente**: Calcolo automatico del tempo di completamento

### 4. **Pianificazione Laser Ottimizzata**
- Raggruppamento automatico per spessore
- Ordinamento per data di consegna
- Prioritizzazione della lavorazione
- Visualizzazione intuitiva della sequenza

### 5. **Dashboard e Monitoraggio**
- Statistiche in tempo reale
- Elenco ordini con filtri
- Tracciamento dello stato di lavorazione
- Visualizzazione file allegati
- **Stato Lavorazione per Colonna**: Visualizza ordini raggruppati per fase (non iniziati, in corso, quasi finiti, completati, bloccati)

## 🚀 Come Installare

### Prerequisiti
- Python 3.8+
- pip (gestore pacchetti Python)
- Browser moderno

### Installazione

1. **Clona/scarica il progetto**
```bash
cd schedulatore
```

2. **Crea un ambiente virtuale Python** (opzionale ma consigliato)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Installa le dipendenze**
```bash
pip install -r requirements.txt
```

4. **Avvia il server backend**
```bash
cd backend
python app.py
```

Il backend sarà disponibile su: `http://localhost:5000`

5. **Apri il frontend**
- Apri il file `frontend/index.html` nel browser
- Oppure usa un server HTTP locale:
```bash
# Con Python
cd frontend
python -m http.server 8000
# Poi accedi a http://localhost:8000
```

## 📁 Struttura del Progetto

```
schedulatore/
├── backend/
│   ├── app.py                 # API Flask principale
│   ├── database.py            # Modelli SQLAlchemy
│   ├── pdf_parser.py          # Parsing file PDF
│   ├── dxf_processor.py       # Analisi file DXF/DWG
│   └── requirements.txt       # Dipendenze Python
├── frontend/
│   └── index.html             # Interfaccia web
├── database/
│   └── scheduler.db           # Database SQLite (creato automaticamente)
└── uploads/
    ├── pdfs/                  # PDF degli ordini
    └── drawings/              # File DXF/DWG
```

## 💾 Database

Il sistema utilizza **SQLite** (non richiede installazione aggiuntiva).

### Tabelle Principali

- **orders**: Ordini principali
- **order_files**: File allegati (DXF, DWG, PDF)
- **processing_steps**: Tracciamento delle fasi di lavorazione

## 🔧 API Endpoints

### Ordini
```
GET  /api/orders                    # Lista tutti gli ordini
POST /api/orders/upload             # Carica nuovo ordine
GET  /api/orders/<id>               # Dettagli ordine
PUT  /api/orders/<id>/status        # Aggiorna stato
POST /api/orders/<id>/files/upload  # Carica file di disegno
GET  /api/orders/by-thickness       # Ordini raggruppati per spessore
```

### Tracciamento Lavorazioni (NEW)
```
GET  /api/orders/<id>/progress      # Progresso complessivo ordine + timeline
GET  /api/orders/<id>/steps         # Lista step di lavorazione
PUT  /api/steps/<id>/status         # Aggiorna stato step
PUT  /api/steps/<id>/progress       # Aggiorna progresso percentuale
GET  /api/steps/<id>/history        # Cronologia cambiamenti step
GET  /api/workflow/by-status        # Ordini raggruppati per stato workflow
```

## 🎨 Interfaccia Utente

### Tab disponibili:
1. **Dashboard**: Vista d'insieme, statistiche
2. **Carica Ordine**: Upload e parsing PDF
3. **Ordini**: Elenco completo con filtri
4. **Stato Lavorazione**: Timeline con step di lavorazione in tempo reale
5. **Pianificazione Laser**: Programma ottimizzato per spessore

## 🔄 Workflow Tipico

1. **Ricevi ordine via mail** → Scarica PDF
2. **Carica PDF** nel sistema
3. **Sistema estrae automaticamente**:
   - Numero ordine
   - Cliente
   - Data consegna
   - Lavorazioni richieste
4. **Allega file di disegno** (DXF/DWG)
5. **Sistema analizza spessore** automaticamente
6. **Visualizza in pianificazione laser** raggruppato per spessore
7. **Ordini organizzati per efficienza** con priorità per consegna

## 📊 Vantaggi

✅ **Automazione**: Da mail a programma in pochi click
✅ **Efficienza**: Raggruppamento intelligente per spessore
✅ **Tracciamento**: Monitoraggio completo dello stato
✅ **Organizzazione**: Priorità per data di consegna
✅ **Riduzione errori**: Parsing automatico dati

## 🐛 Troubleshooting

### Errore: "Connection refused" quando accedo al backend
- Verifica che il server Flask stia correndo con `python app.py`
- Controlla che la porta 5000 sia disponibile

### I dati PDF non vengono estratti correttamente
- Assicurati che il PDF sia testuale (non scansionato)
- Verifica il formato del documento
- Aggiungi i pattern di ricerca specifici nel file `pdf_parser.py`

### File DXF non riconosce lo spessore
- Verifica che il file contenga il dato di spessore nel layer o nel testo
- Prova ad aggiungere lo spessore nel nome file: `ordine_2.5mm.dxf`

## 📝 Prossimi Sviluppi

- [ ] Integrazione email SMTP per ricezione automatica
- [ ] OCR per PDF scansionati
- [ ] Esportazione report/statistiche
- [ ] Integrazione con software di taglio laser
- [ ] App mobile
- [ ] Sistema di notifiche/alert via email/SMS
- [ ] Multi-utente con permessi e ruoli
- [ ] Storico e analytics avanzate
- [ ] Notifiche in tempo reale (WebSocket)
- [ ] Assegnazione automatica step per capacità operatore
- [ ] Analisi performance e tempi medi lavorazione
- [ ] Sistema di costi e quotazioni

## 📧 Supporto

Per problemi o suggerimenti, contatta lo sviluppatore.

---

**Versione**: 1.0
**Ultimo aggiornamento**: Febbraio 2026

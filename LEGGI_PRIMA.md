# 🔴 SCHEDULATORE LASER v1.0 - Sistema Completo

## 📚 Documentazione Principale

Questo documento descrive il sistema **Schedulatore Laser**, un'applicazione web per la gestione automatizzata degli ordini di carpenteria metallica con **supporto multi-postazione su rete locale**.

### 📋 File Importanti

| File | Descrizione |
|------|------------|
| `START_BACKEND.bat` | 🚀 Avvia il backend (eseguire PRIMA di tutto) |
| `FIND_IP.bat` | 🌐 Trova l'IP del server |
| `frontend/welcome.html` | 🏠 Pagina di benvenuto |
| `frontend/scheduler.html` | 📊 Applicazione principale |
| `GUIDA_MULTI_POSTAZIONE.md` | 📖 Guida dettagliata rete multi-postazione |

---

## 🚀 QUICK START (3 PASSI)

### Passo 1️⃣: Avvio Server
```bash
cd c:\Users\39334\Documents\SCHEDULATORE LASER\app
START_BACKEND.bat
```
✅ Il backend si avvia su `http://localhost:5000`

### Passo 2️⃣: Trovare IP (per rete)
Se altri computer accedono da remoto:
```bash
FIND_IP.bat
```
Cerca l'indirizzo IPv4 (es: `192.168.1.100`)

### Passo 3️⃣: Aprire nel Browser
- **Locale**: http://localhost:5000/frontend/welcome.html
- **Remoto**: http://192.168.1.100:5000/frontend/welcome.html

---

## 🌐 ACCESSO MULTI-POSTAZIONE

```
┌─────────────────────────────┐
│  POSTAZIONE SERVER          │
│  IP: 192.168.1.100          │
│  Backend: app.py            │
│  Browser: http://localhost  │
└─────────────────────────────┘
         ↓        ↓         ↓
    ┌────────┐ ┌─────────┐ ┌────────┐
    │POST 1  │ │ POST 2  │ │ POST 3 │
    │Browser │ │ Browser │ │Browser │
    └────────┘ └─────────┘ └────────┘
       http://192.168.1.100:5000
       (Stessa applicazione!)
```

Tutte le postazioni accedono **allo STESSO database** centralizzato.

---

## 🎯 FUNZIONALITÀ PRINCIPALE

### 📊 Dashboard
- Statistiche in tempo reale
- Ordini raggruppati per stato di avanzamento
- Avvisi ordini in scadenza
- Aggiornamento automatico ogni 30 secondi

### 📋 Gestione Ordini
- Upload PDF → Estrazione dati automatica
- Upload DXF/DWG → Analisi spessore automatica
- Visualizzazione file allegati

### ⚙️ Programmazione Laser
- Raggruppamento file per spessore
- Ordinamento per data di consegna
- Pianificazione sequenza lavorazione

### 🚀 Tracciamento Lavorazioni
- 8 step standard di lavorazione:
  1. Laser Cutting
  2. Sbavatura
  3. Piegatura
  4. Saldatura
  5. Finitura
  6. Assemblaggio
  7. Quality Control
  8. Imballaggio
- Aggiornamento stato in tempo reale
- Percentuale di completamento per step
- Note e assegnazione operatore

---

## 📱 ACCESSO DA DISPOSITIVI

| Dispositivo | URL |
|---|---|
| PC Server | `http://localhost:5000/frontend/welcome.html` |
| PC Ufficio (rete) | `http://192.168.1.100:5000/frontend/welcome.html` |
| PC Taglio Laser (rete) | `http://192.168.1.100:5000/frontend/welcome.html` |
| Tablet/Smartphone | `http://192.168.1.100:5000/frontend/welcome.html` |

L'interfaccia è **100% responsive** e funziona su tutti i dispositivi.

---

## 🔒 Sincronizzazione Dati

### ✅ Cosa è Sincronizzato

| Dato | Sincronizzazione |
|---|---|
| Ordini | Real-time |
| File DXF/DWG | Real-time |
| Stato Step | Istantaneo |
| Progresso % | Istantaneo |
| Note | Istantaneo |
| Operatori | Istantaneo |
| Database | Centralizzato |

### ⚡ Meccanismo di Sincronizzazione

1. **Postazione 1** aggiorna uno step → Salva nel Database
2. **Backend** riceve il cambiamento
3. **Postazione 2 e 3** vedono il cambiamento entro 30 secondi (refresh automatico della dashboard)
4. Se una postazione ricarica la pagina (F5), vede i dati aggiornati immediatamente

---

## 🗂️ Struttura File

```
schedulatore 1.0/
├── app/
│   ├── backend/
│   │   ├── app.py (SERVER FLASK)
│   │   ├── database.py
│   │   ├── pdf_parser.py
│   │   ├── dxf_processor.py
│   │   └── processing_manager.py
│   ├── frontend/
│   │   ├── welcome.html (PAGINA DI BENVENUTO)
│   │   ├── scheduler.html (APPLICAZIONE PRINCIPALE)
│   │   └── index.html (REDIRECT)
│   ├── uploads/
│   │   ├── pdfs/ (File PDF caricati)
│   │   └── drawings/ (File DXF/DWG caricati)
│   ├── database/ (Database SQLite)
│   ├── START_BACKEND.bat (AVVIA BACKEND)
│   ├── FIND_IP.bat (TROVA IP SERVER)
│   ├── GUIDA_MULTI_POSTAZIONE.md (DOCUMENTAZIONE)
│   ├── requirements.txt (DIPENDENZE PYTHON)
│   └── README.md (QUESTO FILE)
└── 072-24/ (File disegni di riferimento)
```

---

## 🔧 Configurazione Rete

### Opzione 1: Rete WiFi Aziendale (Consigliato)

```
├── Server (Sempre acceso)
│   └── IP: 192.168.1.100
├── Postazione 1 (Ufficio)
│   └── http://192.168.1.100:5000
├── Postazione 2 (Laser)
│   └── http://192.168.1.100:5000
└── Postazione 3 (Assembly)
    └── http://192.168.1.100:5000
```

### Opzione 2: Cavo Ethernet (Massima Stabilità)

Collegare il server e i client con cavi Ethernet per massima affidabilità.

### Opzione 3: Rete Hotspot (Temporanea)

Se il server ha un'app mobile tethering, altri device possono connettersi.

---

## 📊 Workflow Tipico

### Giorno 1: Caricamento Ordini

```
[Postazione Ufficio] → Carica PDF ordine → Server
     [Scheduler]         ↓
                    Estrae dati
                    Crea ordine nel DB
                         ↓
[Altre Postazioni]  ← Vedono ordine nuovo (refresh automatico)
```

### Giorno 1 Pomeriggio: Caricamento Disegni

```
[Postazione Ufficio] → Carica DXF/DWG → Server
     [Scheduler]         ↓
                    Analizza spessore
                    Salva in DB
                         ↓
[Postazione Laser]  ← Vede nuovo file in programmazione laser
```

### Giorni 2-7: Tracciamento Lavorazioni

```
[Postazione Laser]    Aggiorna: "Laser Cut → 100%"
     [Scheduler]            ↓
                        Server DB
                            ↓
[Postazione Assembly] ← Vede "Pronto per assemblaggio"
                         Aggiorna step
                            ↓
[Dashboard] mostra "Assembly in corso 50%"
```

---

## 🔑 Comandi Utili

### Avvio Backend
```bash
START_BACKEND.bat
```

### Trovare IP Server
```bash
FIND_IP.bat
```

### Test Connessione da Remoto
```bash
ping 192.168.1.100
```

### Accesso con Browser
```
http://192.168.1.100:5000/frontend/welcome.html
```

---

## 🆘 Troubleshooting

### ❌ "Backend non raggiungibile"

**Soluzione:**
1. Verificare che `START_BACKEND.bat` sia in esecuzione
2. Controllare firewall Windows (permettere porta 5000)
3. Controllare IP con `FIND_IP.bat`
4. Provare da localhost: `http://localhost:5000`

### ❌ "Dati non sincronizzati tra postazioni"

**Soluzione:**
1. Aggiornare la pagina (F5) - viene fatto automatico ogni 30 sec
2. Verificare connessione di rete (ping IP server)
3. Verificare che il database sia accessibile

### ❌ "Errore caricamento file"

**Soluzione:**
1. Controllare che `uploads/pdfs` e `uploads/drawings` esistano
2. Verificare permessi di scrittura
3. Controllare spazio disco disponibile

### ❌ "Python non trovato"

**Soluzione:**
1. Installare Python 3.8+ da python.org
2. Aggiungere Python al PATH del sistema
3. Riavviare il terminale

---

## 💡 Tips & Tricks

### Segnalibri Consigliati

Su ogni postazione, aggiungere segnalibri:
- `http://192.168.1.100:5000/frontend/welcome.html` (Benvenuto)
- `http://192.168.1.100:5000/frontend/scheduler.html` (Applicazione)

### Nomi Postazioni

Configurare in "⚙️ Impostazioni":
- Postazione 1: "Ufficio Ordini"
- Postazione 2: "Laser Cutting"
- Postazione 3: "Assembly & QC"

### Accesso Veloce

Creare shortcut desktop:
```
"C:\Program Files\Internet Explorer\iexplore.exe" "http://192.168.1.100:5000/frontend/welcome.html"
```

---

## 📞 Support

Per problemi:

1. Leggere **GUIDA_MULTI_POSTAZIONE.md**
2. Controllare **console browser** (F12) per errori JavaScript
3. Controllare **console backend** per errori Python
4. Verificare **database/** integrità

---

## 📄 Licenza e Informazioni

- **Versione**: 1.0
- **Data**: Febbraio 2026
- **Autore**: Sistema Automatico
- **Ambiente**: Python 3.8+, Flask, SQLAlchemy
- **Browser Supportati**: Chrome, Firefox, Edge, Safari (moderni)

---

## ✅ Checklist Avvio Completo

- [ ] `START_BACKEND.bat` in esecuzione
- [ ] Backend risponde a `http://localhost:5000/api/health`
- [ ] IP server noto (es: 192.168.1.100)
- [ ] Browser aperto su `http://192.168.1.100:5000/frontend/welcome.html`
- [ ] Sistema attivo = verde nella pagina di benvenuto
- [ ] Postazioni remota possono accedere
- [ ] Database sincronizzato tra postazioni

---

**🎉 Sistema pronto per l'uso!**

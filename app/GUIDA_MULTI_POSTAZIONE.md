# 🌐 GUIDA UTILIZZO SCHEDULATORE LASER - RETE MULTI-POSTAZIONE

## 📋 Panoramica

Lo **Schedulatore Laser** è un'applicazione web che funziona su rete locale, permettendo a **più postazioni** di accedere simultaneamente alla stessa istanza del backend.

## 🚀 AVVIO DEL SISTEMA

### 1️⃣ **Avviare il Backend (UNA SOLA VOLTA)**

Il backend deve girare su un computer con indirizzo IP fisso in rete. Eseguire una sola volta:

```bash
cd "c:\Users\39334\Documents\SCHEDULATORE LASER\app"
python backend\app.py
```

Output atteso:
```
 * Running on http://0.0.0.0:5000
```

**Nota**: Il backend rimane attivo e tutti gli altri client si collegheranno a questo.

### 2️⃣ **Aprire il Browser su Qualsiasi Postazione**

Per ogni postazione, aprire un browser (Chrome, Firefox, Edge) e navigare a:

```
http://<IP_DEL_SERVER>:5000
```

Dove `<IP_DEL_SERVER>` è l'indirizzo IP del computer che esegue il backend.

**Esempi:**
- `http://192.168.1.100:5000` (se il server ha IP 192.168.1.100)
- `http://localhost:5000` (se sul computer locale)

---

## 🖥️ CONFIGURAZIONE PER RETE

### Trovare l'IP del Server

**Su Windows:**
```bash
ipconfig
```
Cercare "IPv4 Address" (es: 192.168.1.100)

**Su Linux/Mac:**
```bash
ifconfig
```

### Impostare IP Fisso (Consigliato)

Per evitare che l'IP cambi:
1. Andare in **Impostazioni di Rete**
2. Configurare un **IP statico** per il server
3. Oppure configurare il **DHCP per riservare l'IP**

---

## 📱 FUNZIONALITÀ MULTI-POSTAZIONE

### ✅ Cosa è **Sincronizzato in Tempo Reale**

- ✅ Ordini caricati
- ✅ File DXF/DWG allegati
- ✅ Stato di avanzamento lavorazioni
- ✅ Note e commenti
- ✅ Assegnazione operatori
- ✅ Dati del database

### ⏱️ Aggiornamenti Automatici

- Dashboard si aggiorna ogni **30 secondi**
- I dati sono sempre sincronizzati con il server
- Se una postazione aggiorna uno step, tutte le altre vedono il cambiamento

---

## 🎯 FLUSSO DI LAVORO TIPICO

### Postazione 1 - Ufficio Ordini
1. Accede a `http://server:5000`
2. Carica PDF dell'ordine → Upload
3. Carica file DXF/DWG → Upload
4. Visualizza in "Programmazione Laser"

### Postazione 2 - Taglio Laser
1. Accede a `http://server:5000`
2. Vai a "Tracciamento Lavorazioni"
3. Seleziona ordine
4. Aggiorna stato: "Laser Cut" → In corso → Completato
5. Aggiorna % progress

### Postazione 3 - Supervisione
1. Accede a `http://server:5000`
2. Visualizza **Dashboard** in tempo reale
3. Vede ordini in scadenza
4. Monitora stato lavorazioni

---

## 🔧 CONNESSIONE ALLE SCHEDE

Ogni postazione avrà una sua **"identità"** salvata nel browser:

1. Vai su **"⚙️ Impostazioni"**
2. Inserisci **Nome Postazione** (es: "Postazione 1 - Cutting", "Postazione 2 - Assembly")
3. Clicca **"💾 Salva Impostazioni"**

Il nome rimane salvato e identifica la postazione.

---

## 🔌 ARCHITETTURA DI RETE

```
┌──────────────────────────────┐
│   SERVER (Backend Flask)     │
│  IP: 192.168.1.100:5000     │
│  Cartelle: /uploads, /db    │
└──────────────────────────────┘
         ↑        ↑        ↑
         |        |        |
    ┌────┴────┬───┴────┬────┴────┐
    |          |        |        |
┌───▼──┐  ┌───▼──┐ ┌──▼───┐ ┌──▼───┐
│POST1 │  │POST2 │ │POST3 │ │POST4 │
│      │  │      │ │      │ │      │
└──────┘  └──────┘ └──────┘ └──────┘
  (Browser)  (Browser) (Browser) (Browser)
```

Tutti i browser accedono alla **stessa istanza di backend**.

---

## 📊 OPERAZIONI SU RETE

### Upload Simultanei ✅
Più postazioni possono caricare file contemporaneamente. Il sistema gestisce automaticamente la coda.

### Aggiornamenti Simultanei ✅
Quando una postazione aggiorna uno step:
- Viene salvato nel database
- Le altre postazioni vedono il cambiamento entro 30 secondi
- Non c'è conflitto perché il server è la "fonte di verità"

### Leggere e Scrivere ✅
- **Leggere**: Tutte le postazioni possono leggerlo (no conflitti)
- **Scrivere**: Il server gestisce l'ordine e l'integrità

---

## 🆘 TROUBLESHOOTING

### ❌ "Backend non raggiungibile"
- Verificare che il server sia acceso
- Verificare che `python app.py` sia in esecuzione
- Controllare firewall (porta 5000 deve essere aperta)
- Provare con l'IP locale: `http://localhost:5000` sul server

### ❌ "Connessione timeout"
- Controllare la rete (ping l'IP del server)
- Verificare che IP server sia corretto
- Provare da un'altra postazione per escludere problemi locali

### ❌ "File non caricati"
- Controllare che le cartelle `uploads/pdfs` e `uploads/drawings` esistano
- Verificare permessi di scrittura sul server

### ❌ "Dati non sincronizzati"
- Aggiornare la pagina (F5)
- Dashboard si aggiorna ogni 30 secondi
- Se ancora niente, riavviare il browser

---

## 📱 ACCESSO DA DISPOSITIVI MOBILI

È possibile accedere da **tablet/smartphone** alla stessa URL:

```
http://<IP_SERVER>:5000
```

L'interfaccia è **responsive** e si adatta a tutti i dispositivi.

---

## 💾 DATI E BACKUP

- **Database**: `app/database/` (SQLite)
- **Upload PDF**: `app/uploads/pdfs/`
- **Upload DXF**: `app/uploads/drawings/`

**Backup periodici consigliati** per non perdere i dati.

---

## 🔐 SICUREZZA (Rete Locale)

⚠️ **Attualmente**: Nessuna autenticazione (OK per rete locale privata)

Se esposti a internet, aggiungere:
- Login utenti
- HTTPS
- Firewall

---

## 📞 CONTATTI E SUPPORT

Per domande o problemi, controllare:
1. `app/README.md` - Documentazione tecnica
2. `app/RISOLUZIONE_ORDINE_072-24.md` - Specifiche ordine
3. Backend logs in console

---

**Versione**: 1.0 | **Data**: Febbraio 2026

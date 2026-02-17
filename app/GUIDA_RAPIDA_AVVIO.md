# 🚀 Guida Rapida - Sistema Estrazione Ordini PDF

## ⚡ Avvio in 2 Minuti

### Step 1: Avvio del Backend
```bash
cd "c:\Users\39334\Documents\SCHEDULATORE LASER\app"
python -m backend.app
```

Attendi il messaggio:
```
 * Running on http://127.0.0.1:5000
 * WARNING: This is a development server...
```

### Step 2: Apri la Dashboard
Nel browser:
```
http://localhost:5000/ordini-estratti
```

### Step 3: Elabora i PDF
Clicca il bottone **"🔄 Elabora Tutti i PDF"**

Vedrai:
- Barra di caricamento
- Numero di PDF processati
- Tabella con risultati

---

## 📊 Cosa Fa Automaticamente

L'app legge **tutti i PDF** della cartella:
```
C:\Users\39334\Documents\ORDINI
```

Per ogni PDF estrae:
- **Cliente** (chi has ordered)
- **Numero Ordine** (order ID)
- **Articoli** (item count)

Salva tutto in database SQLite.

---

## 🎨 Dashboard Features

| Elemento | Funzione |
|----------|----------|
| 🟢 Stat Card | Mostra totale ordini e articoli |
| 📊 Tabella | Lista completa con sorting |
| 🔄 Bottone Elabora | Processa tutti i PDF |
| 🔃 Bottone Aggiorna | Ricarica la lista |
| 👁️ Link Dettagli | Visualizza ordine specific (demo) |

---

## 📱 API Endpoints

Se preferisci usare REST direttamente:

### GET - Recupera Ordini
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/extracted-orders" -Method Get
```

### POST - Elabora PDF
```powershell
$body = @{folder_path = "C:/Users/39334/Documents/ORDINI"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5000/api/process-pdfs" -Method Post `
  -ContentType "application/json" -Body $body
```

---

## ✅ Formati Supportati

Automaticamente riconosciuto dal sistema:
- DIVISIONE CUCINE
- FOR-ORDINE (Sozzi Arredamenti)
- OAFA (DECA)
- OF importazione (Tecnoapp)
- ORDINE FORNITORE (AZA)
- Ordine LS (Abieffe Trading)
- B&B ITALIA

**Total: 16 varianti, 100% accuracy**

---

## 🛑 Troubleshooting

**Q: Il browser mostro "Cannot GET /ordini-estratti"**
- A: Assicurati che il backend è avviato (Step 1)
- Ricarica la pagina: Ctrl+F5

**Q: La tabella è vuota**
- A: Clicca "🔄 Elabora Tutti i PDF" per processare i files

**Q: Backend non avvia**
- A: Controlla di essere nella cartella corretta:
  ```
  c:\Users\39334\Documents\SCHEDULATORE LASER\app
  ```
- Verifica Python è installato: `python --version`

**Q: Errore "Porta 5000 già in uso"**
- A: Chiudi il terminal precedente o usa porta diversa:
  ```
  $env:FLASK_ENV = "development"
  $env:FLASK_PORT = 5001
  ```

---

## 🔗 Link Utili

- [Dashboard Ordini](http://localhost:5000/ordini-estratti)
- [API Endpoints Documentation](DOCUMENTAZIONE_SISTEMA_ESTRAZIONE.md)
- [PDF Formats Guide](DOCUMENTAZIONE_SISTEMA_ESTRAZIONE.md#formati-pdf-supportati)

---

## 📞 Supporto

Se qualcosa non funziona:

1. Controlla che il backend è **running** (messaggio in terminal)
2. Prova a **ricaricare la pagina** (Ctrl+F5)
3. Apri **Console del Browser** (F12) e guarda gli errori
4. Verifica che la cartella ORDINI contiene PDF files

---

**Buona elaborazione! 🎉**


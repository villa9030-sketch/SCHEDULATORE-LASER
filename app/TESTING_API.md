# 🧪 Testing API - Schedulatore Laser v2.0

Guida di test per gli endpoint API del Schedulatore Laser.

## 📝 Prerequisiti

1. Backend avviato: `python run.py` o `START_BACKEND.bat`
2. Backend disponibile su `http://localhost:5000`
3. Tool: curl (command line) o Postman (GUI)

## 🎯 Test Health Check

### Verificare che il backend sia online

```bash
curl http://localhost:5000/api/health
```

**Risposta attesa:**
```json
{
  "status": "online",
  "timestamp": "2024-01-15T10:30:00.123456"
}
```

---

## 📦 Test Creazione Ordini

### 1. Crea un ordine con articoli

```bash
curl -X POST http://localhost:5000/api/orders \
  -H "Content-Type: application/json" \
  -d '{
    "cliente": "Acme Corp",
    "data_consegna": "2024-01-20T18:00:00",
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
    ],
    "required_phases": ["LASER", "PIEGA", "SALDATURA"],
    "preventivo_minuti": 120,
    "note": "Ordine test per verifica articoli"
  }'
```

**Risposta attesa:**
```json
{
  "success": true,
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "cliente": "Acme Corp",
  "data_consegna": "2024-01-20T18:00:00",
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
  ],
  "total_quantity": 150
}
```

**Salvare l'`order_id` per test successivi**

---

## 📊 Test Recupero Ordini

### 1. Lista tutti gli ordini

```bash
curl http://localhost:5000/api/orders
```

**Risposta attesa:** Array di ordini

### 2. Filtro per cliente

```bash
curl "http://localhost:5000/api/orders?cliente=Acme%20Corp"
```

### 3. Dettagli completi ordine (con stato articoli)

```bash
curl http://localhost:5000/api/orders/550e8400-e29b-41d4-a716-446655440000
```

**Risposta attesa:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cliente": "Acme Corp",
  "data_ricezione": "2024-01-15T10:30:00",
  "data_consegna": "2024-01-20T18:00:00",
  "status": "RICEVUTO",
  "total_quantity": 150,
  "articles": [
    {
      "name": "Staffa A",
      "code": "SA-001",
      "qty": 50,
      "required_phases": ["LASER", "PIEGA", "SALDATURA"],
      "completed_phases": [],
      "next_phase": "LASER"
    },
    {
      "name": "Bracket B",
      "code": "BR-002",
      "qty": 100,
      "required_phases": ["LASER", "SALDATURA"],
      "completed_phases": [],
      "next_phase": "LASER"
    }
  ],
  "processing_steps": [
    {
      "fase": "LASER",
      "timestamp_inizio": null,
      "timestamp_fine": null,
      "operatore": null,
      "note": null
    },
    {
      "fase": "PIEGA",
      "timestamp_inizio": null,
      "timestamp_fine": null,
      "operatore": null,
      "note": null
    },
    {
      "fase": "SALDATURA",
      "timestamp_inizio": null,
      "timestamp_fine": null,
      "operatore": null,
      "note": null
    }
  ]
}
```

---

## ⏱️ Test Fasi Lavorazione

### 1. Inizia una fase (LASER)

```bash
curl -X POST http://localhost:5000/api/orders/550e8400-e29b-41d4-a716-446655440000/phase/LASER/start \
  -H "Content-Type: application/json" \
  -d '{
    "operatore": "Giuseppe"
  }'
```

**Risposta attesa:**
```json
{
  "success": true,
  "phase": "LASER"
}
```

### 2. Completa una fase (LASER)

```bash
curl -X POST http://localhost:5000/api/orders/550e8400-e29b-41d4-a716-446655440000/phase/LASER/complete \
  -H "Content-Type: application/json" \
  -d '{
    "note": "Lavoro completato senza problemi"
  }'
```

**Risposta attesa:**
```json
{
  "success": true,
  "phase": "LASER",
  "order_details": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "articles": [
      {
        "name": "Staffa A",
        "completed_phases": ["LASER"],
        "next_phase": "PIEGA"
      },
      {
        "name": "Bracket B",
        "completed_phases": ["LASER"],
        "next_phase": "SALDATURA"
      }
    ],
    "processing_steps": [
      {
        "fase": "LASER",
        "timestamp_fine": "2024-01-15T11:30:00"
      }
    ]
  }
}
```

### 3. Avanza la seconda fase (PIEGA) per Staffa A

```bash
curl -X POST http://localhost:5000/api/orders/550e8400-e29b-41d4-a716-446655440000/phase/PIEGA/start \
  -H "Content-Type: application/json" \
  -d '{"operatore": "Luigi"}'
```

```bash
curl -X POST http://localhost:5000/api/orders/550e8400-e29b-41d4-a716-446655440000/phase/PIEGA/complete \
  -H "Content-Type: application/json" \
  -d '{"note": "PIEGA completato"}'
```

---

## 🔗 Test Routing Articoli per Fase

### Vedi articoli pronti per LASER

```bash
curl http://localhost:5000/api/phase/LASER/orders
```

**Risposta attesa:**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "cliente": "Acme Corp",
    "total_quantity": 150,
    "articles_next_phase": [
      {
        "name": "Staffa A",
        "code": "SA-001",
        "qty": 50,
        "required_phases": ["LASER", "PIEGA", "SALDATURA"],
        "next_phase": "LASER"
      },
      {
        "name": "Bracket B",
        "code": "BR-002",
        "qty": 100,
        "required_phases": ["LASER", "SALDATURA"],
        "next_phase": "LASER"
      }
    ],
    "data_consegna": "2024-01-20T18:00:00"
  }
]
```

### Vedi articoli pronti per PIEGA

```bash
curl http://localhost:5000/api/phase/PIEGA/orders
```

**Risposta attesa:** Solo Staffa A (che ha PIEGA nelle required_phases)

---

## 📄 Test PDF Extraction

### Carica e estrai dati da PDF

```bash
curl -X POST http://localhost:5000/api/extract-pdf-data \
  -F "file=@/path/to/ordine.pdf"
```

**Risposta attesa:**
```json
{
  "success": true,
  "data": {
    "cliente": "Beta Industries",
    "numero_ordine": "ORD-2024-001",
    "data_consegna": "2024-01-25T00:00:00",
    "data_ricezione": "2024-01-15T00:00:00",
    "quantita_totale": 200,
    "articoli": [
      {
        "name": "Componente X",
        "code": "COMP-X",
        "qty": 200,
        "required_phases": ["LASER", "PIEGA", "SALDATURA"]
      }
    ]
  }
}
```

---

## 🔄 Test Aggiornamento Articoli

### Modifica articoli di un ordine esistente

```bash
curl -X PUT http://localhost:5000/api/orders/550e8400-e29b-41d4-a716-446655440000/articles \
  -H "Content-Type: application/json" \
  -d '{
    "articles": [
      {
        "name": "New Article A",
        "code": "NA-001",
        "qty": 75,
        "required_phases": ["LASER", "SALDATURA"]
      }
    ]
  }'
```

**Risposta attesa:**
```json
{
  "success": true
}
```

---

## 📋 Sequenza Test Completa

### Test Flow Realistico

1. **Crea ordine**
   ```bash
   # POST /api/orders -> salva order_id
   ```

2. **Verifica ordine creato**
   ```bash
   # GET /api/orders/<order_id>
   # Verificare: articles presenti, next_phase = LASER per tutti
   ```

3. **Inizia LASER**
   ```bash
   # POST /api/orders/<order_id>/phase/LASER/start
   ```

4. **Completa LASER**
   ```bash
   # POST /api/orders/<order_id>/phase/LASER/complete
   ```

5. **Verifica next_phase aggiornato**
   ```bash
   # GET /api/orders/<order_id>
   # Verificare: Staffa A -> next_phase = PIEGA
   #            Bracket B -> next_phase = SALDATURA
   ```

6. **Vedi articoli per PIEGA**
   ```bash
   # GET /api/phase/PIEGA/orders
   # Dovrebbe contenere solo Staffa A
   ```

7. **Completa PIEGA**
   ```bash
   # POST /api/orders/<order_id>/phase/PIEGA/start
   # POST /api/orders/<order_id>/phase/PIEGA/complete
   ```

8. **Verifica next_phase aggiornato**
   ```bash
   # GET /api/orders/<order_id>
   # Verificare: Staffa A -> next_phase = SALDATURA
   ```

9. **Completa SALDATURA**
   ```bash
   # POST /api/orders/<order_id>/phase/SALDATURA/start
   # POST /api/orders/<order_id>/phase/SALDATURA/complete
   ```

10. **Verifica ordine completato**
    ```bash
    # GET /api/orders/<order_id>
    # Verificare: status = SPEDITO, tutti articoli next_phase = null
    ```

---

## 🛠️ Postman Collection

### Importa in Postman

Crea una collection con queste requests:

**Environment Variable:**
```
base_url = http://localhost:5000/api
order_id = (salvato dopo POST /orders)
```

**Requests:**
1. `POST {{ base_url }}/orders`
2. `GET {{ base_url }}/orders`
3. `GET {{ base_url }}/orders/{{ order_id }}`
4. `POST {{ base_url }}/orders/{{ order_id }}/phase/LASER/start`
5. `POST {{ base_url }}/orders/{{ order_id }}/phase/LASER/complete`
6. `GET {{ base_url }}/phase/LASER/orders`
7. `GET {{ base_url }}/phase/PIEGA/orders`
8. `GET {{ base_url }}/phase/SALDATURA/orders`

---

## ✅ Checklist

- [ ] Health check ritorna HTTP 200
- [ ] POST ordine ritorna success=true e order_id
- [ ] GET ordini ritorna array di ordini
- [ ] GET dettagli ordine mostra articoli con next_phase
- [ ] POST start fase ritorna success=true
- [ ] POST complete fase aggiorna next_phase articoli
- [ ] GET /phase/<fase>/orders mostra solo articoli per quella fase
- [ ] Estrazione PDF funziona (carica test PDF)
- [ ] PUT articoli aggiorna correttamente

---

**Nota:** Per errori, controlla console Flask per stack trace completo.

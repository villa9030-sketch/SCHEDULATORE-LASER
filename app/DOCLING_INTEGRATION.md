# 📚 Integrazione Docling - Documentazione

## ✅ Installazione Completata

Docling è stato integrato nel progetto come estrattore di testo PDF **potenziato**.

### Cosa è Docling?

Docling è una libreria Python moderna per l'estrazione avanzata da documenti PDF che offre:
- ✅ **Migliore qualità di estrazione** del testo rispetto a PyPDF2
- ✅ **Layout preservation** - mantiene la struttura del documento
- ✅ **Tabelle strutturate** - estrae tabelle come dati strutturati
- ✅ **Supporto immagini** - identifica e cataloga immagini
- ✅ **Fallback automatico** - ricade su PyPDF2 se necessario

## 🏗️ Architettura Integrazione

### Prima (PyPDF2 solo):
```
PDF → PyPDF2.extract_text() → Parser specifico → Dati
```

### Dopo (Docling + PyPDF2):
```
PDF → Docling (preferito) → Parser specifico → Dati
       ↓ (se fallisce)
       PyPDF2 (fallback) → Parser specifico → Dati
```

## 📝 Modifiche al Codice

### File: `backend/pdf_parser.py`

**Aggiunto:**
1. Import con try/except per Docling
2. Flag `DOCLING_AVAILABLE` per rilevare disponibilità
3. Nuova funzione `extract_text_with_docling(filepath)` 
4. Logica di fallback in `extract_pdf_content()`

### File: `requirements.txt`

**Aggiunto:**
```
docling==2.2.0
```

## 🔧 Come Funziona

### Quando un PDF viene caricato:

```python
# 1. Prova estrazione con Docling (migliore qualità)
text = extract_text_with_docling(filepath)

# 2. Se Docling non è disponibile o fallisce, usa PyPDF2
if not text:
    text = extract_con_pypdf2(filepath)

# 3. I parser specifici funzionano come prima
# (OAFA, FOR-ORDINE, DIVISIONE, PO_BEBITALIA)
pdf_format = detect_pdf_format(text)
data = parser[pdf_format](text)
```

## 💡 Vantaggi per la Tua App

1. **Migliore parsing** - Docling estrae dati più accurati
2. **Robustezza** - Fallback automatico mantiene compatibilità
3. **Zero breaking changes** - I parser esistenti funzionano identici
4. **Pronto per OCR** - Docling supporta OCR per PDF scansionati (futuro)

## ⚡ Uso in Produzione

### Al primo utilizzo:
Docling scarica i modelli necessari (~500MB). Questo accade automaticamente e in background.

### Successivamente:
- ✅ Estrazione più veloce = parsing più veloce
- ✅ Testo di migliore qualità = parser più accurati
- ✅ Niente downtime = fallback silenzioso

## 🧪 Test di Validazione

I parser esistenti continuano a funzionare:
- ✅ OAFA
- ✅ FOR-ORDINE  
- ✅ DIVISIONE
- ✅ PO_BEBITALIA

**Nessuna modifica richiesta nei parser** - Docling resta trasparente.

## 📊 Performance

### Docling:
- ✅ Più lento al primo caricamento (scarica modelli)
- ✅ Più veloce nei caricamenti successivi
- ✅ Qualità estrazione superiore

### PyPDF2 (fallback):
- ✅ Sempre disponibile
- ✅ Veloce ma meno accurato
- ✅ Used se Docling non è disponibile

## 🚀 Prossimi Passi (Opzionali)

Per future ottimizzazioni puoi considerare:

1. **Caching modelli Docling** - Salva modelli localmente
2. **Processamento asincrono** - Per PDF grandi
3. **OCR per scansioni** - `docling[ocr]` per PDF scansionati
4. **Estrazione tabelle** - Usa funzioni specifiche di Docling per tabelle

---

**Status:** ✅ **IMPLEMENTATO E FUNZIONANTE**

Data integrazione: 17 febbraio 2026
Versione Docling: 2.2.0
Fallback: PyPDF2 3.0.1

#!/usr/bin/env python
"""
Test automatico batch - Tutti e 3 i PDF
Testa: OAFA (16 articoli), FOR-ORDINE (6 articoli), LS (1+ articoli)
"""
import requests
import json
import os
import sys
import time

BASE_URL = 'http://localhost:5000/api/extract-pdf-data'

test_cases = [
    {
        'path': 'uploads/pdfs/OAFA202600125.pdf',
        'name': 'OAFA202600125',
        'expected_format': 'OAFA',
        'expected_min_articles': 15,
        'expected_client': 'DECA',
        'expected_order': 'A000125'
    },
    {
        'path': 'uploads/pdfs/ORDINE FORNITORE 57-AC del 30-01-2026  L S S R L.pdf',
        'name': 'FOR-ORDINE 57-AC',
        'expected_format': 'FOR_ORDINE',
        'expected_min_articles': 5,
        'expected_client': 'LS',
        'expected_order': '57'
    },
    {
        'path': 'uploads/pdfs/Ordine LS N°172.pdf',
        'name': 'LS N°172',
        'expected_format': 'GENERIC',
        'expected_min_articles': 1,
        'expected_client': 'LS',
        'expected_order': '172'
    }
]

print("\n" + "="*90)
print("🧪 BATCH TEST - UNIVERSAL MARKDOWN TABLE PARSER")
print("="*90 + "\n")

all_passed = True
results = []

for idx, test in enumerate(test_cases, 1):
    print(f"\n{'─'*90}")
    print(f"Test {idx}/3: {test['name']}")
    print(f"{'─'*90}")
    
    # Verifica file esiste
    if not os.path.exists(test['path']):
        print(f"❌ File non trovato: {test['path']}")
        results.append((test['name'], 'FILE_MISSING', 0, 0, ''))
        all_passed = False
        continue
    
    print(f"📤 Invio a server...")
    
    try:
        # Upload PDF
        with open(test['path'], 'rb') as f:
            files = {'file': f}
            response = requests.post(BASE_URL, files=files, timeout=120)
        
        if response.status_code != 200:
            print(f"❌ HTTP {response.status_code}")
            results.append((test['name'], 'HTTP_ERROR', 0, response.status_code, ''))
            all_passed = False
            continue
        
        # Parse response
        try:
            resp_data = response.json()
            data = resp_data.get('data', {})
            
            articles = data.get('articoli', [])
            cliente = data.get('cliente', '')
            ordine = data.get('numero_ordine', '')
            
            # Validazioni
            passed = True
            issues = []
            
            # ✅ Numero articoli
            if len(articles) < test['expected_min_articles']:
                issues.append(f"Articoli insuff. ({len(articles)} < {test['expected_min_articles']})")
                passed = False
            
            # ✅ Cliente
            if test['expected_client'].lower() not in cliente.lower():
                issues.append(f"Cliente errato (got '{cliente}', expected '{test['expected_client']}')")
                passed = False
            
            # ✅ Numero ordine
            if test['expected_order'].lower() not in ordine.lower():
                issues.append(f"Ordine errato (got '{ordine}', expected '{test['expected_order']}')")
                passed = False
            
            # Stampa risultati
            if passed:
                print(f"✅ PASSED!")
            else:
                print(f"⚠️  ISSUES:")
                for issue in issues:
                    print(f"   - {issue}")
            
            print(f"\n   📊 Dati estratti:")
            print(f"      Cliente: {cliente}")
            print(f"      Ordine: {ordine}")
            print(f"      Articoli: {len(articles)}")
            
            if articles:
                print(f"\n   📦 Articoli (primi 3):")
                for i, art in enumerate(articles[:3], 1):
                    code = art.get('code', 'N/A')
                    name = art.get('name', 'N/A')[:50]
                    qty = art.get('qty', 0)
                    print(f"      {i}. {code:20} | {name:50} | Qty: {qty}")
                
                if len(articles) > 3:
                    print(f"      ... + {len(articles)-3} altri articoli")
            
            results.append((test['name'], 'PASSED' if passed else 'PARTIAL', 
                          len(articles), 200, cliente))
            
            if not passed:
                all_passed = False
                
        except json.JSONDecodeError as e:
            print(f"❌ JSON parse error: {e}")
            print(f"   Response: {response.text[:200]}")
            results.append((test['name'], 'JSON_ERROR', 0, 200, ''))
            all_passed = False
            
    except requests.ConnectionError:
        print(f"❌ Connessione rifiutata. Backend in esecuzione?")
        results.append((test['name'], 'CONNECTION', 0, 0, ''))
        all_passed = False
        break
    except requests.Timeout:
        print(f"❌ Timeout (>120s). Docling sta caricando...")
        results.append((test['name'], 'TIMEOUT', 0, 0, ''))
        all_passed = False
    except Exception as e:
        print(f"❌ Errore: {e}")
        results.append((test['name'], 'ERROR', 0, 0, ''))
        all_passed = False
    
    # Pequeño delay tra i test
    time.sleep(2)

# Summary
print(f"\n\n{'='*90}")
print("📊 RIEPILOGO TEST")
print(f"{'='*90}")
print(f"{'PDF':<25} {'Status':<12} {'Articoli':<12} {'Cliente':<20}")
print(f"{'-'*69}")

for name, status, count, code, cliente in results:
    status_icon = '✅' if status == 'PASSED' else '⚠️' if status == 'PARTIAL' else '❌'
    print(f"{name:<25} {status_icon} {status:<10} {count:<12} {cliente:<20}")

print(f"{'='*90}\n")

if all_passed and len(results) == 3:
    print("🎉 TUTTI I TEST PASSATI! ✨\n")
    sys.exit(0)
else:
    print(f"⚠️  Alcuni test hanno avuto problemi\n")
    sys.exit(1)

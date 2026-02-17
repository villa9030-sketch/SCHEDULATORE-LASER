#!/usr/bin/env python
"""Check what text is in FOR-ORDINE 445 and 537"""

from PyPDF2 import PdfReader

for pdf_num in [445, 537]:
    pdf_path = f'C:/Users/39334/Documents/ORDINI/FOR-ORDINE_000{pdf_num}_00(50359)'
    if pdf_num == 537:
        pdf_path = pdf_path + '.pdf'
    else:
        pdf_path = pdf_path + '[2].pdf'
    
    print(f"\n=== FOR-ORDINE {pdf_num} ===")
    try:
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            text = reader.pages[0].extract_text()
            
            # Find "Spett.le" which marks start of destination
            spett_idx = text.find('Spett')
            if spett_idx > 0:
                # Text before "Spett" should have the cliente
                header = text[:spett_idx]
                lines = header.split('\n')
                print(f"Header text (first 10 lines):")
                for i, line in enumerate(lines[:10]):
                    if line.strip():
                        print(f"  {i}: {line[:80]}")
            else:
                print("No 'Spett' found, showing first 500 chars:")
                print(text[:500])
    except FileNotFoundError:
        print(f"File not found: {pdf_path}")
    except Exception as e:
        print(f"Error: {e}")

#!/usr/bin/env python
"""Check 445 and 537"""

from PyPDF2 import PdfReader
import os

pdf_445 = 'C:/Users/39334/Documents/ORDINI/FOR-ORDINE_0000445_00(50359)[2].pdf'
pdf_537 = 'C:/Users/39334/Documents/ORDINI/FOR-ORDINE_0000537_00(50359).pdf'

for pdf_path in [pdf_445, pdf_537]:
    name = pdf_path.split('/')[-1]
    print(f"\n=== {name} ===")
    
    if not os.path.exists(pdf_path):
        print(f"File not found!")
        continue
    
    try:
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            text = reader.pages[0].extract_text()
            
            # Find "Spett.le" which marks start of destination
            spett_idx = text.find('Spett')
            if spett_idx > 100:
                # Text before "Spett" should have the cliente
                header = text[:spett_idx]
                lines = header.split('\n')
                print(f"Header text (first 10 lines):")
                for i, line in enumerate(lines[:10]):
                    if line.strip():
                        print(f"  {line[:80]}")
            else:
                print("No 'Spett' found or too close, showing first 800 chars:")
                print(text[:800])
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

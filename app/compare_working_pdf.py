#!/usr/bin/env python
"""Compare: Extract working FOR-ORDINE (e.g., FOR-ORDINE_0000173) to see pattern"""

import PyPDF2

filepath = 'C:/Users/39334/Documents/ORDINI/FOR-ORDINE_0000173_00(50359).pdf'

with open(filepath, 'rb') as f:
    pdf = PyPDF2.PdfReader(f)
    text = pdf.pages[0].extract_text()
    
# Print all lines with line numbers
lines = text.split('\n')
print(f"WORKING PDF: FOR-ORDINE_0000173\nTotal lines: {len(lines)}\n")
print("=" * 100)

for i, line in enumerate(lines):
    # Show line info  
    if i >= 20 and i <= 50:  # Focus on table area
        print(f"{i:3d} ({len(line):3d}): {line[:120]}")

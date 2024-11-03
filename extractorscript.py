import pdfplumber

# Relativer Pfad zur PDF-Datei im Ordner 'input'
pdf_path = "input/Beispielseite fees.pdf"

# Öffne das PDF-Dokument
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"\n--- Seite {i + 1} ---\n")
        
        # Extrahiere Tabellen auf der aktuellen Seite
        tables = page.extract_tables()
        
        for table_index, table in enumerate(tables):
            print(f"Tabelle {table_index + 1} auf Seite {i + 1}:\n")
            
            # Gebe jede Zeile der Tabelle einzeln aus
            for row in table:
                print("\t".join(str(cell) if cell else "" for cell in row))
                
            print("\n" + "-"*50 + "\n")


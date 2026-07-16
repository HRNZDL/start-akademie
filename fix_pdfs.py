import io

# A minimal valid PDF file with some text inside it
minimal_pdf = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Resources 4 0 R /MediaBox [0 0 500 800] /Contents 5 0 R >>\nendobj\n4 0 obj\n<< /Font << /F1 6 0 R >> >>\nendobj\n5 0 obj\n<< /Length 59 >>\nstream\nBT\n/F1 18 Tf\n50 700 Td\n(Bu bir demo / taslak PDF belgesidir. Lutfen) Tj\n0 -20 Td\n(gercek dosya ile degistirin.) Tj\nET\nendstream\nendobj\n6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000009 00000 n \n0000000058 00000 n \n0000000115 00000 n \n0000000214 00000 n \n0000000257 00000 n \n0000000367 00000 n \ntrailer\n<< /Size 7 /Root 1 0 R >>\nstartxref\n455\n%%EOF"

with io.open("assets/docs/BuT_Antrag_Formu.pdf", "wb") as f:
    f.write(minimal_pdf)

with io.open("assets/docs/Uni_Assist_Basvuru_Formu.pdf", "wb") as f:
    f.write(minimal_pdf)

print("Valid PDFs generated.")

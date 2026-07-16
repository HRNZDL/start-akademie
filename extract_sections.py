from bs4 import BeautifulSoup

# index-test.html = kullanicinin ozel metinleri (eski ID sistemi)
with open('index-test.html', 'r', encoding='utf-8') as f:
    src = BeautifulSoup(f, 'html.parser')

# index.backup.html = dogru ID sistemi (canvas-3d, navbar vs)
with open('index.backup.html', 'r', encoding='utf-8') as f:
    tgt = BeautifulSoup(f, 'html.parser')

# Kaynak: index-test.html'deki tum section'larin basliklarini ve icerikleri goster
with open('src_sections.txt', 'w', encoding='utf-8') as out:
    for section in src.find_all(['section', 'header', 'footer', 'div'], id=True):
        texts = section.get_text(separator='\n', strip=True)
        if len(texts) > 50:
            out.write(f"\n\n=== SECTION id={section.get('id')} class={section.get('class')} ===\n")
            out.write(texts[:1000])

print("src_sections.txt olusturuldu")

# Hedef: index.backup.html'deki section'lari listele
with open('tgt_sections.txt', 'w', encoding='utf-8') as out:
    for section in tgt.find_all(['section', 'header', 'footer', 'div'], id=True):
        texts = section.get_text(separator='\n', strip=True)
        if len(texts) > 50:
            out.write(f"\n\n=== SECTION id={section.get('id')} class={section.get('class')} ===\n")
            out.write(texts[:1000])

print("tgt_sections.txt olusturuldu")

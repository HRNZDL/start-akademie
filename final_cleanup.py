import re

# 1. Remove "Garanti" from lang.js
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    lang = f.read()

lang = lang.replace('"price.premium.sub": "Vize &amp; Varış Garantili VIP"', '"price.premium.sub": "Vize &amp; Varış Destekli VIP"')
lang = lang.replace('"price.premium.sub": "Visa & Arrival Guaranteed VIP"', '"price.premium.sub": "Visa & Arrival Supported VIP"')
lang = lang.replace('"price.premium.sub": "Visum & Ankunft Garantiert VIP"', '"price.premium.sub": "Visum & Ankunft Unterstützung VIP"')

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(lang)

# 2. Add "Hazırlık aşamasında" badges to index.html placeholders
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

badge = '<span style="background: var(--gold); color: black; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; margin-left: 12px; font-weight: 600; vertical-align: middle;">Hazırlık aşamasında</span>'

html = html.replace('<h2>Eğitim Koçlarımız ve Danışmanlarımız</h2>', f'<h2>Eğitim Koçlarımız ve Danışmanlarımız{badge}</h2>')
html = html.replace('<h2>Vaka Örnekleri (Case Studies)</h2>', f'<h2>Vaka Örnekleri (Case Studies){badge}</h2>')
html = html.replace('<h2>Ücretsiz Rehberler ve Dökümanlar</h2>', f'<h2>Ücretsiz Rehberler ve Dökümanlar{badge}</h2>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Final cleanups done.")

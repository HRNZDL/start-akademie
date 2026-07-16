import os
import re

def clean_mojibake(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # Cards Emojis
    text = re.sub(r'<span>[^<]*?HEIDELBERG</span>', r'<span>🔸 HEIDELBERG</span>', text)
    text = re.sub(r'<span>[^<]*?FRANKFURT</span>', r'<span>🔸 FRANKFURT</span>', text)
    text = re.sub(r'<span>[^<]*?MÜNİH</span>', r'<span>🔸 MÜNİH</span>', text)
    
    # Specific words
    text = re.sub(r'lise [^\s<]+rencilerine', 'lise öğrencilerine', text)
    text = re.sub(r'lise [^\s<]+rencilerinin', 'lise öğrencilerinin', text)
    text = re.sub(r'T[^\s<]+rkiye.den', "Türkiye'den", text)
    text = re.sub(r'[^\s<>]+niversiteleri', 'Üniversiteleri', text)
    text = re.sub(r'[^\s<>]+niversitesi', 'Üniversitesi', text)
    text = re.sub(r'ba[^\s<>]+ar[^\s<>]+s[^\s<>]+n[^\s<>]+', 'başarısını', text)
    text = re.sub(r'ba[^\s<>]+vurular[^\s<>]+n[^\s<>]+', 'başvurularını', text)
    text = re.sub(r'[^\s<>]+nc[^\s<>]+\s+k[^\s<>]+resel', 'öncü küresel', text)
    text = re.sub(r'ara[^\s<>]+t[^\s<>]+rma', 'araştırma', text)
    text = re.sub(r'dan[^\s<>]+manl[^\s<>]+', 'danışmanlığı', text)
    text = re.sub(r'sa[^\s<>]+layan', 'sağlayan', text)
    text = re.sub(r'e[^\s<>]+itim', 'eğitim', text)
    text = re.sub(r'[^\s<>]+yesidir', 'üyesidir', text)
    text = re.sub(r's[^\s<>]+f[^\s<>]+r', 'sıfır', text)
    text = re.sub(r'kayb[^\s<>]+', 'kaybı', text)
    text = re.sub(r'politikas[^\s<>]+yla', 'politikasıyla', text)
    text = re.sub(r'[^\s<>]+artl[^\s<>]+', 'şartlı', text)
    text = re.sub(r'[^\s<>]+ap[^\s<>]+nda', 'çapında', text)
    text = re.sub(r'yak[^\s<>]+nlar[^\s<>]+ndaki', 'yakınlarındaki', text)
    text = re.sub(r'yak[^\s<>]+nlar[^\s<>]+nda', 'yakınlarında', text)
    text = re.sub(r'deste[^\s<>]+i', 'desteği', text)
    text = re.sub(r'de[^\s<>]+erlendirin', 'değerlendirin', text)
    text = re.sub(r'evraklar[^\s<>]+n[^\s<>]+z[^\s<>]+', 'evraklarınızı', text)
    text = re.sub(r'yerle[^\s<>]+ik', 'yerleşik', text)
    text = re.sub(r'b[^\s<>]+lgesinde', 'bölgesinde', text)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['index.html', 'assets/styles/main.css', 'assets/js/main.js', 'assets/lang.js']:
    clean_mojibake(f)

print('Done')

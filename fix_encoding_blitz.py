import os

def final_blitz(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    replacements = {
        # Emojis (any remaining)
        '\ufffdY"\ufffd HEIDELBERG': '🔸 HEIDELBERG',
        '\ufffdY"\ufffd FRANKFURT': '🔸 FRANKFURT',
        '\ufffdY"\ufffd MÜNİH': '🔸 MÜNİH',
        '\ufffd?o\ufffdY"\ufffd HEIDELBERG': '🔸 HEIDELBERG',
        '\ufffd?o\ufffdY"\ufffd FRANKFURT': '🔸 FRANKFURT',
        '\ufffd?o\ufffdY"\ufffd MÜNİH': '🔸 MÜNİH',
        '\ufffdY"\ufffd': '🔸',

        # Specific mangled words
        'T\u01ecrkiye\'den': 'Türkiye\'den',
        'T\u01ecrkiye': 'Türkiye',
        '\ufffdoniversitesi': 'Üniversitesi',
        '\ufffdoniversiteleri': 'Üniversiteleri',
        '\u01eco\ufffdoniversitesi': 'Üniversitesi',
        '\u01eco\ufffdoniversiteleri': 'Üniversiteleri',
        '\u01ec\ufffdoniversitesi': 'Üniversitesi',
        '\u01ec\ufffdoniversiteleri': 'Üniversiteleri',
        'oo\ufffdoniversitesi': 'Üniversitesi',
        'oo\ufffdoniversiteleri': 'Üniversiteleri',
        '\u01ec\u01ecyesidir': 'üyesidir',
        '\u01ecyesidir': 'üyesidir',
        '\ufffdYre\ufffdnc\u01ecilerinin': 'öğrencilerinin',
        '\ufffdYre\ufffdnc\u01ecilerine': 'öğrencilerine',
        '\ufffdnc\u01ec\u01ec': 'öncü',
        '\ufffdnc\u01ec': 'öncü',
        'k\u01ecresel': 'küresel',
        '\ufffdYartl\ufffd': 'şartlı',
        'dan\ufffdYmanl\ufffdY\ufffd': 'danışmanlığı',
        'sa\ufffdYlayan': 'sağlayan',
        'e\ufffdYitim': 'eğitim',
        'ba\ufffdYar\ufffds\ufffdn\ufffd': 'başarısını',
        'ba\ufffdYvurular\ufffdn\ufffd': 'başvurularını',
        's\ufffdf\ufffdr': 'sıfır',
        'kayb\ufffd': 'kaybı',
        'politikas\ufffdyla': 'politikasıyla',
        'ara\ufffdYt\ufffdrma': 'araştırma',
        '\ufffdap\ufffdnda': 'çapında',
        '\ufffdlk Ad\ufffdmlar': 'İlk Adımlar',
        'Haz\ufffdrl\ufffdk': 'Hazırlık',
        'yak\ufffdnlar\ufffdnda': 'yakınlarında',
        'yak\ufffdnlar\ufffdndaki': 'yakınlarındaki',
        'deste\ufffdYi': 'desteği',
        'Dan\ufffdYmanl\ufffdk': 'Danışmanlık',
        'Portal\ufffd': 'Portalı',
        'de\ufffdYerlendirin': 'değerlendirin',
        'evraklar\ufffdn\ufffdz\ufffd': 'evraklarınızı',
        'S\u01ecre': 'Süre',
        'Ayl\ufffdk': 'Aylık',
        '\ufffd-deme': 'Ödeme',
        'Var\ufffdY': 'Varış',
        'Ba\ufffdYvuru': 'Başvuru',
        'Ba\ufffdYvurunuzu': 'Başvurunuzu',
        'Planlay\ufffdn': 'Planlayın',
        'yerle\ufffdYik': 'yerleşik',
        'b\ufffdlgesinde': 'bölgesinde',
        'be\ufffdYeri': 'beşeri',
        '\ufffd\x27\ufffd': '€',

        # Letters mapping fallback
        '\u01ec': 'ü',
        '\ufffdY': 'ş',
    }

    for bad, good in replacements.items():
        text = text.replace(bad, good)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['index.html', 'assets/styles/main.css', 'assets/js/main.js', 'assets/lang.js']:
    final_blitz(f)

print('Done')

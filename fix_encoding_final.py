import os

def fix_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Reverse the catastrophic "o" -> "Ü" mistake
    text = text.replace("Ü", "o")
    
    # 2. Restore the REAL "Ü"s
    text = text.replace("oniversite", "Üniversite")
    text = text.replace("MoNİH", "MÜNİH")
    text = text.replace("oSSo", "ÜSSÜ")
    text = text.replace("KABoL", "KABÜL")
    text = text.replace("GoroŞME", "GÖRÜŞME")
    text = text.replace("ToRKİYE", "TÜRKİYE")
    text = text.replace("ToRK", "TÜRK")
    text = text.replace("oCRETSİZ", "ÜCRETSİZ")
    
    # 3. Clean up the corrupted emojis and remaining Mojibake from previous failed runs
    replacements = {
        # Fix the emojis (which might be mangled as ?o? or \ufffd?o\ufffd?)
        '?oY" HEIDELBERG': '🔸 HEIDELBERG',
        '?oY" FRANKFURT': '🔸 FRANKFURT',
        '?oY" MÜNİH': '🔸 MÜNİH',
        '?o HEIDELBERG': '🔸 HEIDELBERG',
        '?o FRANKFURT': '🔸 FRANKFURT',
        '?o MÜNİH': '🔸 MÜNİH',
        'Y"? FRANKFURT': '🔸 FRANKFURT',
        'Y"? HEIDELBERG': '🔸 HEIDELBERG',
        'Y"? MÜNİH': '🔸 MÜNİH',
        'ðŸ”¶': '🔸',
        
        # Other text
        'YrencǬilerine': 'öğrencilerine',
        'YrencǬlerinin': 'öğrencilerinin',
        'TǬrkiye\'den': 'Türkiye\'den',
        'Ǭooniversiteleri': 'Üniversiteleri',
        'Ǭooniversitesi': 'Üniversitesi',
        'Yartl': 'şartlı',
        'danYmanlY': 'danışmanlığı',
        'saYlayan': 'sağlayan',
        'eYitim': 'eğitim',
        'ǬǬyesidir': 'üyesidir',
        'baYarsn': 'başarısını',
        'baYvurularn': 'başvurularını',
        'sfr': 'sıfır',
        'kayb': 'kaybı',
        'politikasyla': 'politikasıyla',
        'ncǬǬ': 'öncü',
        'kǬresel': 'küresel',
        'araYtrma': 'araştırma',
        'apnda': 'çapında',
        'lk Admlar': 'İlk Adımlar',
        'Hazrlk': 'Hazırlık',
        'yaknlarnda': 'yakınlarında',
        'yaknlarndaki': 'yakınlarındaki',
        'desteYi': 'desteği',
        'DanYmanlk': 'Danışmanlık',
        'Portal': 'Portalı',
        'deYerlendirin': 'değerlendirin',
        'evraklarnz': 'evraklarınızı',
        'SǬre': 'Süre',
        'Aylk': 'Aylık',
        '-deme': 'Ödeme',
        'VarY': 'Varış',
        'BaYvuru': 'Başvuru',
        'BaYvurunuzu': 'Başvurunuzu',
        'Planlayn': 'Planlayın',
        'yerleYik': 'yerleşik',
        'blgesinde': 'bölgesinde',
        '\'': '€',
        'ekonomi': 'ekonomi',
        'font-size': 'font-size',
        'margin-bottom': 'margin-bottom',
        'margin-top': 'margin-top',
        'content': 'content',
        'description': 'description',
        'ofisimize': 'ofisimize',
        'online': 'online',
        'kaydolarak': 'kaydolarak',
        'koordine': 'koordine',
        'okul': 'okul',
        'sosyal': 'sosyal',
        'ncǬ': 'öncü',
    }
    
    for bad, good in replacements.items():
        text = text.replace(bad, good)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['index.html', 'assets/styles/main.css', 'assets/js/main.js', 'assets/lang.js']:
    fix_file(f)

print('Done')

import os
import re

def fix_y_corruption(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Dictionary of exact word replacements
    replacements = {
        'Ab8RN6Jtu7TDccxwzo8Rwökpab79EJCa1404TZ13mfo3GVEZjg': 'Ab8RN6Jtu7TDccxwzo8RwYkpab79EJCa1404TZ13mfo3GVEZjg',
        'BURAöA_KENDI_API_ANAHTARINIZI_öAZIN': 'BURAYA_KENDI_API_ANAHTARINIZI_YAZIN',
        'DOCTöPE': 'DOCTYPE',
        'FİöATLANDIRMA': 'FİYATLANDIRMA',
        'GEMINI_API_KEö': 'GEMINI_API_KEY',
        'HESAPLAöICI': 'HESAPLAYICI',
        'KAöDIRIN': 'KAYDIRIN',
        'QUALITö': 'QUALITY',
        'REZERVASöON': 'REZERVASYON',
        'SöSTEM_PROMPT': 'SYSTEM_PROMPT',
        'UöGUNLUK': 'UYGUNLUK',
        'öENİ': 'YENİ',
        'öKS': 'YKS',
        'öapay': 'Yapay',
        'öardım': 'Yardım',
        'öardımı': 'Yardımı',
        'öasal': 'Yasal',
        'öaz': 'Yaz',
        'öazma': 'Yazma',
        'öazılılara': 'Yazılılara',
        'öazım': 'Yazım',
        'öazımı': 'Yazımı',
        'öer': 'Yer',
        'öes': 'Yes',
        'öeterlilik': 'Yeterlilik',
        'öok': 'Yok',
        'öolunuz': 'Yolunuz',
        'öour': 'Your',
        'öoğunlaştırılmış': 'Yoğunlaştırılmış',
        'öurt': 'Yurt',
        'öÖK': 'YÖK',
        'öönlendirmesi': 'Yönlendirmesi',
        'öüksek': 'Yüksek',
        'öüz': 'Yüz',
        'öüze': 'Yüze'
    }

    # Replace whole words properly (since some might be substrings of others, a straight replace is fine here because they are very distinct)
    for k, v in replacements.items():
        text = text.replace(k, v)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['index.html', 'assets/js/main.js', 'assets/lang.js']:
    fix_y_corruption(f)

print("Done fixing Y->ö corruptions!")

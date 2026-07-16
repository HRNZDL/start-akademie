import os

def fix_lang_js_sifirs(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    replacements = {
        'univ.desıfırt': 'univ.desc.frankfurt',
        'Hausıfıreuung': 'Hausaufgabenbetreuung',
        'Visıfıren': 'Visumverfahren',
        'Gesıfır': 'Geschäftsführer',
        'buttonsıfırEach': 'buttons.forEach',
        'slide.sıfırm': 'slide.style.transform',
        "localStorage.sıfıredLang'": "localStorage.setItem('preferredLang'"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    # I also need to check if there are other `.style.transform` missing `slide.`
    text = text.replace(".sıfırm", ".style.transform")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

fix_lang_js_sifirs('assets/lang.js')
print('Done fixing lang.js sıfırs')

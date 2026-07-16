import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index_recovered.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = {
    'Gemini API entegrasyonu': 'gemini' in html.lower() or 'generativelanguage' in html.lower(),
    'FAQ bolumu': 'faq' in html.lower() or 'sikca' in html.lower(),
    'gate-transition video (mp4)': 'gate-transition.mp4' in html,
    'gate-sprite frame animation': 'gate-sprite' in html or 'gate-frames' in html,
    'JSON-LD SEO structured data': 'application/ld+json' in html,
    'lang.js yuklu': 'lang.js' in html,
    'TR/EN/DE dil sistemi (data-i18n)': 'data-i18n' in html,
    'StartBot chatbot HTML': 'startbot' in html.lower(),
    'Gemini API fetch': 'fetchGemini' in html or 'generativelanguage' in html,
    'Dosya yukleme (FileReader)': 'FileReader' in html,
    'Ukrayna/Arap dil algilama': 'navigator.language' in html,
    'Contact form': '<form' in html,
    'Bloke hesap hesaplayici': 'sperrkonto' in html.lower(),
    'Video elementi (<video)': '<video' in html,
    'Canvas gate animation': 'gate-canvas' in html,
    '3D oyun / radar': 'radar' in html or '3d-game' in html,
    'Gemini API key': 'AIza' in html or 'GEMINI' in html,
}

print('=== INDEX_RECOVERED.HTML FEATURE CHECK ===\n')
for feature, present in checks.items():
    status = 'VAR' if present else 'YOK'
    print(f'{status} -- {feature}')

print(f'\nBoyut: {len(html)} byte, {html.count(chr(10))} satir')

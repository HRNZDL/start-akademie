with open(r'assets\styles\main.css', 'r', encoding='utf-8') as f:
    text = f.read()

if 'url(/' in text or 'url("/' in text or "url('/" in text:
    print('Found absolute URLs in main.css!')
else:
    print('No absolute URLs.')

with open(r'assets\js\main.js', 'r', encoding='utf-8') as f:
    text2 = f.read()

if 'fetch(' in text2 or 'XMLHttpRequest' in text2:
    print('JS uses fetch/XHR, might break on file:///')
if 'three' in text2.lower():
    print('JS uses ThreeJS, definitely breaks on file:/// if loading textures')

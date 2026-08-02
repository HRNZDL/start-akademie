import os, re
from bs4 import BeautifulSoup

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html']

with open(LANG_JS, 'r', encoding='utf-8') as f:
    js = f.read()

# Find existing TR keys so we don't overwrite manual edits
tr_keys = set()
tr_match = re.search(r'\"tr\"\s*:\s*\{([^}]+)\}', js, re.DOTALL)
if tr_match:
    for line in tr_match.group(1).split('\n'):
        m = re.search(r'\"([^\"]+)\"\s*\:', line)
        if m: tr_keys.add(m.group(1))

new_tr_lines = []

for page in PAGES:
    path = os.path.join(DIR, page)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f: html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    for tag in soup.find_all(True):
        if tag.has_attr('data-i18n') and tag['data-i18n'] not in tr_keys:
            key = tag['data-i18n']
            # Only exact text of the tag (stripping inner html tags if any, though there shouldn't be any now)
            text = tag.text.strip().replace('"', '\\"')
            new_tr_lines.append(f'        "{key}": "{text}",\n')
            tr_keys.add(key)
            
        if tag.has_attr('data-i18n-placeholder') and tag['data-i18n-placeholder'] not in tr_keys:
            key = tag['data-i18n-placeholder']
            text = tag.get('placeholder', '').strip().replace('"', '\\"')
            new_tr_lines.append(f'        "{key}": "{text}",\n')
            tr_keys.add(key)
            
        if tag.has_attr('data-i18n-value') and tag['data-i18n-value'] not in tr_keys:
            key = tag['data-i18n-value']
            text = tag.get('value', '').strip().replace('"', '\\"')
            new_tr_lines.append(f'        "{key}": "{text}",\n')
            tr_keys.add(key)

if new_tr_lines:
    tr_str = "".join(new_tr_lines)
    if '"tr": {' in js:
        js = js.replace('"tr": {', '"tr": {\n' + tr_str)
        with open(LANG_JS, 'w', encoding='utf-8') as f:
            f.write(js)
        print(f"Added {len(new_tr_lines)} missing TR keys to lang.js")
    else:
        print("Could not find 'tr': { in lang.js")
else:
    print("No missing TR keys found.")

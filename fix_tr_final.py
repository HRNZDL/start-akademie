import os, sys, re
from bs4 import BeautifulSoup

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html', 'impressum.html', 'datenschutz.html']

with open(LANG_JS, 'r', encoding='utf-8') as f:
    js = f.read()

tr_start = js.find('"tr": {')
tr_end = js.find('},', tr_start)
tr_block = js[tr_start:tr_end]
tr_keys = set(re.findall(r'"([^"]+)"\s*:', tr_block))

new_tr_lines = []
found_keys = set()

for page in PAGES:
    path = os.path.join(DIR, page)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    for tag in soup.find_all(True):
        for attr in ['data-i18n', 'data-i18n-placeholder', 'data-i18n-value']:
            if tag.has_attr(attr):
                key = tag[attr]
                if key not in tr_keys and key not in found_keys:
                    if attr == 'data-i18n':
                        inner = "".join([str(c) for c in tag.contents]).strip()
                    elif attr == 'data-i18n-placeholder':
                        inner = tag.get('placeholder', '')
                    else:
                        inner = tag.get('value', '')
                    inner = inner.replace('"', '\\"').replace('\n', ' ')
                    inner = re.sub(r'\s+', ' ', inner)
                    new_tr_lines.append(f'        "{key}": "{inner}",\n')
                    found_keys.add(key)

print(f"Injecting {len(found_keys)} keys into TR.")

if new_tr_lines:
    insert_at = js.find('\n', tr_start) + 1
    js = js[:insert_at] + "".join(new_tr_lines) + js[insert_at:]
    with open(LANG_JS, 'w', encoding='utf-8') as f:
        f.write(js)
    print("lang.js TR block updated.")

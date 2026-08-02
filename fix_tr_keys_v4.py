import os, re, json
from bs4 import BeautifulSoup

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html', 'impressum.html', 'datenschutz.html']

with open(LANG_JS, 'r', encoding='utf-8') as f:
    js = f.read()

# Extract EN keys robustly
en_start = js.find('"en": {')
en_end = js.find('}\n};', en_start)
if en_end == -1: en_end = js.find('};', en_start)
if en_end == -1: en_end = len(js)
en_block = js[en_start:en_end]
en_keys = set(re.findall(r'"([^"]+)"\s*:', en_block))

# Extract TR keys
tr_start = js.find('"tr": {')
tr_end = js.find('},', tr_start)
tr_block = js[tr_start:tr_end]
tr_keys = set(re.findall(r'"([^"]+)"\s*:', tr_block))

missing_tr = en_keys - tr_keys
print(f"Missing TR keys: {len(missing_tr)}")

# Find HTML for missing keys
new_tr_lines = []
found_keys = set()

for page in PAGES:
    path = os.path.join(DIR, page)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    for el in soup.find_all(True):
        for attr in ['data-i18n', 'data-i18n-placeholder', 'data-i18n-value']:
            if el.has_attr(attr):
                key = el[attr]
                if key in missing_tr and key not in found_keys:
                    if attr == 'data-i18n':
                        inner = "".join([str(c) for c in el.contents]).strip()
                    elif attr == 'data-i18n-placeholder':
                        inner = el.get('placeholder', '')
                    else:
                        inner = el.get('value', '')
                    inner = inner.replace('"', '\\"').replace('\n', ' ')
                    inner = re.sub(r'\s+', ' ', inner)
                    new_tr_lines.append(f'        "{key}": "{inner}",')
                    found_keys.add(key)

print(f"Found {len(found_keys)} missing keys in HTML")

# Now what about keys that are in EXTRA (patch_index_v2.py) that are missing?
# They might not be in the HTML if they are generic. But let's see.

if new_tr_lines:
    js = js[:tr_end] + ",\n" + "\n".join(new_tr_lines) + js[tr_end:]
    with open(LANG_JS, 'w', encoding='utf-8') as f:
        f.write(js)
    print("lang.js updated.")

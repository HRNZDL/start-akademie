import os, re, json
from bs4 import BeautifulSoup

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html', 'impressum.html', 'datenschutz.html']

with open(LANG_JS, 'r', encoding='utf-8') as f:
    js = f.read()

# Extract en keys
en_keys = set()
m = re.search(r'"en"\s*:\s*{(.*?)\n\s*},', js, re.DOTALL)
if not m:
    m = re.search(r'"en"\s*:\s*{(.*?)\n\s*}', js, re.DOTALL)
if m:
    en_keys = set(re.findall(r'"([^"]+)"\s*:', m.group(1)))

# Extract tr keys
tr_keys = set()
tr_start = js.find('"tr": {')
if tr_start != -1:
    tr_block_end = js.find('},', tr_start)
    if tr_block_end == -1: tr_block_end = js.find('}', tr_start)
    tr_block = js[tr_start:tr_block_end]
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
    for el in soup.find_all(attrs={'data-i18n': True}):
        key = el['data-i18n']
        if key in missing_tr and key not in found_keys:
            # We want innerHTML
            inner = "".join([str(c) for c in el.contents]).strip()
            # Escape quotes
            inner = inner.replace('"', '\\"').replace('\n', ' ')
            # Clean up excessive spaces
            inner = re.sub(r'\s+', ' ', inner)
            new_tr_lines.append(f'        "{key}": "{inner}",')
            found_keys.add(key)

print(f"Found {len(found_keys)} missing keys in HTML")

# Append new lines to TR block
if new_tr_lines and tr_start != -1:
    insert_pos = tr_block_end
    if js[tr_block_end] == '}':
        # Need to insert before the closing brace
        js = js[:insert_pos] + ",\n" + "\n".join(new_tr_lines) + "\n    " + js[insert_pos:]
    else:
        pass # Handle if needed
    with open(LANG_JS, 'w', encoding='utf-8') as f:
        f.write(js)
    print("lang.js updated.")

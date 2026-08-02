import os, sys, re, json
from bs4 import BeautifulSoup

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html', 'impressum.html', 'datenschutz.html']

with open(LANG_JS, 'r', encoding='utf-8') as f:
    js = f.read()

tr_start = js.find('"tr": {')
tr_end = js.find('},', tr_start)
tr_keys = set(re.findall(r'"([^"]+)"\s*:', js[tr_start:tr_end]))

missing_in_tr = []

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
                if key not in tr_keys:
                    missing_in_tr.append(key)

if missing_in_tr:
    print(f"FAILED! Found {len(missing_in_tr)} keys in HTML that are missing in TR!")
    print(missing_in_tr[:20])
else:
    print("SUCCESS! All HTML keys are present in TR!")

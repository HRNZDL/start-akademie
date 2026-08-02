# -*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html']

bad_prefixes = ['idx.auto.v2.', 'uni.auto.', 'dil.auto.', 'ausbildung.auto.', 'denklik.auto.', 'degisim.auto.', 'konaklama.auto.', 'iletisim.auto.', 'hakkimizda.auto.']

# Revert HTML
for page in PAGES:
    file_path = os.path.join(DIR, page)
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    modified = False
    
    for tag in soup.find_all(True):
        if tag.has_attr('data-i18n'):
            val = tag['data-i18n']
            if any(val.startswith(p) for p in bad_prefixes):
                del tag['data-i18n']
                modified = True
                
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Reverted bad data-i18n tags in {page}")

# Revert lang.js
with open(LANG_JS, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
removed = 0
for line in lines:
    is_bad = False
    for p in bad_prefixes:
        if f'"{p}' in line:
            is_bad = True
            break
    if is_bad:
        removed += 1
    else:
        new_lines.append(line)

if removed > 0:
    with open(LANG_JS, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Removed {removed} bad lines from lang.js")

print("Revert complete.")

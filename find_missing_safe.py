# -*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup, NavigableString

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html']
MISSING_OUT = os.path.join(DIR, 'missing_text_safe.json')

missing_dict = {}

def get_prefix(page):
    if page == 'index.html': return 'idx'
    return page.replace('.html', '')

for page in PAGES:
    file_path = os.path.join(DIR, page)
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    prefix = get_prefix(page)
    auto_counter = 1
    
    # We want to find TEXT nodes that contain Turkish letters, and wrap them in <span data-i18n="..."> if they aren't already translated.
    for text_node in soup.find_all(string=True):
        parent = text_node.parent
        # Skip scripts, styles, and already i18n'd elements
        if parent.name in ['script', 'style', 'title']: continue
        
        # Check if parent or any ancestor has data-i18n
        has_i18n = False
        for p in text_node.parents:
            if p is None: break
            if p.has_attr('data-i18n'):
                has_i18n = True
                break
        
        if has_i18n: continue
        
        text = text_node.strip()
        if len(text) > 2 and re.search(r'[a-zA-ZğüşıöçĞÜŞİÖÇ]', text):
            # This is a missing text node!
            key = f"{prefix}.safe.{auto_counter}"
            auto_counter += 1
            missing_dict[key] = text

import json
with open(MISSING_OUT, 'w', encoding='utf-8') as f:
    json.dump(missing_dict, f, ensure_ascii=False, indent=2)

print(f"Found {len(missing_dict)} missing text nodes.")

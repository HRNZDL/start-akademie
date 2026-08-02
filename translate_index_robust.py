# -*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import time

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
INDEX = os.path.join(DIR, 'index.html')
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')

print("Starting index.html auto-translator...")

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

tags_to_check = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'button', 'a', 'li', 'div', 'strong', 'em', 'label']

tr_to_en = GoogleTranslator(source='tr', target='en')
tr_to_de = GoogleTranslator(source='tr', target='de')

translations = {}
counter = 1
modified = False

def translate_safe(text, translator):
    if not text.strip(): return text
    
    # Strip HTML tags before translating if it's too complex, or just translate
    # For now, translate directly, but retry on failure
    for _ in range(3):
        try:
            return translator.translate(text)
        except Exception as e:
            time.sleep(1)
            continue
    # If all retries fail, return original
    return text

for tag in soup.find_all(tags_to_check):
    if tag.has_attr('data-i18n'):
        continue
    
    has_parent_i18n = False
    for p in tag.parents:
        if p.has_attr('data-i18n'):
            has_parent_i18n = True
            break
    if has_parent_i18n:
        continue

    text = ''.join(tag.find_all(string=True, recursive=False)).strip()
    
    if len(text) > 2 and re.search(r'[a-zA-ZğüşıöçĞÜŞİÖÇ]', text):
        inner_html = "".join(str(c) for c in tag.contents).strip()
        
        if len(inner_html) > 500:
            continue # Skip large blocks
            
        key = f"idx.auto.v2.{counter}"
        counter += 1
        
        safe_print = f"Translating: {key} -> {inner_html[:40]}...".encode('cp1252', errors='replace').decode('cp1252')
        print(safe_print)
        
        en_text = translate_safe(inner_html, tr_to_en)
        de_text = translate_safe(inner_html, tr_to_de)
        
        translations[key] = {
            "tr": inner_html,
            "en": en_text,
            "de": de_text
        }
        
        tag['data-i18n'] = key
        modified = True
        time.sleep(0.1)

if modified:
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated index.html with {len(translations)} new data-i18n attributes.")
    
    with open(LANG_JS, 'r', encoding='utf-8') as f:
        js = f.read()

    en_lines = ""
    de_lines = ""
    for key, vals in translations.items():
        en_v = vals["en"].replace('"', '\\"').replace('\n', ' ')
        de_v = vals["de"].replace('"', '\\"').replace('\n', ' ')
        en_lines += f'        "{key}": "{en_v}",\n'
        de_lines += f'        "{key}": "{de_v}",\n'

    en_pos = js.find('"en": {')
    if en_pos != -1:
        insert_at = js.find('\n', en_pos) + 1
        js = js[:insert_at] + en_lines + js[insert_at:]

    de_pos = js.find('"de": {')
    if de_pos != -1:
        insert_at = js.find('\n', de_pos) + 1
        js = js[:insert_at] + de_lines + js[insert_at:]

    with open(LANG_JS, 'w', encoding='utf-8') as f:
        f.write(js)
    
    print(f"Injected {len(translations)} keys into lang.js.")
else:
    print("No new tags needed translating.")

print("Done.")

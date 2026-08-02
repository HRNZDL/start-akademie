# -*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import time

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html']

print("Starting full site auto-translator...")

# Create translators
tr_to_en = GoogleTranslator(source='tr', target='en')
tr_to_de = GoogleTranslator(source='tr', target='de')

tags_to_check = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'button', 'a', 'li', 'div', 'strong', 'em', 'label']

def translate_safe(text, translator):
    if not text.strip(): return text
    try:
        return translator.translate(text)
    except Exception as e:
        err_msg = f"Translation error: {e}".encode('cp1252', errors='replace').decode('cp1252')
        print(err_msg)
        return text

all_translations = {}

for page in PAGES:
    file_path = os.path.join(DIR, page)
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    page_name = page.split('.')[0]
    counter = 1
    modified = False
    
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
        
        # Must be longer than 2 chars and contain letters
        if len(text) > 2 and re.search(r'[a-zA-ZğüşıöçĞÜŞİÖÇ]', text):
            key = f"{page_name}.auto.{counter}"
            counter += 1
            
            inner_html = "".join(str(c) for c in tag.contents).strip()
            
            if len(inner_html) > 1500:
                continue # Skip huge blocks
                
            safe_print = f"Translating {page}: {key} -> {inner_html[:30]}...".encode('cp1252', errors='replace').decode('cp1252')
            print(safe_print)
            
            en_text = translate_safe(inner_html, tr_to_en)
            de_text = translate_safe(inner_html, tr_to_de)
            
            all_translations[key] = {
                "tr": inner_html,
                "en": en_text,
                "de": de_text
            }
            
            tag['data-i18n'] = key
            modified = True
            time.sleep(0.1)
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {page} with new data-i18n attributes.")

if all_translations:
    with open(LANG_JS, 'r', encoding='utf-8') as f:
        js = f.read()

    en_lines = ""
    de_lines = ""
    for key, vals in all_translations.items():
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
        
    print(f"Injected {len(all_translations)} new keys into lang.js.")
else:
    print("All subpages are fully translated.")

print("Done.")

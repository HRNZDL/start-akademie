# -*- coding: utf-8 -*-
import os
import re
import json
import time
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html']

def get_prefix(page):
    if page == 'index.html': return 'idx'
    return page.replace('.html', '')

def translate_safe(text, dest_lang, retries=3):
    text = text.strip()
    if not text: return text
    for i in range(retries):
        try:
            return GoogleTranslator(source='tr', target=dest_lang).translate(text)
        except Exception as e:
            err_msg = str(e).encode('ascii', 'ignore').decode()
            print(f"Translation error ({dest_lang}): {err_msg}")
            time.sleep(1)
    return text

def process_all():
    with open(LANG_JS, 'r', encoding='utf-8') as f:
        lang_js = f.read()

    new_keys_en = []
    new_keys_de = []
    total_processed = 0

    for page in PAGES:
        file_path = os.path.join(DIR, page)
        if not os.path.exists(file_path): continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        prefix = get_prefix(page)
        auto_counter = 1
        modified = False
        
        text_nodes = []
        for text_node in soup.find_all(string=True):
            parent = text_node.parent
            if parent is None or parent.name in ['script', 'style', 'title']: continue
            
            has_i18n = False
            for p in text_node.parents:
                if p is None: break
                if p.has_attr('data-i18n'):
                    has_i18n = True
                    break
            
            if has_i18n: continue
            
            text = text_node.strip()
            if len(text) > 2 and re.search(r'[a-zA-ZğüşıöçĞÜŞİÖÇ]', text):
                text_nodes.append((text_node, text))

        print(f"Found {len(text_nodes)} text nodes to translate in {page}")
        
        for text_node, text in text_nodes:
            key = f"{prefix}.safe.{auto_counter}"
            auto_counter += 1
            
            span = soup.new_tag('span', attrs={'data-i18n': key})
            span.string = text
            text_node.replace_with(span)
            modified = True
            
            en_text = translate_safe(text, 'en').replace('"', '\\"')
            de_text = translate_safe(text, 'de').replace('"', '\\"')
            
            new_keys_en.append(f'        "{key}": "{en_text}",\n')
            new_keys_de.append(f'        "{key}": "{de_text}",\n')
            
            total_processed += 1
            if total_processed % 10 == 0:
                print(f"Translated {total_processed} items...")

        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Saved {page}")

    if total_processed > 0:
        en_str = "".join(new_keys_en)
        de_str = "".join(new_keys_de)
        
        if '"en": {' in lang_js:
            lang_js = lang_js.replace('"en": {', '"en": {\n' + en_str)
        if '"de": {' in lang_js:
            lang_js = lang_js.replace('"de": {', '"de": {\n' + de_str)
            
        with open(LANG_JS, 'w', encoding='utf-8') as f:
            f.write(lang_js)
        print("Updated lang.js")

if __name__ == '__main__':
    process_all()
    print("All done!")

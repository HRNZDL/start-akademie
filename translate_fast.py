# -*- coding: utf-8 -*-
import os
import sys
import re
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Ensure print statements flush immediately
sys.stdout.reconfigure(line_buffering=True)

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html']

def get_prefix(page):
    if page == 'index.html': return 'idx'
    return page.replace('.html', '')

def translate_safe_wrapper(text, dest_lang):
    text = text.strip()
    if not text: return text
    for _ in range(2):
        try:
            # We recreate the translator each time to avoid sharing state across threads
            t = GoogleTranslator(source='tr', target=dest_lang)
            return t.translate(text)
        except Exception as e:
            time.sleep(1)
    return text

def process_all():
    with open(LANG_JS, 'r', encoding='utf-8') as f:
        lang_js = f.read()

    new_keys_en = []
    new_keys_de = []
    
    # We will gather all translation tasks from all pages first
    translation_tasks = []
    
    # page -> list of (text_node, key, text)
    page_tasks = {}
    
    for page in PAGES:
        file_path = os.path.join(DIR, page)
        if not os.path.exists(file_path): continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        prefix = get_prefix(page)
        auto_counter = 1
        
        page_tasks[page] = {'soup': soup, 'nodes': [], 'path': file_path}
        
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
                key = f"{prefix}.fast.{auto_counter}"
                auto_counter += 1
                page_tasks[page]['nodes'].append((text_node, key, text))
                
                translation_tasks.append((key, text, 'en'))
                translation_tasks.append((key, text, 'de'))
                
    print(f"Total translation tasks queued: {len(translation_tasks)}")
    
    translations_result = {}
    
    # Process translations in parallel (max 20 workers to avoid heavy rate-limiting, but enough to be fast)
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_task = {executor.submit(translate_safe_wrapper, text, dest_lang): (key, dest_lang) for key, text, dest_lang in translation_tasks}
        completed = 0
        for future in as_completed(future_to_task):
            key, dest_lang = future_to_task[future]
            try:
                result = future.result()
            except Exception as exc:
                result = text # Fallback
            
            if key not in translations_result:
                translations_result[key] = {}
            translations_result[key][dest_lang] = result.replace('"', '\\"') if result else ""
            
            completed += 1
            if completed % 50 == 0:
                print(f"Translated {completed}/{len(translation_tasks)} items...")
                
    print("Translations complete. Applying to HTML and lang.js...")
    
    for page, data in page_tasks.items():
        if not data['nodes']: continue
        
        soup = data['soup']
        for text_node, key, text in data['nodes']:
            span = soup.new_tag('span', attrs={'data-i18n': key})
            span.string = text
            text_node.replace_with(span)
            
            en_val = translations_result[key]['en']
            de_val = translations_result[key]['de']
            new_keys_en.append(f'        "{key}": "{en_val}",\n')
            new_keys_de.append(f'        "{key}": "{de_val}",\n')
            
        with open(data['path'], 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Saved {page}")
        
    en_str = "".join(new_keys_en)
    de_str = "".join(new_keys_de)
    
    if '"en": {' in lang_js:
        lang_js = lang_js.replace('"en": {', '"en": {\n' + en_str)
    if '"de": {' in lang_js:
        lang_js = lang_js.replace('"de": {', '"de": {\n' + de_str)
        
    with open(LANG_JS, 'w', encoding='utf-8') as f:
        f.write(lang_js)
    print("Updated lang.js successfully!")

if __name__ == '__main__':
    process_all()

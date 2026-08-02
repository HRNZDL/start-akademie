# -*- coding: utf-8 -*-
import os, sys, re, time
import bs4
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator

sys.stdout.reconfigure(line_buffering=True)
DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')
PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html']

def get_prefix(page):
    if page == 'index.html': return 'idx'
    return page.replace('.html', '')

def translate_safe(text, dest):
    text = text.strip()
    if not text: return text
    for _ in range(2):
        try:
            return GoogleTranslator(source='tr', target=dest).translate(text)
        except Exception:
            time.sleep(1)
    return text

def process_all():
    with open(LANG_JS, 'r', encoding='utf-8') as f: lang_js = f.read()
    new_keys_en, new_keys_de = [], []
    translation_tasks, page_tasks = [], {}
    
    for page in PAGES:
        path = os.path.join(DIR, page)
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8') as f: soup = BeautifulSoup(f.read(), 'html.parser')
        
        prefix = get_prefix(page)
        auto_c = 1
        page_tasks[page] = {'soup': soup, 'nodes': [], 'attrs': [], 'path': path}
        
        # 1. Text nodes
        for node in soup.find_all(string=True):
            if type(node) is not bs4.element.NavigableString: continue
            if node.parent and node.parent.name in ['script', 'style', 'title']: continue
            if any(p.has_attr('data-i18n') for p in node.parents if p): continue
            
            text = node.strip()
            if len(text) > 2 and re.search(r'[a-zA-ZğüşıöçĞÜŞİÖÇ]', text):
                k = f"{prefix}.fast2.{auto_c}"; auto_c += 1
                page_tasks[page]['nodes'].append((node, k, text))
                translation_tasks.extend([(k, text, 'en'), (k, text, 'de')])
                
        # 2. Placeholders and values
        for tag in soup.find_all(True):
            if tag.has_attr('placeholder') and not tag.has_attr('data-i18n-placeholder'):
                text = tag['placeholder'].strip()
                if len(text) > 2 and re.search(r'[a-zA-ZğüşıöçĞÜŞİÖÇ]', text):
                    k = f"{prefix}.fast2.{auto_c}"; auto_c += 1
                    page_tasks[page]['attrs'].append((tag, 'placeholder', k, text))
                    translation_tasks.extend([(k, text, 'en'), (k, text, 'de')])
                    
            if tag.name == 'input' and tag.get('type') == 'submit' and tag.has_attr('value') and not tag.has_attr('data-i18n-value'):
                text = tag['value'].strip()
                if len(text) > 1 and re.search(r'[a-zA-ZğüşıöçĞÜŞİÖÇ]', text):
                    k = f"{prefix}.fast2.{auto_c}"; auto_c += 1
                    page_tasks[page]['attrs'].append((tag, 'value', k, text))
                    translation_tasks.extend([(k, text, 'en'), (k, text, 'de')])

    print(f"Total tasks: {len(translation_tasks)}")
    res = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        f2t = {executor.submit(translate_safe, text, dest): (k, dest) for k, text, dest in translation_tasks}
        completed = 0
        for future in as_completed(f2t):
            k, dest = f2t[future]
            try: r = future.result()
            except: r = text
            if k not in res: res[k] = {}
            res[k][dest] = r.replace('"', '\\"') if r else ""
            completed += 1
            if completed % 50 == 0: print(f"{completed}/{len(translation_tasks)}...")

    for page, data in page_tasks.items():
        if not data['nodes'] and not data['attrs']: continue
        soup = data['soup']
        
        for node, k, text in data['nodes']:
            span = soup.new_tag('span', attrs={'data-i18n': k})
            span.string = text
            node.replace_with(span)
            new_keys_en.append(f'        "{k}": "{res[k]["en"]}",\n')
            new_keys_de.append(f'        "{k}": "{res[k]["de"]}",\n')
            
        for tag, attr, k, text in data['attrs']:
            if attr == 'placeholder': tag['data-i18n-placeholder'] = k
            elif attr == 'value': tag['data-i18n-value'] = k
            new_keys_en.append(f'        "{k}": "{res[k]["en"]}",\n')
            new_keys_de.append(f'        "{k}": "{res[k]["de"]}",\n')

        with open(data['path'], 'w', encoding='utf-8') as f: f.write(str(soup))
        print(f"Saved {page}")

    en_str = "".join(new_keys_en)
    de_str = "".join(new_keys_de)
    if '"en": {' in lang_js: lang_js = lang_js.replace('"en": {', '"en": {\n' + en_str)
    if '"de": {' in lang_js: lang_js = lang_js.replace('"de": {', '"de": {\n' + de_str)
    with open(LANG_JS, 'w', encoding='utf-8') as f: f.write(lang_js)

if __name__ == '__main__':
    process_all()

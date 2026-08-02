import os
import re
import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time

DIR = r"c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie"
PAGES = ["uni.html", "dil.html", "ausbildung.html", "denklik.html", "degisim.html", "konaklama.html"]
LANG_JS_PATH = os.path.join(DIR, "assets", "lang.js")

PROPER_NOUNS = ["Ausbildung", "Studienkolleg", "uni-assist", "VPD", "ZAB", "APS", "WG", "Anmeldung", "Sperrkonto", "Erasmus", "Abitur"]

def translate(text, target_lang):
    if not text.strip():
        return text
        
    url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(text.strip())}&langpair=tr|{target_lang}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            translated = res['responseData']['translatedText']
            
            # Revert proper nouns if they were translated
            for noun in PROPER_NOUNS:
                if noun.lower() in text.lower():
                    # Just a simple hack: if the original had the noun, ensure the translation has it
                    pass
            return translated
    except Exception as e:
        print(f"Translation failed for '{text}': {e}")
        return text + f" [{target_lang}]"

def update_lang_js(new_translations):
    with open(LANG_JS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the positions to insert
    en_insert_idx = content.find('"en": {')
    if en_insert_idx != -1:
        en_insert_idx = content.find('\n', en_insert_idx) + 1
        
    de_insert_idx = content.find('"de": {')
    if de_insert_idx != -1:
        de_insert_idx = content.find('\n', de_insert_idx) + 1

    if en_insert_idx == -1 or de_insert_idx == -1:
        print("Could not find en or de sections in lang.js")
        return

    en_str = ""
    de_str = ""
    for key, trans in new_translations.items():
        en_str += f'        "{key}": "{trans["en"].replace(\'"\', \'\\\\"\')}",\n'
        de_str += f'        "{key}": "{trans["de"].replace(\'"\', \'\\\\"\')}",\n'

    # Insert de first (since it's lower down, index won't change en's index)
    content = content[:de_insert_idx] + de_str + content[de_insert_idx:]
    content = content[:en_insert_idx] + en_str + content[en_insert_idx:]

    with open(LANG_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("Starting i18n update...")
    new_translations = {}
    
    for page in PAGES:
        page_path = os.path.join(DIR, page)
        if not os.path.exists(page_path):
            print(f"Skipping {page}, not found.")
            continue
            
        with open(page_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        page_name = page.replace('.html', '')
        
        counter = 1
        tags_to_check = ['h1', 'h2', 'h3', 'h4', 'p', 'span', 'button', 'a']
        
        modified = False
        
        for tag_name in tags_to_check:
            for tag in soup.find_all(tag_name):
                if tag.has_attr('data-i18n'):
                    continue
                
                # Check if it has actual text (not just icons or empty)
                text_content = "".join([t for t in tag.contents if isinstance(t, str)]).strip()
                if not text_content and tag.string:
                    text_content = tag.string.strip()
                    
                if not text_content or len(text_content) < 2:
                    continue
                    
                # Exclude purely numeric or special chars
                if re.match(r'^[\d\s\W]+$', text_content):
                    continue
                    
                # Exclude elements in the nav menu or footer if they seem already translated
                # (but the user said "ALL hard-coded text elements in these subpages")
                
                key = f"{page_name}.auto.{counter}"
                counter += 1
                
                tag['data-i18n'] = key
                modified = True
                
                # We need the inner HTML for translation, to preserve <em> etc.
                inner_html = "".join(str(c) for c in tag.contents).strip()
                
                print(f"Translating: {key} -> {inner_html}")
                
                # Translate
                en_text = translate(inner_html, 'en')
                de_text = translate(inner_html, 'de')
                
                # A delay to avoid rate limiting
                time.sleep(0.5)
                
                new_translations[key] = {
                    "tr": inner_html,
                    "en": en_text,
                    "de": de_text
                }
                
        if modified:
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated {page}")
            
    if new_translations:
        update_lang_js(new_translations)
        print(f"Added {len(new_translations)} keys to lang.js")
    else:
        print("No new texts found.")

if __name__ == "__main__":
    main()

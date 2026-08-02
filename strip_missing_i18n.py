import os, re
from bs4 import BeautifulSoup

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'

with open(os.path.join(DIR, 'assets', 'lang.js'), 'r', encoding='utf-8') as f:
    js = f.read()

en_keys = set()
en_match = re.search(r'\"en\"\s*:\s*\{([^}]+)\}', js, re.DOTALL)
if en_match:
    for line in en_match.group(1).split('\n'):
        m = re.search(r'\"([^\"]+)\"\s*\:', line)
        if m: en_keys.add(m.group(1))

PAGES = ['index.html', 'uni.html', 'dil.html', 'ausbildung.html', 'denklik.html', 'degisim.html', 'konaklama.html', 'iletisim.html', 'hakkimizda.html']

for page in PAGES:
    path = os.path.join(DIR, page)
    if not os.path.exists(path): continue
    
    with open(path, 'r', encoding='utf-8') as f: html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    modified = False
    
    for tag in soup.find_all(True):
        if tag.has_attr('data-i18n') and tag['data-i18n'] not in en_keys:
            del tag['data-i18n']
            modified = True
            
    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f'Stripped missing tags from {page}')

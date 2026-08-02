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

with open('missing_keys_dump.txt', 'w', encoding='utf-8') as out:
    for page in PAGES:
        with open(os.path.join(DIR, page), 'r', encoding='utf-8') as f: html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        out.write(f'=== {page} ===\n')
        for tag in soup.find_all(True):
            if tag.has_attr('data-i18n') and tag['data-i18n'] not in en_keys:
                out.write(f"Key: {tag['data-i18n']}\n")
                out.write(f"HTML: {str(tag)[:150]}\n")
                out.write('-'*50 + '\n')

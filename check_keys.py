import os, re
from bs4 import BeautifulSoup

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
with open(os.path.join(DIR, 'index.html'), 'r', encoding='utf-8') as f: html = f.read()
soup = BeautifulSoup(html, 'html.parser')

keys_in_html = set()
for tag in soup.find_all(True):
    if tag.has_attr('data-i18n'):
        keys_in_html.add(tag['data-i18n'])

with open(os.path.join(DIR, 'assets', 'lang.js'), 'r', encoding='utf-8') as f:
    js = f.read()

en_keys = set()
de_keys = set()
en_match = re.search(r'\"en\"\s*:\s*\{([^}]+)\}', js, re.DOTALL)
if en_match:
    for line in en_match.group(1).split('\n'):
        m = re.search(r'\"([^\"]+)\"\s*\:', line)
        if m: en_keys.add(m.group(1))

missing_in_en = keys_in_html - en_keys
print(f'Total data-i18n keys in index.html: {len(keys_in_html)}')
print(f'Missing in EN dict: {len(missing_in_en)}')
if missing_in_en:
    print('Sample missing:', list(missing_in_en)[:10])

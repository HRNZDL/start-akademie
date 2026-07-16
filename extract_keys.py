import json
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

keys = {}
for el in soup.find_all(attrs={"data-i18n": True}):
    key = el['data-i18n']
    # For some elements (like inputs) we might need to check placeholders instead, 
    # but the javascript uses data-i18n for innerHTML and data-i18n-placeholder for placeholders.
    # So we extract innerHTML.
    inner_html = el.decode_contents().strip()
    keys[key] = inner_html

for el in soup.find_all(attrs={"data-i18n-placeholder": True}):
    key = el['data-i18n-placeholder']
    placeholder = el.get('placeholder', '')
    keys[key] = placeholder

with open('keys.json', 'w', encoding='utf-8') as f:
    json.dump(keys, f, indent=2, ensure_ascii=False)

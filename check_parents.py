import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
for el in soup.find_all(attrs={'data-i18n': True}):
    children = el.find_all(True)
    if children:
        print(f'<{el.name} data-i18n="{el.get("data-i18n")}"> has {len(children)} children: {[c.name for c in children[:3]]}')

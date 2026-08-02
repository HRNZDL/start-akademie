# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import re

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
INDEX = os.path.join(DIR, 'index.html')

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

missing = []
tags_to_check = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'button', 'a', 'li', 'div', 'strong', 'em', 'label']

for tag in soup.find_all(tags_to_check):
    if tag.has_attr('data-i18n'):
        continue
    
    # Check if a parent has data-i18n
    has_parent_i18n = False
    for p in tag.parents:
        if p.has_attr('data-i18n'):
            has_parent_i18n = True
            break
    if has_parent_i18n:
        continue
        
    text = ''.join(tag.find_all(string=True, recursive=False)).strip()
    
    if len(text) > 2 and re.search(r'[a-zA-ZğüşıöçĞÜŞİÖÇ]', text):
        missing.append((tag.name, text, str(tag)[:100]))

with open('missing_index.txt', 'w', encoding='utf-8') as f:
    for i, m in enumerate(missing):
        f.write(f"{i}. {m[0]}: {repr(m[1][:60])} | {m[2]}\n")

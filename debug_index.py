# -*- coding: utf-8 -*-
import os, sys, re
os.environ['PYTHONIOENCODING'] = 'utf-8'

DIR = r"c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie"
INDEX = os.path.join(DIR, "index.html")
LANG_JS = os.path.join(DIR, "assets", "lang.js")

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all li text patterns
matches = re.findall(r'</i>([^<]{2,60})</li>', html)
for m in matches[:20]:
    print(repr(m))

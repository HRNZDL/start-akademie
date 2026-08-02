import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    js = f.read()

tr_start = js.find('"tr": {')
tr_end = js.find('},', tr_start)
tr_block = js[tr_start:tr_end]

for key in ['idx.srv.section.tag', 'idx.srv.dnk.desc']:
    if key in tr_block:
        print(f'{key} is present')
    else:
        print(f'{key} is MISSING')

import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    js = f.read()

tr_start = js.find('"tr": {')
tr_end = js.find('},', tr_start)
if tr_end == -1: tr_end = js.find('}', tr_start)

print(js[tr_end-200:tr_end+50])

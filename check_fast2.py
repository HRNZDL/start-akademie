import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    js = f.read()

tr_start = js.find('"tr": {')
tr_end = js.find('},', tr_start)
if tr_end == -1: tr_end = js.find('}', tr_start)
tr_block = js[tr_start:tr_end]

print('idx.fast2.19 in TR:', 'idx.fast2.19' in tr_block)

import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    js = f.read()

tr_start = js.find('"tr": {')
tr_end = js.find('},', tr_start)
if tr_end == -1: tr_end = js.find('}', tr_start)
tr_block = js[tr_start:tr_end]

empty_count = 0
for line in tr_block.split('\n'):
    m = re.search(r'"([^"]+)"\s*:\s*"(.*)"', line)
    if m:
        if not m.group(2).strip():
            empty_count += 1
print(f'Empty TR values: {empty_count}')

import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    js = f.read()

m_en = re.search(r'"en"\s*:\s*{(.*?)\n\s*},', js, re.DOTALL)
if not m_en:
    m_en = re.search(r'"en"\s*:\s*{(.*?)\n\s*}', js, re.DOTALL)
en_keys = set(re.findall(r'"([^"]+)"\s*:', m_en.group(1))) if m_en else set()

tr_start = js.find('"tr": {')
tr_end = js.find('},', tr_start)
if tr_end == -1: tr_end = js.find('}', tr_start)
tr_keys = set(re.findall(r'"([^"]+)"\s*:', js[tr_start:tr_end])) if tr_start != -1 else set()

missing = en_keys - tr_keys
print('Missing:', len(missing))
print(list(missing)[:20])

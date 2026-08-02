import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    js = f.read()

m_en = re.search(r'"en"\s*:\s*{(.*?)\n\s*},', js, re.DOTALL)
if m_en:
    en_keys = set(re.findall(r'"([^"]+)"\s*:', m_en.group(1)))

m_tr = re.search(r'"tr"\s*:\s*{(.*?)\n\s*},', js, re.DOTALL)
if m_tr:
    tr_keys = set(re.findall(r'"([^"]+)"\s*:', m_tr.group(1)))

missing = en_keys - tr_keys
print(f"Missing keys: {len(missing)}")
for i, k in enumerate(list(missing)[:20]):
    print(k)

import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    js = f.read()

m = re.search(r'"tr"\s*:\s*{(.*?)\n\s*},', js, re.DOTALL)
if m:
    tr = m.group(1)
    for line in tr.split('\n'):
        val = re.search(r':\s*"(.*)"', line)
        if val:
            v = val.group(1)
            if v.count('<') != v.count('>'):
                print(line)

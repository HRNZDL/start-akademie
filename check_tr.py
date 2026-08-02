import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    js = f.read()
m = re.search(r'"tr"\s*:\s*{(.*?)}', js, re.DOTALL)
if m:
    tr_block = m.group(1)
    for line in tr_block.split('\n'):
        if 'welcome.title' in line or 'hero.title' in line or 'hero.main_title' in line:
            print(line.strip())

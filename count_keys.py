import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    js = f.read()

def get_keys(lang):
    m = re.search(f'"{lang}"\\s*:\\s*{{(.*?)\n\\s*}},', js, re.DOTALL)
    if not m:
        # Try matching till the end if it's the last one
        m = re.search(f'"{lang}"\\s*:\\s*{{(.*?)\n\\s*}}', js, re.DOTALL)
    if not m: return 0
    return len(re.findall(r'"[\w\.-]+"\s*:', m.group(1)))

print('en:', get_keys('en'))
print('de:', get_keys('de'))
print('tr:', get_keys('tr'))

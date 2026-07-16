import os
import re

def fix_sifir_css_js(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Any remaining sıfırEach should be forEach
    text = text.replace("sıfırEach", "forEach")
    
    # Let's also check for other instances of forEach being corrupted
    text = re.sub(r'(\w+)\.sıfır', r'\1.for', text)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['assets/styles/main.css', 'assets/js/main.js']:
    fix_sifir_css_js(f)

print('Done fixing sıfırEach')

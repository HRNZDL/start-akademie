import os

def fix_sifir(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace("entriesıfıry", "entries.forEach((entry")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['index.html', 'assets/styles/main.css', 'assets/js/main.js', 'assets/lang.js']:
    fix_sifir(f)

print('Done')

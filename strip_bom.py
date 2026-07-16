import os

def remove_bom(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    if text.startswith('\ufeff'):
        text = text[1:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Removed BOM from {filepath}")

for f in ['index.html', 'assets/js/main.js', 'assets/styles/main.css', 'assets/lang.js']:
    remove_bom(f)

print('Done stripping BOM')

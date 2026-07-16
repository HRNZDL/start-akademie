import os

def fix_wizard(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace(".wizard-forEach", ".wizard-step').forEach")
    text = text.replace(".wizard-for", ".wizard-step').for") # in case the other regex ran

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['assets/styles/main.css', 'assets/js/main.js']:
    fix_wizard(f)

print('Done fixing wizard step')

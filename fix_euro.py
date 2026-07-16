import os
import re

def fix_euro_quotes(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # First, change ALL € back to ' to fix code
    text = text.replace("€", "'")
    
    # Then carefully add back € ONLY for prices where they belong
    text = re.sub(r'(\d+[\.,]\d+|\d+)\s*\'', r'\1 €', text)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['index.html', 'assets/styles/main.css', 'assets/js/main.js', 'assets/lang.js']:
    fix_euro_quotes(f)

print('Done fixing € -> \'')

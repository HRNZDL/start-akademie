import os
import re

def fix_euro_regex_mistakes(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Revert accidental € back to ' for code
    text = text.replace("'0 €", "'0'")
    text = text.replace("'1 €", "'1'")
    text = text.replace(" 0 €", " 0 '") # if any
    
    # Let's just blindly change any € that is immediately followed by a semicolon or something
    text = re.sub(r"\'(\d+)\s*€", r"'\1'", text)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['index.html', 'assets/styles/main.css', 'assets/js/main.js', 'assets/lang.js']:
    fix_euro_regex_mistakes(f)

print('Done fixing € -> \' regex mistake')

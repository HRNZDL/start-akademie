import os

def fix_question_mark(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace("🔸", "?")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['assets/js/main.js']:
    fix_question_mark(f)

print('Done fixing ?')

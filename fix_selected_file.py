import os

def fix_selected_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace("'sıfırText = file.name;", "'selected-file').innerText = file.name;")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['assets/js/main.js']:
    fix_selected_file(f)

print('Done fixing selected file')

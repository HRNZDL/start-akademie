import os
import re

def fix_sifir_html(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Revert the corrupted src="assets/logo-final-cropped.png"
    text = text.replace("s\u0131f\u0131ropped.png\"", "src=\"assets/logo-final-cropped.png\"")
    text = text.replace("sıfıropped.png\"", "src=\"assets/logo-final-cropped.png\"")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

fix_sifir_html('index.html')
print('Done fixing sıfıropped.png')

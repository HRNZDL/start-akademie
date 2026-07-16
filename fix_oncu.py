import os
import re

def fix_oncu_disaster(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Protect the real word "öncü" (which is preceded by a space or in specific contexts)
    # The only real usage in the text is "beşeri bilimlerde öncü küresel"
    text = text.replace(" bilimlerde öncü küresel", " bilimlerde __REAL_ONCU__ küresel")
    
    # Also in case I wrote "öncü" anywhere else intentionally
    text = text.replace(">öncü<", ">__REAL_ONCU__<")

    # Now replace the catastrophic "öncü" back to "nc"
    text = text.replace("öncü", "nc")

    # Restore the real "öncü"
    text = text.replace("__REAL_ONCU__", "öncü")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in ['index.html', 'assets/styles/main.css', 'assets/js/main.js', 'assets/lang.js']:
    fix_oncu_disaster(f)

print('Done')

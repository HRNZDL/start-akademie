import codecs
import re

with codecs.open('assets/style.css', 'r', 'utf-8') as f:
    css = f.read()

# Fix 1: Add overflow-x hidden
if 'overflow-x: hidden' not in css:
    css += "\n\nhtml, body {\n    overflow-x: hidden !important;\n    width: 100%;\n    max-width: 100vw;\n    margin: 0;\n    padding: 0;\n}\n"

# Fix 2: Change startbot-window from absolute to fixed
css = re.sub(r'(\.startbot-window\s*\{[^}]*)position:\s*absolute;', r'\1position: fixed;', css)

# Add mobile startbot fix
if 'startbot-window-fix' not in css:
    css += "\n/* startbot-window-fix */\n@media(max-width:768px) {\n    .startbot-window:not(.active) {\n        display: none !important;\n    }\n}\n"

with codecs.open('assets/style.css', 'w', 'utf-8') as f:
    f.write(css)

print("Overflow and StartBot bugs fixed.")

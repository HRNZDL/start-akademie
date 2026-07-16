import re
import os

with open('index.backup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix common encoding errors I might have introduced
html = html.replace('translateö', 'translate0')
html = html.replace('translateYö', 'translateY0')
html = html.replace('translateXö', 'translateX0')
html = html.replace('sıfır', '0')
html = html.replace('scrollö', 'scrollY')
html = html.replace('forö', 'forEach')
html = html.replace('transformö', 'transform0')

# Extract the big script
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
if scripts:
    main_script = max(scripts, key=len)
    
    # Remove the big inline script from HTML
    html = html.replace(f'<script>{main_script}</script>', '<script src="assets/js/main.js?v=20260604c"></script>')
    
    # Fix encoding errors in main_script
    main_script = main_script.replace('translateö', 'translate0')
    main_script = main_script.replace('translateYö', 'translateY0')
    main_script = main_script.replace('translateXö', 'translateX0')
    main_script = main_script.replace('sıfır', '0')
    main_script = main_script.replace('scrollö', 'scrollY')
    main_script = main_script.replace('forö', 'forEach')
    main_script = main_script.replace('transformö', 'transform0')

    with open(r'assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(main_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("RESTORED CUSTOM SITE SUCCESSFULLY")

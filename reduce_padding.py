import re

# Update style.css
with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace padding: 48px; with padding: 32px; in .glass-card
css = css.replace('padding: 48px;', 'padding: 32px;')

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace inline style padding: 64px with padding: 40px
html = html.replace('padding: 64px;', 'padding: 40px;')
# Also update the cache buster
html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=26', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

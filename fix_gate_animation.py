import re

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove overflow-x: hidden !important; from the html, body block at the bottom
css = css.replace(
'''html, body {
    overflow-x: hidden !important;
    width: 100%;
    max-width: 100vw;
    margin: 0;
    padding: 0;
}''',
'''html, body {
    width: 100%;
    max-width: 100vw;
    margin: 0;
    padding: 0;
}'''
)

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update cache buster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=23', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

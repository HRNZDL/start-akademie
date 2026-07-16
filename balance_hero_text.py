import re

with open('assets/lang.js', 'r', encoding='utf-8') as f:
    lang = f.read()

# Fix German
lang = lang.replace('"Ihr Bildungsweg in <br><em>Deutschland</em>"', '"Ihr Bildungsweg <br><em>in Deutschland</em>"')
# Fix English
lang = lang.replace('"Your Education Path <em>in Germany</em>"', '"Your Education Path <br><em>in Germany</em>"')
# Fix other English title
lang = lang.replace('"Your Education Journey in Germany <em>Starts Here</em>"', '"Your Education Journey <br><em>Starts Here</em>"')
# Fix other German title
lang = lang.replace('"Ihr Bildungsweg in Deutschland <em>Beginnt Hier</em>"', '"Ihr Bildungsweg <br><em>Beginnt Hier</em>"')

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(lang)

# Update cache buster in index.html to force a reload
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=30', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

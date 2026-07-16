import re

with open('assets/lang.js', 'r', encoding='utf-8') as f:
    lang = f.read()

# Specifically replace the TR hero.main_title
tr_find = '''        "welcome.stat2_desc": "Akredite Kalite",
        "hero.main_title": "Ihr Bildungsweg <br><em>in Deutschland</em>",
        "hero.seo_desc": "Almanya'da Eğitim, Nachhilfe ve Üniversite Kabul Danışmanlığı Merkezi",'''

tr_replace = '''        "welcome.stat2_desc": "Akredite Kalite",
        "hero.main_title": "Almanya'daki Eğitim <br><em>Yolculuğunuz</em>",
        "hero.seo_desc": "Almanya'da Eğitim, Nachhilfe ve Üniversite Kabul Danışmanlığı Merkezi",'''

lang = lang.replace(tr_find, tr_replace)

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(lang)

# Update index.html cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=34', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

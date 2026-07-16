import io

lang_path = 'assets/lang.js'

with io.open(lang_path, 'r', encoding='utf-8') as f:
    lang_js = f.read()

# Fix the known Turkish fragment
fragment_tr = ' bloke hesap ve lise ders destekleri hakkinda size nasil yardimci olabilirim?",'
lang_js = lang_js.replace(fragment_tr, '')

fragment_en = ' blocked accounts, or tutoring today?",'
lang_js = lang_js.replace(fragment_en, '')

fragment_de = ' Sperrkonto oder Nachhilfe helfen?",'
lang_js = lang_js.replace(fragment_de, '')

with io.open(lang_path, 'w', encoding='utf-8') as f:
    f.write(lang_js)

# Also force index.html cache bust again just in case
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('assets/lang.js?v=10', 'assets/lang.js?v=11')
with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Syntax error fragments removed.")

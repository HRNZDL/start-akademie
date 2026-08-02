import os

DIR = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie'
LANG_JS = os.path.join(DIR, 'assets', 'lang.js')

with open(LANG_JS, 'r', encoding='utf-8') as f:
    js = f.read()

if 'data-i18n-value' not in js:
    js = js.replace(
        "document.querySelectorAll('input[data-i18n-placeholder], textarea[data-i18n-placeholder]').forEach(function(el) {",
        "document.querySelectorAll('input[data-i18n-value]').forEach(function(el) { var key = el.getAttribute('data-i18n-value'); if (translations[lang] && translations[lang][key]) { el.setAttribute('value', translations[lang][key]); } });\n    document.querySelectorAll('input[data-i18n-placeholder], textarea[data-i18n-placeholder]').forEach(function(el) {"
    )
    with open(LANG_JS, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Added data-i18n-value support!")

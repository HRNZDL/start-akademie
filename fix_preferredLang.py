import io

html_path = 'index.html'

with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the localStorage key
html = html.replace("localStorage.getItem('lang')", "localStorage.getItem('preferredLang')")

# Cache busting
html = html.replace('assets/lang.js?v=8', 'assets/lang.js?v=9')
html = html.replace('assets/style.css?v=10', 'assets/style.css?v=11')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed preferredLang key in bot logic.")

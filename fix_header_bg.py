import io

css_path = 'assets/style.css'
with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix header background variables for dark mode
css = css.replace('--header-bg: rgba(3, 4, 7, 0.4);', '--header-bg: rgba(9, 10, 15, 0.3);')
css = css.replace('--header-scrolled-bg: rgba(3, 4, 7, 0.88);', '--header-scrolled-bg: rgba(9, 10, 15, 0.65);')

# Also let's check if there's any other hardcoded #030407 in dark mode variables
# --bg is now #090a0f

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update version in HTML
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/style.css?v=13', 'assets/style.css?v=14')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Header background fixed.")

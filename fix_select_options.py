import re

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add option styling right after form-group select
old_css = '''        .form-group input, .form-group select {
            background: rgba(255, 255, 255, 0.03);'''

new_css = '''        .form-group select option {
            background-color: var(--bg-deep);
            color: var(--text);
        }

        .form-group input, .form-group select {
            background: rgba(255, 255, 255, 0.03);'''

if old_css in css:
    css = css.replace(old_css, new_css)
else:
    print("Could not find the target CSS block to replace.")

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=27', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

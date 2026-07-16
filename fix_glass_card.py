import re

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_glass_card = '''        .glass-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 48px;
            backdrop-filter: blur(24px);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
            transition: var(--transition);
        }'''

new_glass_card = '''        .glass-card {
            background: rgba(14, 16, 21, 0.65); /* Darkened background for readability */
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 48px;
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px); /* Safari support */
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
            transition: var(--transition);
        }'''

css = css.replace(old_glass_card, new_glass_card)

# Let's also ensure the portal slide glass card padding is correct
old_portal_card = '''    .portal-slide .glass-panel { padding: 24px 16px !important; }'''
new_portal_card = '''    .portal-slide .glass-card { padding: 24px 16px !important; }'''
css = css.replace(old_portal_card, new_portal_card)

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=24', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

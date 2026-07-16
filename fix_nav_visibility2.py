import re

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure dark theme has the variable properly formatted if it was missed
if '--nav-text-color: rgba(255,255,255,0.85);' not in css:
    css = css.replace(':root[data-theme="dark"] {', ':root[data-theme="dark"] {\n    --nav-text-color: rgba(255,255,255,0.85);')

# Replace color for .lang-btn
css = re.sub(r'(\.lang-btn\s*\{[^}]*?)color:\s*var\(--text-muted\);', r'\1color: var(--nav-text-color);', css)

# Replace color for .theme-toggle
css = re.sub(r'(\.theme-toggle\s*\{[^}]*?)color:\s*var\(--text-muted\);', r'\1color: var(--nav-text-color);', css)

# Add a text-shadow to make it even more visible against bright sky
css = re.sub(r'(\.nav-link\s*\{[^}]*?)color:\s*var\(--nav-text-color\);', r'\1color: var(--nav-text-color);\n            text-shadow: 0 1px 4px rgba(0,0,0,0.4);', css)

# Make lang-btn and theme-toggle have text shadow
css = re.sub(r'(\.lang-btn\s*\{[^}]*?)color:\s*var\(--nav-text-color\);', r'\1color: var(--nav-text-color);\n            text-shadow: 0 1px 4px rgba(0,0,0,0.4);', css)
css = re.sub(r'(\.theme-toggle\s*\{[^}]*?)color:\s*var\(--nav-text-color\);', r'\1color: var(--nav-text-color);\n            filter: drop-shadow(0 1px 4px rgba(0,0,0,0.4));', css)


with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=33', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

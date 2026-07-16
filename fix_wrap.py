import io

css_path = 'assets/style.css'
with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the flex container to wrap instead of horizontal scrolling
old_chips = """        .startbot-chips {
            display: flex;
            gap: 8px;
            padding: 12px 20px;
            overflow-x: auto;
            white-space: nowrap;
            border-top: none; /* Removed cluttered line */
        }"""
        
new_chips = """        .startbot-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            padding: 12px 20px;
            border-top: none;
        }"""

if old_chips in css:
    css = css.replace(old_chips, new_chips)

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html version tag to bust cache
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/style.css?v=7', 'assets/style.css?v=8')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Chips wrapping fixed.")

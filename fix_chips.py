import io

css_path = 'assets/style.css'
with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Light Mode Chips
old_light_chips = """        :root[data-theme="light"] .startbot-chips {
            border-top: 1px solid rgba(0, 0, 0, 0.06);
        }
        :root[data-theme="light"] .startbot-chip {
            background: #ffffff;
            border: 1px solid rgba(0,0,0,0.1);
            color: #333;
        }
        :root[data-theme="light"] .startbot-chip:hover {
            background: var(--gold);
            color: #fff;
            border-color: var(--gold);
        }"""
        
new_light_chips = """        :root[data-theme="light"] .startbot-chips {
            border-top: none; /* Removed cluttered line */
        }
        :root[data-theme="light"] .startbot-chip {
            background: #f5f5f7; /* Apple soft grey */
            border: none; /* Removed harsh border */
            color: #1d1d1f;
            padding: 8px 16px;
        }
        :root[data-theme="light"] .startbot-chip:hover {
            background: var(--gold);
            color: #fff;
        }"""

if old_light_chips in css:
    css = css.replace(old_light_chips, new_light_chips)

# 2. Update Dark Mode Chips
old_dark_chips = """        .startbot-chips {
            display: flex;
            gap: 8px;
            padding: 10px 20px;
            overflow-x: auto;
            white-space: nowrap;
            border-top: 1px solid rgba(255, 255, 255, 0.04);
        }

        .startbot-chips::-webkit-scrollbar {
            display: none;
        }

        .startbot-chip {
            background: rgba(212, 175, 100, 0.06);
            border: 1px solid rgba(212, 175, 100, 0.2);
            color: var(--gold-light);
            padding: 6px 14px;
            border-radius: 30px;
            font-size: 0.76rem;
            font-weight: 500;
            cursor: pointer;
            transition: var(--transition);
        }"""

new_dark_chips = """        .startbot-chips {
            display: flex;
            gap: 8px;
            padding: 12px 20px;
            overflow-x: auto;
            white-space: nowrap;
            border-top: none; /* Removed cluttered line */
        }

        .startbot-chips::-webkit-scrollbar {
            display: none;
        }

        .startbot-chip {
            background: rgba(255, 255, 255, 0.06);
            border: none; /* Removed harsh border */
            color: #ffffff;
            padding: 8px 16px;
            border-radius: 30px;
            font-size: 0.76rem;
            font-weight: 500;
            cursor: pointer;
            transition: var(--transition);
        }"""
if old_dark_chips in css:
    css = css.replace(old_dark_chips, new_dark_chips)

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html version tag to bust cache
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/style.css?v=6', 'assets/style.css?v=7')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Chips styling fixed.")

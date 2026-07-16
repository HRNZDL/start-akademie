import re

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add --nav-text-color to dark theme
dark_root_find = '''        :root[data-theme="dark"] {
            --bg-deep: #090a0f;'''
dark_root_replace = '''        :root[data-theme="dark"] {
            --bg-deep: #090a0f;
            --nav-text-color: rgba(255, 255, 255, 0.85);'''
css = css.replace(dark_root_find, dark_root_replace)

# 2. Add --nav-text-color to light theme
light_root_find = '''        :root[data-theme="light"] {
            --bg-deep: #ffffff;'''
light_root_replace = '''        :root[data-theme="light"] {
            --bg-deep: #ffffff;
            --nav-text-color: #555555;'''
css = css.replace(light_root_find, light_root_replace)

# 3. Replace text-muted in nav components
# We need to replace specific blocks carefully.
nav_link_find = '''        .nav-link {
            font-size: clamp(0.75rem, 0.9vw, 0.85rem);
            font-weight: 400;
            color: var(--text-muted);'''
nav_link_replace = '''        .nav-link {
            font-size: clamp(0.75rem, 0.9vw, 0.85rem);
            font-weight: 400;
            color: var(--nav-text-color);'''
css = css.replace(nav_link_find, nav_link_replace)

lang_btn_find = '''        .lang-btn {
            background: none;
            border: none;
            color: var(--text-muted);'''
lang_btn_replace = '''        .lang-btn {
            background: none;
            border: none;
            color: var(--nav-text-color);'''
css = css.replace(lang_btn_find, lang_btn_replace)

theme_toggle_find = '''        .theme-toggle {
            background: none;
            border: none;
            color: var(--text-muted);'''
theme_toggle_replace = '''        .theme-toggle {
            background: none;
            border: none;
            color: var(--nav-text-color);'''
css = css.replace(theme_toggle_find, theme_toggle_replace)

mobile_btn_find = '''        .mobile-btn {
            display: none;
            background: none;
            border: none;
            color: var(--text-muted);'''
mobile_btn_replace = '''        .mobile-btn {
            display: none;
            background: none;
            border: none;
            color: var(--nav-text-color);'''
css = css.replace(mobile_btn_find, mobile_btn_replace)

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=31', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

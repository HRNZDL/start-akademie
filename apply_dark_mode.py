import io
import re

css_path = 'assets/style.css'
with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update the dark mode palette
palette_old = """        :root {
            /* Palette */
            --bg: #030407;
            --bg-deep: #010204;
            --text: #f4f3ef;
            --text-muted: #8d909a;
            --gold: #d4af64;
            --gold-light: #ebd6a8;
            --gold-glow: rgba(212, 175, 100, 0.18);
            --border: rgba(255, 255, 255, 0.06);
            --border-hover: rgba(212, 175, 100, 0.25);
            --surface: rgba(12, 14, 24, 0.45);
            --surface-hover: rgba(18, 22, 38, 0.65);"""

palette_new = """        :root {
            /* Palette */
            --bg: #090a0f;
            --bg-deep: #060609;
            --text: #f4f3ef;
            --text-muted: #8d909a;
            --gold: #d4af64;
            --gold-light: #ebd6a8;
            --gold-glow: rgba(212, 175, 100, 0.18);
            --border: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(212, 175, 100, 0.3);
            --surface: rgba(255, 255, 255, 0.02);
            --surface-hover: rgba(255, 255, 255, 0.05);"""

if palette_old in css:
    css = css.replace(palette_old, palette_new)
else:
    print("WARNING: Palette old block not found perfectly, trying regex fallback.")
    css = re.sub(r'--bg:\s*#030407;', '--bg: #090a0f;', css)
    css = re.sub(r'--bg-deep:\s*#010204;', '--bg-deep: #060609;', css)
    css = re.sub(r'--border:\s*rgba\(255, 255, 255, 0\.06\);', '--border: rgba(255, 255, 255, 0.08);', css)
    css = re.sub(r'--surface:\s*rgba\(12, 14, 24, 0\.45\);', '--surface: rgba(255, 255, 255, 0.02);', css)
    css = re.sub(r'--surface-hover:\s*rgba\(18, 22, 38, 0\.65\);', '--surface-hover: rgba(255, 255, 255, 0.05);', css)


# 2. Add Ambient Glow to body ONLY for dark mode
body_old = """        body {
            font-family: var(--font-sans);
            background-color: var(--bg);
            color: var(--text);"""

body_new = """        body {
            font-family: var(--font-sans);
            background-color: var(--bg);
            background-image: radial-gradient(circle at 50% 0%, rgba(212, 175, 100, 0.06) 0%, transparent 50%);
            color: var(--text);"""

css = css.replace(body_old, body_new)

# Protect light mode body from the glow
light_body_old = """        :root[data-theme="light"] body {
            background-color: #fcfcfc;
            color: #1a1a1c;
        }"""
        
light_body_new = """        :root[data-theme="light"] body {
            background-color: #fcfcfc;
            background-image: none;
            color: #1a1a1c;
        }"""
css = css.replace(light_body_old, light_body_new)


# 3. Add drop shadow and inner border to glass cards for 3D depth
glass_card_old = """        .glass-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 30px;
            backdrop-filter: blur(16px);
            transition: all 0.4s ease;
        }"""
        
glass_card_new = """        .glass-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-top: 1px solid rgba(255, 255, 255, 0.12); /* 3D top shine */
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6); /* Deep shadow */
            border-radius: 12px;
            padding: 30px;
            backdrop-filter: blur(16px);
            transition: all 0.4s ease;
        }"""
css = css.replace(glass_card_old, glass_card_new)

glass_hover_old = """        .glass-card:hover {
            transform: translateY(-5px);
            background: var(--surface-hover);
            border-color: var(--border-hover);
        }"""
        
glass_hover_new = """        .glass-card:hover {
            transform: translateY(-6px);
            background: var(--surface-hover);
            border-color: var(--border-hover);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(212, 175, 100, 0.1) inset;
        }"""
css = css.replace(glass_hover_old, glass_hover_new)


with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html version tag to force reload
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/style.css?v=11', 'assets/style.css?v=13')
html = html.replace('assets/style.css?v=12', 'assets/style.css?v=13')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Dark mode CSS applied successfully!")

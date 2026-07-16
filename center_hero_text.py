import io
import re

css_path = 'assets/style.css'
with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add text-align: center; to .gate-initial-hero h1
old_css = """        .gate-initial-hero h1 {
            font-size: clamp(2.2rem, 5vw, 4rem);
            margin-bottom: 20px;
            color: #ffffff !important;
            text-shadow: 0 4px 20px rgba(0,0,0,0.7), 0 2px 8px rgba(0,0,0,0.4);
            line-height: 1.15;
        }"""

new_css = """        .gate-initial-hero h1 {
            font-size: clamp(2.2rem, 5vw, 4rem);
            margin-bottom: 20px;
            color: #ffffff !important;
            text-shadow: 0 4px 20px rgba(0,0,0,0.7), 0 2px 8px rgba(0,0,0,0.4);
            line-height: 1.15;
            text-align: center; /* Center the text properly */
        }"""

if old_css in css:
    css = css.replace(old_css, new_css)
else:
    print("Warning: EXACT block not found, trying regex fallback...")
    css = re.sub(r'(\.gate-initial-hero\s*h1\s*\{[^}]+?line-height:\s*1\.15;)', r'\1\n            text-align: center;', css)

# Make sure .hero-glass-panel text is generally centered just in case
old_panel = """        .hero-glass-panel {
            background: rgba(5, 6, 12, 0.62);
            backdrop-filter: blur(28px);
            -webkit-backdrop-filter: blur(28px);
            border: 1px solid rgba(212, 175, 100, 0.15);
            padding: 36px 52px;
            border-radius: 28px;
            box-shadow: 0 24px 56px rgba(0,0,0,0.55), 0 0 0 1px rgba(212,175,100,0.08) inset, inset 0 1px 0 rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
            align-items: center;
        }"""

new_panel = """        .hero-glass-panel {
            background: rgba(5, 6, 12, 0.62);
            backdrop-filter: blur(28px);
            -webkit-backdrop-filter: blur(28px);
            border: 1px solid rgba(212, 175, 100, 0.15);
            padding: 36px 52px;
            border-radius: 28px;
            box-shadow: 0 24px 56px rgba(0,0,0,0.55), 0 0 0 1px rgba(212,175,100,0.08) inset, inset 0 1px 0 rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }"""

if old_panel in css:
    css = css.replace(old_panel, new_panel)

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Cache bust
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/style.css?v=14', 'assets/style.css?v=15')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Text alignment applied.")

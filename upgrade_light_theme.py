import io

css_path = 'assets/style.css'

with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace the root light variables
old_root_light = """        :root[data-theme="light"] {
            --bg: #fdfbf7;
            --bg-deep: #ffffff;
            --text: #1d1d1f;
            --text-muted: #86868b;
            --gold: #b38b4d;
            --gold-light: #d4af64;
            --gold-glow: rgba(179, 139, 77, 0.12);
            --border: rgba(255, 255, 255, 0.5);
            --border-hover: rgba(255, 255, 255, 0.8);
            --surface: rgba(255, 255, 255, 0.35);
            --surface-hover: rgba(255, 255, 255, 0.55);
            
            --header-bg: rgba(253, 251, 247, 0.95); /* Creamy warm white */
            --header-scrolled-bg: rgba(253, 251, 247, 0.98);
        }"""
        
new_root_light = """        :root[data-theme="light"] {
            --bg: #f5f5f7;
            --bg-deep: #ffffff;
            --text: #1d1d1f;
            --text-muted: #6e6e73;
            --gold: #b38b4d;
            --gold-light: #d4af64;
            --gold-glow: rgba(179, 139, 77, 0.12);
            --border: rgba(0, 0, 0, 0.08);
            --border-hover: rgba(212, 175, 100, 0.4);
            --surface: rgba(255, 255, 255, 0.85);
            --surface-hover: #ffffff;
            
            --header-bg: rgba(245, 245, 247, 0.95); /* Apple-like light grey */
            --header-scrolled-bg: rgba(245, 245, 247, 0.98);
        }"""
css = css.replace(old_root_light, new_root_light)

# 2. Update the light glass-card
old_glass_light = """        :root[data-theme="light"] .glass-card {
            background: #ffffff;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(0, 0, 0, 0.08);
        }"""

new_glass_light = """        :root[data-theme="light"] .glass-card {
            background: #ffffff;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.06), 0 2px 6px rgba(0, 0, 0, 0.04);
            border: 1px solid rgba(0, 0, 0, 0.08);
            transform: translateY(0);
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        }"""
css = css.replace(old_glass_light, new_glass_light)

# 3. Fix the scrolled header background to match new bg
css = css.replace("background: #fdfbf7;", "background: #f5f5f7;")

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# 4. Update index.html version tag to bust cache
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/style.css?v=2', 'assets/style.css?v=3')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Light theme upgraded.")

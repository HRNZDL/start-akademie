import io

css_path = 'assets/style.css'
with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Bring back the underline in light mode and fix the active link color for transparent header
old_nav_light = """        :root[data-theme="light"] header .nav-link:hover,
        :root[data-theme="light"] header .nav-link.active,
        :root[data-theme="light"] header .lang-btn:hover {
            color: var(--gold) !important; 
        }
        
        :root[data-theme="light"] .nav-link::after {
            display: none !important;
        }"""

new_nav_light = """        /* When scrolled (light background), active/hover is gold */
        :root[data-theme="light"] header.scrolled .nav-link:hover,
        :root[data-theme="light"] header.scrolled .nav-link.active,
        :root[data-theme="light"] header.scrolled .lang-btn:hover {
            color: var(--gold) !important; 
        }

        /* When NOT scrolled (transparent background over bright sky), keep it white but add text shadow and underline */
        :root[data-theme="light"] header:not(.scrolled) .nav-link:hover,
        :root[data-theme="light"] header:not(.scrolled) .nav-link.active,
        :root[data-theme="light"] header:not(.scrolled) .lang-btn:hover {
            color: #ffffff !important; 
            text-shadow: 0 4px 16px rgba(0,0,0,0.9), 0 0 8px rgba(0,0,0,0.6);
        }

        /* Re-enable the gold underline indicator in light mode for active links */
        :root[data-theme="light"] .nav-link::after {
            display: block !important;
            height: 2px;
            bottom: -4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }"""

if old_nav_light in css:
    css = css.replace(old_nav_light, new_nav_light)
else:
    # If slight string differences exist
    print("Could not find the exact old block. Doing targeted replace.")
    css = css.replace("        :root[data-theme=\"light\"] .nav-link::after {\n            display: none !important;\n        }", "        /* Underline restored */")

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html version tag to bust cache
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/style.css?v=4', 'assets/style.css?v=5')
html = html.replace('assets/lang.js?v=6', 'assets/lang.js?v=7')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Nav link visibility fixed.")

import io
import re

html_path = 'index.html'
css_path = 'assets/style.css'

# 1. Update HTML
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update In-Person Camp list to use Lucide check-circle icons
inperson_features = ['f1', 'f2', 'f3', 'f4']
for f in inperson_features:
    old_line = re.search(r'<li class="check" data-i18n="camp\.inperson\.' + f + r'">.*?</li>', html)
    if old_line:
        content = old_line.group(0).replace('<li class="check" data-i18n="camp.inperson.' + f + '">', '')
        content = content.replace('</li>', '')
        new_line = f'<li style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px;"><i data-lucide="check-circle" style="color: var(--gold); width: 18px; min-width: 18px; margin-top: 2px;"></i> <span data-i18n="camp.inperson.{f}">{content}</span></li>'
        html = html.replace(old_line.group(0), new_line)

# Update Online Camp tags to badges
class_tags = ['class11', 'class12', 'class13']
for c in class_tags:
    old_tag = re.search(r'<span style="font-family: var\(--font-mono\); font-size: 0\.72rem; color: var\(--gold\); letter-spacing: 0\.1em; display: block; margin-bottom: 8px;" data-i18n="camp\.' + c + r'\.tag">.*?</span>', html)
    if old_tag:
        content = old_tag.group(0).split('">')[-1].replace('</span>', '')
        new_tag = f'<span style="display: inline-block; background: var(--gold-glow); color: var(--gold); padding: 4px 12px; border-radius: 20px; font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.1em; font-weight: 600; margin-bottom: 16px;" data-i18n="camp.{c}.tag">{content}</span>'
        html = html.replace(old_tag.group(0), new_tag)

# Update Online Camp lists to have subtle bullets and spacing
for c in class_tags:
    for i in range(1, 5):
        old_li = re.search(r'<li data-i18n="camp\.' + c + r'\.p' + str(i) + r'">.*?</li>', html)
        if old_li:
            content = old_li.group(0).split('">', 1)[-1].replace('</li>', '')
            new_li = f'<li style="display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05);"><div style="width: 6px; height: 6px; background: var(--gold); border-radius: 50%; margin-top: 8px; min-width: 6px; opacity: 0.5;"></div> <span style="line-height: 1.5;" data-i18n="camp.{c}.p{i}">{content}</span></li>'
            html = html.replace(old_li.group(0), new_li)

# Bust cache again
html = html.replace('assets/lang.js?v=4', 'assets/lang.js?v=5')
html = html.replace('assets/style.css', 'assets/style.css?v=2')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update CSS
with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add Light Mode CSS for wizard buttons and progress bar
light_mode_css = """
        /* Light Theme Wizard Enhancements */
        :root[data-theme="light"] .wizard-btn-option {
            background: #ffffff;
            border: 1px solid rgba(0, 0, 0, 0.12);
            color: #333333;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        }
        :root[data-theme="light"] .wizard-btn-option:hover {
            border-color: var(--gold);
            background: #fdfbf7;
            color: var(--gold);
            box-shadow: 0 8px 24px rgba(212, 175, 100, 0.12);
            transform: translateY(-2px);
        }
        :root[data-theme="light"] .wizard-progress {
            background: rgba(0, 0, 0, 0.06);
        }
        :root[data-theme="light"] .wizard-step h4 {
            color: #111111;
        }

        /* Online Camp Cards Hover Lift */
        #camp .glass-card {
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        #camp .glass-card:hover {
            transform: translateY(-8px);
        }
        
        /* Fix list borders in light mode */
        :root[data-theme="light"] #camp li[style*="border-bottom"] {
            border-bottom: 1px solid rgba(0,0,0,0.06) !important;
        }
"""

if "Light Theme Wizard Enhancements" not in css:
    css += light_mode_css

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("UI enhancements applied.")

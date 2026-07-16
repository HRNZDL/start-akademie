import io

css_path = 'assets/style.css'

with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Dark Theme .glass-card:hover
old_glass_hover_dark = """        .glass-card:hover {
            border-color: var(--border-hover);
            background: var(--surface-hover);
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(212, 175, 100, 0.05);
            transform: translateY(-5px);
        }"""
new_glass_hover_dark = """        .glass-card:hover {
            border-color: var(--gold);
            background: var(--surface-hover);
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.6), 0 0 24px rgba(212, 175, 100, 0.2);
            transform: translateY(-8px);
        }"""
css = css.replace(old_glass_hover_dark, new_glass_hover_dark)

# 2. Light Theme .glass-card:hover
old_glass_hover_light = """        :root[data-theme="light"] .glass-card:hover {
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.08);
            border-color: rgba(212, 175, 100, 0.3);
        }"""
new_glass_hover_light = """        :root[data-theme="light"] .glass-card:hover {
            box-shadow: 0 30px 60px rgba(212, 175, 100, 0.15), 0 15px 30px rgba(0, 0, 0, 0.05);
            border-color: var(--gold);
            transform: translateY(-8px);
        }"""
css = css.replace(old_glass_hover_light, new_glass_hover_light)


# 3. Wizard Button Hover (Light Theme)
old_wizard_hover_light = """        :root[data-theme="light"] .wizard-btn-option:hover {
            border-color: var(--gold);
            background: #fdfbf7;
            color: var(--gold);
            box-shadow: 0 8px 24px rgba(212, 175, 100, 0.12);
            transform: translateY(-2px);
        }"""
new_wizard_hover_light = """        :root[data-theme="light"] .wizard-btn-option:hover {
            border-color: var(--gold);
            background: #ffffff;
            color: var(--gold);
            box-shadow: 0 12px 32px rgba(212, 175, 100, 0.25);
            transform: translateY(-4px);
        }"""
css = css.replace(old_wizard_hover_light, new_wizard_hover_light)


# 4. Wizard Button Hover (Dark Theme)
old_wizard_hover_dark = """        .wizard-btn-option:hover {
            border-color: var(--gold);
            background: rgba(212, 175, 100, 0.05);
            color: var(--gold-light);
        }"""
new_wizard_hover_dark = """        .wizard-btn-option:hover {
            border-color: var(--gold);
            background: rgba(212, 175, 100, 0.08);
            color: var(--gold-light);
            box-shadow: 0 8px 24px rgba(212, 175, 100, 0.15);
            transform: translateY(-4px);
        }"""
css = css.replace(old_wizard_hover_dark, new_wizard_hover_dark)


# 5. Camp Cards Hover
old_camp_hover = """        #camp .glass-card:hover {
            transform: translateY(-8px);
        }"""
new_camp_hover = """        #camp .glass-card:hover {
            transform: translateY(-12px);
            box-shadow: 0 40px 80px rgba(0, 0, 0, 0.2), 0 0 30px rgba(212, 175, 100, 0.15);
        }
        :root[data-theme="light"] #camp .glass-card:hover {
            box-shadow: 0 40px 80px rgba(212, 175, 100, 0.15), 0 15px 30px rgba(0, 0, 0, 0.08);
        }"""
css = css.replace(old_camp_hover, new_camp_hover)

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Hover effects upgraded successfully.")

import os

def fix_html_sifirs(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    replacements = {
        'httpsıfıraunces': 'https://fonts.googleapis.com/css2?family=Fraunces',
        'script sıfıre.com': 'script src="https://cdnjs.cloudflare.com',
        'Hausıfıreuung': 'Hausaufgabenbetreuung',
        'clasıfıres"': 'class="features"',
        'clasıfıred-badge"': 'class="featured-badge"',
        'clasıfırm-box"': 'class="form-box"',
        'clasıfırm"': 'class="form"',
        'clasıfırow-2"': 'class="form-row-2"',
        'clasıfıroup"': 'class="form-group"',
        'clasıfıreview"': 'class="file-preview"',
        'id="sıfıreview"': 'id="selected-file-preview"',
        'clasıfırid"': 'class="footer-grid"',
        'clasıfır-logo"': 'class="footer-logo"',
        'clasıfır-links"': 'class="footer-links"',
        'clasıfır-bottom"': 'class="footer-bottom"',
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

fix_html_sifirs('index.html')
print('Done fixing remaining sıfırs in HTML')

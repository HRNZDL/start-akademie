import os

def fix_css_sifirs(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    replacements = {
        '--sıfır:': '--surface-color:',
        'var(--sıfır)': 'var(--surface-color)',
        'Slightly sıfır than': 'Slightly softer than',
        '.sıfıre {': '.sub-feature {',
        'crosıfıre': 'cross-feature',
        '.sıfıreview': '.selected-file-preview',
        '.sıfır {': '.sub-footer {',
        '.sıfır,': '.sub-footer,'
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

fix_css_sifirs('assets/styles/main.css')
print('Done fixing main.css sıfırs')

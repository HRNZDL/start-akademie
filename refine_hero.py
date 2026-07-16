import re

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Refine hero-glass-panel
old_panel = '''        .hero-glass-panel {
            background: rgba(14, 16, 21, 0.45);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 32px;
            padding: 80px 100px;
            text-align: center;
            box-shadow: 0 40px 100px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.05);
            max-width: 900px;
            width: 90%;
        }'''

new_panel = '''        .hero-glass-panel {
            background: rgba(14, 16, 21, 0.55); /* Slightly darker for better text contrast */
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12); /* Brighter edge */
            border-radius: 24px; /* More elegant curve */
            padding: 56px 64px; /* Tighter, more cohesive padding */
            text-align: center;
            box-shadow: 0 40px 100px rgba(0,0,0,0.7), inset 0 0 0 1px rgba(255,255,255,0.08);
            max-width: 800px; /* Better line breaks */
            width: 90%;
        }'''

css = css.replace(old_panel, new_panel)

# Refine h1
old_h1 = '''        .gate-initial-hero h1 {
            font-size: clamp(2.2rem, 5vw, 4rem);
            margin-bottom: 20px;
            color: #ffffff !important;
            text-shadow: 0 4px 20px rgba(0,0,0,0.6);
            letter-spacing: -0.03em;
            line-height: 1.1;
            font-weight: 600;
        }'''

new_h1 = '''        .gate-initial-hero h1 {
            font-size: clamp(2.6rem, 5.5vw, 4.4rem); /* Larger, more impactful */
            margin-bottom: 24px;
            color: #ffffff !important;
            text-shadow: 0 8px 32px rgba(0,0,0,0.8); /* Deeper shadow */
            letter-spacing: -0.02em;
            line-height: 1.05; /* Tighter line height for premium feel */
            font-weight: 500; /* Slightly lighter weight for elegance */
        }'''

css = css.replace(old_h1, new_h1)

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html to force proper line break for the title
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    lang = f.read()

# Add a manual break <br> to ensure "Deutschland" drops to the next line beautifully
lang = lang.replace('"Ihr Bildungsweg <em>in Deutschland</em>"', '"Ihr Bildungsweg in <br><em>Deutschland</em>"')
# Do it for all occurrences
lang = lang.replace('"Ihr Bildungsweg <em>in Deutschland</em>"', '"Ihr Bildungsweg in <br><em>Deutschland</em>"')
# Just in case for Turkish too
lang = lang.replace('"Almanya\'da Eğitim Yolunuz <em>Burada Başlar</em>"', '"Almanya\'da Eğitim Yolunuz <br><em>Burada Başlar</em>"')

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(lang)

# Update index.html cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=28', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

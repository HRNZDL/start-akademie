import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section[^>]*>(.*?)</section>', text, re.DOTALL | re.IGNORECASE)
with open('sections_dump.txt', 'w', encoding='utf-8') as out:
    for i, s in enumerate(sections):
        h2s = re.findall(r'<h[12][^>]*>(.*?)</h[12]>', s, re.IGNORECASE)
        out.write(f'Section {i}: {h2s}\n')

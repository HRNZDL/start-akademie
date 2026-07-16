import re

with open(r'assets\js\main.js', 'r', encoding='utf-8') as f:
    js = f.read()

ids = re.findall(r'getElementById\([\'"](.*?)[\'"]\)', js)
ids += re.findall(r'querySelector\([\'"]#(.*?)[\'"]\)', js)
unique_ids = set(ids)
print('Expected IDs in main.js:', unique_ids)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

missing_ids = []
for idx in unique_ids:
    if f'id="{idx}"' not in html and f"id='{idx}'" not in html:
        # Also check for regex or complex cases
        if not re.search(f'id\\s*=\\s*[\'"]{idx}[\'"]', html):
            missing_ids.append(idx)

print('Missing IDs in index.html:', missing_ids)

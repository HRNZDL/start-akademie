import re

with open(r'assets\js\main.js', 'r', encoding='utf-8') as f:
    js = f.read()

ids = re.findall(r'getElementById\([\'"](.*?)[\'"]\)', js)
ids += re.findall(r'querySelector\([\'"]#(.*?)[\'"]\)', js)
unique_ids = set(ids)

with open('index.backup.html', 'r', encoding='utf-8') as f:
    html = f.read()

missing_ids = []
for idx in unique_ids:
    if f'id="{idx}"' not in html and f"id='{idx}'" not in html:
        if not re.search(f'id\\s*=\\s*[\'"]{idx}[\'"]', html):
            missing_ids.append(idx)

print('Missing IDs in index.backup.html:', len(missing_ids))
print('Total IDs expected:', len(unique_ids))

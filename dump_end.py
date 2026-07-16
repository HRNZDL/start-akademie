import json
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open('index_end.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines[-30:]):
        out.write(f"{len(lines)-30+i}: {line}")

import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'loading-screen' in line:
        start = max(0, i)
        end = min(len(lines), i+15)
        print(''.join(lines[start:end]))
        break

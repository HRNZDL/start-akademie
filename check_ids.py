import re

with open('index-test.html', 'r', encoding='utf-8') as f:
    html = f.read()

ids = re.findall(r'id="([^"]+)"', html)
important = ['canvas-3d', 'navbar', 'startbot-panel', 'action-modal', 'game-hud-overlay', 'mobile-menu-panel', 'gate-canvas']
for i in important:
    print(i, ':', i in ids)

print('\nAll ids in file:', ids[:30])

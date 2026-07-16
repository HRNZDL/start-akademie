import re

with open('index.backup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check what the hero section looks like
hero_match = re.search(r'id="hero".*?</section>', html, re.DOTALL)
if hero_match:
    print("Hero found, length:", len(hero_match.group(0)))
    print("Has gate-canvas:", 'gate-canvas' in hero_match.group(0))
    print("Has canvas-3d:", 'canvas-3d' in hero_match.group(0))
    print("Has portal:", 'portal' in hero_match.group(0))
else:
    print("No hero section found!")

# Check for Three.js
if 'three' in html.lower():
    print("Three.js FOUND inline!")
else:
    print("No Three.js inline")
    
# Total size
print("Total size:", len(html))

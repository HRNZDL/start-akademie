import os

html_path = 'index.html'
js_path = r'assets\js\main.js'
css_path = r'assets\styles\main.css'

print(f"index.html exists: {os.path.exists(html_path)}")
print(f"main.js exists: {os.path.exists(js_path)}")
print(f"main.css exists: {os.path.exists(css_path)}")

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()
    print(f"Has main.css link: {'assets/styles/main.css' in html}")
    print(f"Has main.js script: {'assets/js/main.js' in html}")
    print(f"Has GSAP library: {'gsap' in html}")
    print(f"Has ThreeJS library: {'three' in html}")
    print(f"Has Canvas: {'canvas' in html}")

if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
        print(f"JS length: {len(js)}")
        # Check if there's any unclosed template literals or missing functions
        if 'TOTAL_FRAMES' in js:
            print("Found TOTAL_FRAMES in main.js")

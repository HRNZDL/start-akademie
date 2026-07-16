import re

# We will use the June 3rd backup as the base structure
with open('index.backup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Strip the old dummy CSS and JS blocks
style_pattern = r'<style[^>]*>.*?</style>'
script_pattern = r'<script[^>]*>.*?</script>'

# Find all styles and remove the big ones
styles = re.findall(style_pattern, html, re.DOTALL)
for s in styles:
    if len(s) > 1000:
        html = html.replace(s, '<!-- STYLE INJECT -->', 1)

scripts = re.findall(script_pattern, html, re.DOTALL)
for s in scripts:
    if len(s) > 1000:
        html = html.replace(s, '<!-- SCRIPT INJECT -->', 1)

# Now inject the June 3rd main.css and main.js
with open(r'assets\styles\main.css', 'r', encoding='utf-8') as f:
    main_css = f.read()
    
with open(r'assets\js\main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# Add ThreeJS, ScrollTrigger, Lenis dependencies
deps = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/@studio-freight/lenis@1.0.33/dist/lenis.min.js"></script>
"""

new_style = f"<style>\n{main_css}\n</style>"
new_script = f"{deps}\n<script>\n{main_js}\n</script>"

html = html.replace('<!-- STYLE INJECT -->', new_style, 1)
html = html.replace('<!-- STYLE INJECT -->', '') # clear duplicates if any

html = html.replace('<!-- SCRIPT INJECT -->', new_script, 1)
html = html.replace('<!-- SCRIPT INJECT -->', '')

# Save the monolithic file
with open('index_monolithic.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Created index_monolithic.html")

import re

html_path = 'index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the giant inline <style> block
style_pattern = r'<style[^>]*>.*?</style>'
styles = re.findall(style_pattern, html, re.DOTALL)
for s in styles:
    if len(s) > 1000:
        html = html.replace(s, '<link rel="stylesheet" href="assets/styles/main.css">', 1)

# 2. Replace the giant inline <script> block
script_pattern = r'<script[^>]*>.*?</script>'
scripts = re.findall(script_pattern, html, re.DOTALL)
for s in scripts:
    if len(s) > 1000:
        # Inject dependencies right before the main.js script
        deps = """
    <!-- Immersive 3D and Animation Dependencies -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="https://unpkg.com/@studio-freight/lenis@1.0.33/dist/lenis.min.js"></script>
    <script src="assets/js/main.js"></script>
"""
        html = html.replace(s, deps, 1)

# 3. Save the stripped HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Stripped inline CSS and JS, injected external links and dependencies.")

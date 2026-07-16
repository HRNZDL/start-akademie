import re
import os

with open('index-test.html', 'r', encoding='utf-8') as f:
    source_html = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    target_html = f.read()

# We want to find sections or tags in source_html that have custom text, and map them to target_html.
# Because the structure might be different, let's extract all <h1/2/3/4>, <p>, <li>, <a> tags that have Turkish/German text.
# Actually, the simplest way is to look for common sections by ID or class.
sections_to_check = [
    ('Hero/Portal Slide 1', r'<div class="portal-slide" id="portal-slide-1">.*?</div>\s*</div>\s*<!-- Slide 2'),
    ('Portal Slide 2', r'<div class="portal-slide" id="portal-slide-2">.*?</div>\s*</div>\s*<!-- Slide 3'),
    ('Portal Slide 3', r'<div class="portal-slide" id="portal-slide-3">.*?</div>\s*</div>\s*</div>'),
    ('About Us', r'<section[^>]*id="about"[^>]*>.*?</section>'),
    ('Services', r'<section[^>]*id="services"[^>]*>.*?</section>'),
    ('Contact', r'<section[^>]*id="contact"[^>]*>.*?</section>'),
    ('Features', r'<section[^>]*id="features"[^>]*>.*?</section>')
]

def get_block(regex, html):
    match = re.search(regex, html, re.DOTALL | re.IGNORECASE)
    return match.group(0) if match else None

for name, pattern in sections_to_check:
    src_block = get_block(pattern, source_html)
    tgt_block = get_block(pattern, target_html)
    
    if src_block and tgt_block:
        # If both exist, replace the target block with the source block, BUT we might lose 3D IDs.
        # Wait, if we replace the whole block, we lose the new IDs.
        pass

# Let's see what is inside index-test.html vs index.html
with open('diff_check.py', 'w') as f:
    f.write("print('Diff check script generated')")

print("Let's first dump the text from index-test.html for the hero section.")
match = re.search(r'<section[^>]*hero[^>]*>.*?</section>', source_html, re.DOTALL | re.IGNORECASE)
if match:
    print("Source Hero:\n", match.group(0)[:500])
else:
    print("No hero in source")

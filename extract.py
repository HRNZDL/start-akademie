import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

sections = ['nachhilfe-details', 'wizard', 'camp', 'visa-faq']
res = ""

for sec in sections:
    # Pattern looks for <section ... id="section_name"> ... </section>
    m = re.search(f'<section[^>]*id="{sec}"[^>]*>.*?</section>', content, re.DOTALL)
    if m:
        res += f"=== {sec.upper()} ===\n" + m.group(0) + "\n\n"
    else:
        # Fallback if id is in a different order
        m2 = re.search(f'<section[^>]*id="{sec}".*?</section>', content, re.DOTALL)
        if m2:
             res += f"=== {sec.upper()} ===\n" + m2.group(0) + "\n\n"

os.makedirs('scratch', exist_ok=True)
with open('scratch/sections_to_translate.html', 'w', encoding='utf-8') as f:
    f.write(res)
print("Saved to scratch/sections_to_translate.html")

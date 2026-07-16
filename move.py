import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Match the entire visa-faq section
faq_match = re.search(r'<section class="section-padding" style="background: var\(--bg-deep\);" id="visa-faq">.*?</section>', content, re.DOTALL)

if faq_match:
    faq_content = faq_match.group(0)
    # Remove from original position
    content = content.replace(faq_content, '')
    
    # Find contact section position
    contact_pos = content.find('<section class="section-padding" id="contact">')
    if contact_pos != -1:
        # Insert before contact section
        new_content = content[:contact_pos] + faq_content + '\n\n    ' + content[contact_pos:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully moved visa-faq to right before contact section.")
    else:
        print("Could not find contact section.")
else:
    print("Could not find visa-faq section.")

from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

untranslated = []

# Elements that typically contain text
for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', 'button', 'li', 'label', 'strong']):
    if not tag.has_attr('data-i18n'):
        # Check if any ancestor has data-i18n (some translations might be HTML blobs)
        ancestor_has_i18n = any(parent.has_attr('data-i18n') for parent in tag.parents if parent.name != '[document]')
        if not ancestor_has_i18n:
            text = tag.get_text(strip=True)
            # Filter out empty strings, numbers, or very short punctuation
            if text and len(text) > 2 and not text.isdigit() and not re.match(r'^[\W_]+$', text):
                untranslated.append((tag.name, text))

# For inputs and textareas check placeholder attributes
for tag in soup.find_all(['input', 'textarea']):
    if tag.has_attr('placeholder') and not tag.has_attr('data-i18n-placeholder'):
        untranslated.append((tag.name + ' (placeholder)', tag['placeholder']))

with open('scratch/untranslated.txt', 'w', encoding='utf-8') as f:
    for name, text in untranslated:
        f.write(f"[{name}] {text}\n")

print(f"Found {len(untranslated)} potentially untranslated items. Saved to scratch/untranslated.txt")

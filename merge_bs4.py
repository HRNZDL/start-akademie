from bs4 import BeautifulSoup
import re

with open('index-test.html', 'r', encoding='utf-8') as f:
    soup_src = BeautifulSoup(f, 'html.parser')

with open('index.html', 'r', encoding='utf-8') as f:
    soup_tgt = BeautifulSoup(f, 'html.parser')

# We want to transfer inner texts from source to target for common tags
# Because the structure might be different, let's just grab all texts from headers and paragraphs
def extract_texts(soup, tags):
    return [t.get_text(strip=True) for t in soup.find_all(tags) if t.get_text(strip=True)]

src_texts = extract_texts(soup_src, ['h1', 'h2', 'h3', 'h4', 'p'])
tgt_elements = soup_tgt.find_all(['h1', 'h2', 'h3', 'h4', 'p'])

# Try to map sequentially
min_len = min(len(src_texts), len(tgt_elements))
for i in range(min_len):
    # Only replace if the target text is not empty and is purely text (no nested complex tags other than formatting)
    if tgt_elements[i].string:
        tgt_elements[i].string.replace_with(src_texts[i])

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup_tgt))
    
print(f"Transferred {min_len} text nodes.")

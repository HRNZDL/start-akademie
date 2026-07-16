from bs4 import BeautifulSoup
import re

with open('index-test.html', 'r', encoding='utf-8') as f:
    soup_src = BeautifulSoup(f, 'html.parser')

with open('index_monolithic.html', 'r', encoding='utf-8') as f:
    soup_tgt = BeautifulSoup(f, 'html.parser')

# Extract texts
def extract_texts(soup, tags):
    return [t.get_text(strip=True) for t in soup.find_all(tags) if t.get_text(strip=True)]

src_texts = extract_texts(soup_src, ['h1', 'h2', 'h3', 'h4', 'p'])
tgt_elements = soup_tgt.find_all(['h1', 'h2', 'h3', 'h4', 'p'])

# Merge sequentially
min_len = min(len(src_texts), len(tgt_elements))
for i in range(min_len):
    if tgt_elements[i].string:
        tgt_elements[i].string.replace_with(src_texts[i])

# Fix HTML formatting/entities issues by using the raw string instead of bs4 write if possible, 
# but bs4 is our only option to preserve nodes here.
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup_tgt))
    
print(f"Merged text and created final monolithic index.html")

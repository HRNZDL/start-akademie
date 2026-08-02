# -*- coding: utf-8 -*-
import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Pattern: mobile drawer lang buttons with onclick but no data-lang
# <span class="lang-btn" onclick="changeLanguage('tr')" ...>TR</span>
pattern = re.compile(
    r"(<span\s+class=\"lang-btn\"\s+)(onclick=\"changeLanguage\('(tr|en|de)'\)\")",
    re.IGNORECASE
)

def add_data_lang(m):
    lang = m.group(3)
    return m.group(1) + 'data-lang="' + lang + '" ' + m.group(2)

fixed = []
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = pattern.sub(add_data_lang, content)
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed.append(fname)
        print('Fixed: ' + fname)

print('Done! Fixed ' + str(len(fixed)) + ' files.')

# -*- coding: utf-8 -*-
import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove onclick from spans that already have data-lang
    # Match: data-lang="xx" ... onclick="changeLanguage('xx')"
    new_content = re.sub(
        r'(<span[^>]*data-lang=["\'][^"\']+["\'][^>]*)\s+onclick=["\'][^"\']*["\']',
        r'\1',
        content
    )
    # Also the reverse order: onclick first then data-lang
    new_content = re.sub(
        r'(<span[^>]*)\s+onclick=["\'][^"\']*["\']([^>]*data-lang=["\'][^"\']+["\'][^>]*>)',
        r'\1\2',
        new_content
    )

    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Fixed: ' + fname)
    else:
        print('No change: ' + fname)

print('Done!')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html2 = html.replace("url('assets/heidelberg.png')", "url('assets/gate.png')")
count = html.count("url('assets/heidelberg.png')")
print(f"Replaced {count} occurrences")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('Done - replaced heidelberg.png with gate.png in gate door CSS')

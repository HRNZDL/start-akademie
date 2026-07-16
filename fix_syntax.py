with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('systemPrompt + "\\n\\nKullanıcı sorusu: "', 'systemPrompt + "\\\\n\\\\nKullanıcı sorusu: "')
html = html.replace('systemPrompt + "\n\nKullanıcı sorusu: "', 'systemPrompt + "\\\\n\\\\nKullanıcı sorusu: "')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed JS syntax error')

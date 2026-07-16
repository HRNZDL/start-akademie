with open('assets/lang.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('"Özgür Üniversite"', '\\"Özgür Üniversite\\"')
text = text.replace("'Özgür Üniversite'", "\\'Özgür Üniversite\\'")

# Also check for Free University in EN
text = text.replace('"Free University"', '\\"Free University\\"')
# And DE
text = text.replace('"Freie Universität"', '\\"Freie Universität\\"')

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(text)

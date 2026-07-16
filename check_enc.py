with open('index.backup.html', 'r', encoding='utf-8') as f:
    text = f.read()
import re
with open('enc_res.txt', 'w', encoding='utf-8') as out:
    out.write(f"sıfır: {len(re.findall('sıfır', text))}\n")
    out.write(f"scrollö: {len(re.findall('scrollö', text))}\n")
    out.write(f"forö: {len(re.findall('forö', text))}\n")

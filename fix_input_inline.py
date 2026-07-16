import io
import re

html_path = 'index.html'

with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace inline styled input with a clean one
# Old: <input type="text" placeholder="Sorunuzu buraya yazın..." id="startbot-text" style="flex-grow:1; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px; color:#fff;" onkeypress="if(event.key === 'Enter') sendBotMsg()">

# Since there are Turkish characters, regex is safer to catch the element
html = re.sub(
    r'<input type="text"[^>]*id="startbot-text"[^>]*onkeypress="if\(event\.key === \'Enter\'\) sendBotMsg\(\)">', 
    r'<input type="text" placeholder="Sorunuzu buraya yazın..." id="startbot-text" onkeypress="if(event.key === \'Enter\') sendBotMsg()">', 
    html
)

# And fix the button inline style just in case
# Old: <button onclick="sendBotMsg()" style="background:var(--gold); color:black; border:none; border-radius:6px; padding:10px; cursor:pointer;"><i data-lucide="send"></i></button>
html = re.sub(
    r'<button onclick="sendBotMsg\(\)" style="[^"]*"><i data-lucide="send"></i></button>',
    r'<button onclick="sendBotMsg()"><i data-lucide="send"></i></button>',
    html
)

html = html.replace('assets/style.css?v=9', 'assets/style.css?v=10')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Inline styles removed from input.")

import os

def fix_sifir_in_js():
    js_path = 'assets/js/main.js'
    if os.path.exists(js_path):
        with open(js_path, 'r', encoding='utf-8') as f:
            text = f.read()

        text = text.replace("sıfıreview", "selected-file-preview")
        text = text.replace("asıfırame_", "assets/frames/frame_")
        text = text.replace("httpsıfırateContent", "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent")
        text = text.replace('class="btn btn-primary" sıfırem;', 'class="btn btn-primary" style="font-size:0.9rem;')
        text = text.replace('class="btn btn-outline" sıfırem;', 'class="btn btn-outline" style="font-size:0.9rem;')

        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print("Fixed main.js")

fix_sifir_in_js()

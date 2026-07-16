import os

def fix_question_marks():
    # Fix lang.js
    lang_path = 'assets/lang.js'
    if os.path.exists(lang_path):
        with open(lang_path, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace('🔸', '?')
        with open(lang_path, 'w', encoding='utf-8') as f:
            f.write(text)
            
    # Fix index.html
    index_path = 'index.html'
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Replace 🔸 with ? but skip <span>🔸 
        # We can just temporarily protect <span>🔸 
        text = text.replace('<span>🔸 ', 'SPAN_BULLET_PLACEHOLDER')
        text = text.replace('🔸', '?')
        text = text.replace('SPAN_BULLET_PLACEHOLDER', '<span>🔸 ')
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(text)

fix_question_marks()
print('Done fixing ?')

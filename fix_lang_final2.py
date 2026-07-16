import json
import codecs

with open('keys.json', 'r', encoding='utf-8') as f:
    tr_keys = json.load(f)

# The bot keys to be preserved
bot_keys = {
    "tr": {
        "bot.greeting": "Merhaba! Start Akademie eğitim danışmanlığı asistanına hoş geldiniz. Almanya'da eğitim vizesi, bloke hesap ve lise ders destekleri hakkında size nasıl yardımcı olabilirim?",
        "bot.chip_uni": "🎓 Üni Kayıt Evrakları",
        "bot.chip_but": "📝 BuT Evrakları",
        "bot.chip_bloke": "Bloke Hesap Miktarı",
        "bot.chip_but_info": "Ücretsiz BuT Desteği",
        "bot.chip_contact": "Adres & İletişim"
    },
    "en": {
        "bot.greeting": "Hello! Welcome to the Start Akademie assistant. How can I help you with education visas, blocked accounts, or tutoring today?",
        "bot.chip_uni": "🎓 Uni Docs",
        "bot.chip_but": "📝 BuT Docs",
        "bot.chip_bloke": "Blocked Account",
        "bot.chip_but_info": "Free BuT Support",
        "bot.chip_contact": "Contact"
    },
    "de": {
        "bot.greeting": "Hallo! Willkommen beim Start Akademie Assistenten. Wie kann ich Ihnen heute bei Bildungsvisa, Sperrkonto oder Nachhilfe helfen?",
        "bot.chip_uni": "🎓 Uni-Dokumente",
        "bot.chip_but": "📝 BuT-Dokumente",
        "bot.chip_bloke": "Sperrkonto",
        "bot.chip_but_info": "Kostenlose BuT-Hilfe",
        "bot.chip_contact": "Kontakt"
    }
}

for k, v in bot_keys['tr'].items(): tr_keys[k] = v

with open('assets/lang.js', 'r', encoding='utf-8') as f:
    lang_content = f.read()

import re
# Extract the translations object
match = re.search(r'const translations = (\{.*?\});\s*function', lang_content, re.DOTALL)
if match:
    trans_str = match.group(1)
    translations = json.loads(trans_str)
    
    # Overwrite TR with perfect keys
    translations['tr'] = tr_keys
    
    # Fix EN and DE
    def fix_de_en(text):
        if not isinstance(text, str): return text
        return text.replace('ǟ', 'ü').replace('Y', 'ß').replace('', 'ä').replace('', 'ö').replace('Y', 'ß')
        
    for k in translations['en']:
        translations['en'][k] = fix_de_en(translations['en'][k])
    for k in translations['de']:
        translations['de'][k] = fix_de_en(translations['de'][k])
        
    for k, v in bot_keys['en'].items(): translations['en'][k] = v
    for k, v in bot_keys['de'].items(): translations['de'][k] = v

    # Write back
    new_lang = lang_content[:match.start()] + 'const translations = ' + json.dumps(translations, indent=4, ensure_ascii=False) + ';' + lang_content[match.end()-8:]
    with open('assets/lang.js', 'w', encoding='utf-8') as f:
        f.write(new_lang)
    print("Fixed!")
else:
    print("Could not find translations block.")

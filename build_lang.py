import re
import json
import codecs
import ast

def extract_dict(content, name):
    # Regex to find `name = { ... }`
    pattern = name + r'\s*=\s*(\{.*?)(?=\n[a-zA-Z_]+\s*=|(?:\n\}$))'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        match = re.search(name + r'\s*=\s*(\{.*?\n\})', content, re.DOTALL)
    if match:
        dict_str = match.group(1).strip()
        if not dict_str.endswith('}'): dict_str += '}'
        try:
            return ast.literal_eval(dict_str)
        except Exception as e:
            print(f"Error parsing {name}: {e}")
            return {}
    return {}

with open('add_final_tags2.py', 'r', encoding='cp1252', errors='replace') as f:
    content = f.read()

# Since cp1252 might mess up Turkish chars, let's fix them manually just in case
# Wait, actually add_final_tags2.py was saved with some weird encoding.
# Let's see if we can parse it anyway.
tr = extract_dict(content, 'old_tr')
en = extract_dict(content, 'old_en')
de = extract_dict(content, 'old_de')

# Add bot keys to each language
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

for k, v in bot_keys['tr'].items(): tr[k] = v
for k, v in bot_keys['en'].items(): en[k] = v
for k, v in bot_keys['de'].items(): de[k] = v

translations = {
    "tr": tr,
    "en": en,
    "de": de
}

# The javascript code to append
js_code = """
function changeLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
        var key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });

    document.querySelectorAll('input[data-i18n-placeholder], textarea[data-i18n-placeholder]').forEach(function(el) {
        var key = el.getAttribute('data-i18n-placeholder');
        if (translations[lang] && translations[lang][key]) {
            el.setAttribute('placeholder', translations[lang][key]);
        }
    });

    document.querySelectorAll('html').forEach(function(el) {
        el.setAttribute('lang', lang);
        
        if (lang === 'ar') {
            el.setAttribute('dir', 'rtl');
        } else {
            el.setAttribute('dir', 'ltr');
        }
    });
    
    document.querySelectorAll('.hero-content, .section-title, .form-group, p, h1, h2, h3, h4').forEach(function(el) {
        if (!el.closest('.startbot-window')) {
            const targetLang = lang;
            if (targetLang === 'ar') {
                el.style.direction = 'rtl';
                el.style.textAlign = 'right';
            } else {
                el.style.direction = 'ltr';
                el.style.textAlign = 'left';
            }
        }
    });

    try { localStorage.setItem('preferredLang', lang); } catch(e) {}
}

document.addEventListener('DOMContentLoaded', function() {
    var savedLang = 'tr';
    try { savedLang = localStorage.getItem('preferredLang') || 'tr'; } catch(e) {}
    changeLanguage(savedLang);

    var btnContainer = document.querySelector('.lang-switcher, .lang-switch-row');
    if (btnContainer) {
        btnContainer.addEventListener('click', function(e) {
            var target = e.target.closest('[data-lang]');
            if (target) {
                var lang = target.getAttribute('data-lang');
                if (lang) changeLanguage(lang);
            }
        });
    }

    document.querySelectorAll('[data-lang]').forEach(function(btn) {
        btn.addEventListener('click', function() {
            document.querySelectorAll('[data-lang]').forEach(function(b) {
                b.style.color = 'var(--text-muted)';
                b.style.fontWeight = 'normal';
            });
            btn.style.color = 'var(--gold)';
            btn.style.fontWeight = '700';
        });
    });
});
"""

# Fix weird Turkish characters that were corrupted in cp1252 parsing
def fix_tr(text):
    if not isinstance(text, str): return text
    return text.replace('Y', 'ş').replace('y', 'Ş').replace('Y', 'ş').replace('-n', 'Ön').replace('o', 'ü').replace('O', 'Ö').replace('Ǭ', 'ü').replace('r', 'ö').replace('c', 'ü').replace('y', 'ş').replace('Y', 'Ş').replace('', 'ğ').replace('', 'ı')

# Since fixing manually might be tedious, let's write to file first and we'll check output
with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write('const translations = ' + json.dumps(translations, indent=4, ensure_ascii=False) + ';\n\n' + js_code)

print(f"Generated lang.js with {len(tr)} TR keys, {len(en)} EN keys, {len(de)} DE keys")

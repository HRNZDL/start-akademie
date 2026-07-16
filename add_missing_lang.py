import io
import re

lang_path = 'assets/lang.js'

with io.open(lang_path, 'r', encoding='utf-8') as f:
    lang_js = f.read()

# First, remove any existing bot translations to avoid duplicates
lang_js = re.sub(r'\s*"bot\.greeting":.*?,', '', lang_js)
lang_js = re.sub(r'\s*"bot\.chip_uni":.*?,', '', lang_js)
lang_js = re.sub(r'\s*"bot\.chip_but":.*?,', '', lang_js)
lang_js = re.sub(r'\s*"bot\.chip_bloke":.*?,', '', lang_js)
lang_js = re.sub(r'\s*"bot\.chip_but_info":.*?,', '', lang_js)
lang_js = re.sub(r'\s*"bot\.chip_contact":.*?,', '', lang_js)

# Insert the translations properly right after the language keys
tr_insert = """    "tr": {
        "bot.greeting": "Merhaba! Start Akademie egitim danismanligi asistanina hos geldiniz. Almanya'da egitim vizesi, bloke hesap ve lise ders destekleri hakkinda size nasil yardimci olabilirim?",
        "bot.chip_uni": "🎓 Üni Kayıt Evrakları",
        "bot.chip_but": "📝 BuT Evrakları",
        "bot.chip_bloke": "Bloke Hesap Miktarı",
        "bot.chip_but_info": "Ücretsiz BuT Desteği",
        "bot.chip_contact": "Adres & İletişim",
"""

en_insert = """    "en": {
        "bot.greeting": "Hello! Welcome to the Start Akademie assistant. How can I help you with education visas, blocked accounts, or tutoring today?",
        "bot.chip_uni": "🎓 Uni Docs",
        "bot.chip_but": "📝 BuT Docs",
        "bot.chip_bloke": "Blocked Account",
        "bot.chip_but_info": "Free BuT Support",
        "bot.chip_contact": "Contact",
"""

de_insert = """    "de": {
        "bot.greeting": "Hallo! Willkommen beim Start Akademie Assistenten. Wie kann ich Ihnen heute bei Bildungsvisa, Sperrkonto oder Nachhilfe helfen?",
        "bot.chip_uni": "🎓 Uni-Dokumente",
        "bot.chip_but": "📝 BuT-Dokumente",
        "bot.chip_bloke": "Sperrkonto",
        "bot.chip_but_info": "Kostenlose BuT-Hilfe",
        "bot.chip_contact": "Kontakt",
"""

lang_js = lang_js.replace('"tr": {', tr_insert)
lang_js = lang_js.replace('"en": {', en_insert)
lang_js = lang_js.replace('"de": {', de_insert)

with io.open(lang_path, 'w', encoding='utf-8') as f:
    f.write(lang_js)

# Also force index.html cache bust again
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('assets/lang.js?v=9', 'assets/lang.js?v=10')
with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Translations forcefully added to lang.js.")

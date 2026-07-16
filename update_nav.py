import re

# 1. Add translation keys to assets/lang.js
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    lang_js = f.read()

# TR has "nav.university": "Üniversite", "nav.languages": "Dil Kursları", etc.
# We need to insert these under EN and DE blocks
# Locate EN block and insert:
en_keys = '''        "nav.university": "University",
        "nav.languages": "Language Courses",
        "nav.ausbildung": "Ausbildung",
        "nav.recognition": "Equivalence",
        "nav.exchange": "Exchange & Summer",
        "nav.accommodation": "Accommodation",
        "nav.about": "About Us",'''

de_keys = '''        "nav.university": "Universität",
        "nav.languages": "Sprachkurse",
        "nav.ausbildung": "Ausbildung",
        "nav.recognition": "Anerkennung",
        "nav.exchange": "Austausch & Sommer",
        "nav.accommodation": "Unterkunft",
        "nav.about": "Über uns",'''

# Insert in EN block after "en": {
lang_js = lang_js.replace('"en": {', '"en": {\n' + en_keys)
# Insert in DE block after "de": {
lang_js = lang_js.replace('"de": {', '"de": {\n' + de_keys)

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(lang_js)
print("Updated assets/lang.js with new keys.")

# 2. Update navigation links in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace header nav menu
old_nav_menu = """            <div class="nav-menu">
                <a href="#hero" class="nav-link active" data-i18n="nav.home">Ana Sayfa</a>
                <a href="#pillars" class="nav-link" data-i18n="nav.programs">Programlar</a>
                <a href="#universities" class="nav-link" data-i18n="nav.universities">Üniversiteler</a>
                <a href="#pricing" class="nav-link" data-i18n="nav.consulting">Danışmanlık</a>
                <a href="#wizard" class="nav-link" data-i18n="nav.test">Denklik Testi</a>
                <a href="#camp" class="nav-link" data-i18n="nav.camp">Yaz Kampı</a>
                <a href="#contact" class="nav-link" data-i18n="nav.contact">İletişim</a>
            </div>"""

new_nav_menu = """            <div class="nav-menu">
                <a href="index.html#hero" class="nav-link active" data-i18n="nav.home">Ana Sayfa</a>
                <a href="uni.html" class="nav-link" data-i18n="nav.university">Üniversite</a>
                <a href="dil.html" class="nav-link" data-i18n="nav.languages">Dil Kursları</a>
                <a href="ausbildung.html" class="nav-link" data-i18n="nav.ausbildung">Ausbildung</a>
                <a href="denklik.html" class="nav-link" data-i18n="nav.recognition">Denklik</a>
                <a href="degisim.html" class="nav-link" data-i18n="nav.exchange">Değişim ve Yaz Programları</a>
                <a href="konaklama.html" class="nav-link" data-i18n="nav.accommodation">Konaklama</a>
                <a href="hakkimizda.html" class="nav-link" data-i18n="nav.about">Hakkımızda</a>
                <a href="iletisim.html" class="nav-link" data-i18n="nav.contact">İletişim</a>
            </div>"""

html = html.replace(old_nav_menu, new_nav_menu)

# Replace mobile menu drawer
old_drawer = """        <a href="#hero" class="nav-link">Home</a>
        <a href="#pillars" class="nav-link">Programlar</a>
        <a href="#universities" class="nav-link">Üniversiteler</a>
        <a href="#pricing" class="nav-link">Danışmanlık</a>
        <a href="#wizard" class="nav-link">Denklik Testi</a>
        <a href="#camp" class="nav-link">Sommercamp</a>
        <a href="#contact" class="nav-link">İletişim</a>"""

new_drawer = """        <a href="index.html#hero" class="nav-link" data-i18n="nav.home">Home</a>
        <a href="uni.html" class="nav-link" data-i18n="nav.university">Üniversite</a>
        <a href="dil.html" class="nav-link" data-i18n="nav.languages">Dil Kursları</a>
        <a href="ausbildung.html" class="nav-link" data-i18n="nav.ausbildung">Ausbildung</a>
        <a href="denklik.html" class="nav-link" data-i18n="nav.recognition">Denklik</a>
        <a href="degisim.html" class="nav-link" data-i18n="nav.exchange">Değişim ve Yaz Programları</a>
        <a href="konaklama.html" class="nav-link" data-i18n="nav.accommodation">Konaklama</a>
        <a href="hakkimizda.html" class="nav-link" data-i18n="nav.about">Hakkımızda</a>
        <a href="iletisim.html" class="nav-link" data-i18n="nav.contact">İletişim</a>"""

html = html.replace(old_drawer, new_drawer)

# Replace header consultation button
html = html.replace('href="#contact" class="btn btn-primary btn-header-consult"', 'href="iletisim.html" class="btn btn-primary btn-header-consult"')
html = html.replace('<a href="#contact" class="btn btn-primary" style="margin-top: 20px; width: 100%;">Ön Görüşme</a>', '<a href="iletisim.html" class="btn btn-primary" style="margin-top: 20px; width: 100%;" data-i18n="nav.meeting">Ön Görüşme</a>')

# Replace footer links
html = html.replace('<li><a href="#services">Üniversite Danışmanlığı</a></li>', '<li><a href="uni.html" data-i18n="nav.university">Üniversite Danışmanlığı</a></li>')
html = html.replace('<li><a href="#services">Ausbildung (Mesleki Eğitim)</a></li>', '<li><a href="ausbildung.html" data-i18n="nav.ausbildung">Ausbildung (Mesleki Eğitim)</a></li>')
html = html.replace('<li><a href="#services">Dil Kursları</a></li>', '<li><a href="dil.html" data-i18n="nav.languages">Dil Kursları</a></li>')
html = html.replace('<li><a href="#pillars">Okul Ders Desteği (Nachhilfe)</a></li>', '<li><a href="https://www.startakademie.de/" target="_blank">Okul Ders Desteği (Nachhilfe)</a></li>')
html = html.replace('<li><a href="#services">Denklik Süreçleri</a></li>', '<li><a href="denklik.html" data-i18n="nav.recognition">Denklik Süreçleri</a></li>')

html = html.replace('<li><a href="#" data-i18n="footer.l1">Impressum</a></li>', '<li><a href="impressum.html" data-i18n="footer.l1">Impressum</a></li>')
html = html.replace('<li><a href="#">Datenschutzerklärung</a></li>', '<li><a href="datenschutz.html" data-i18n="footer.datenschutz">Datenschutzerklärung</a></li>')
html = html.replace('<a href="#" data-i18n="footer.l2">Gizlilik Sözleşmesi</a>', '<a href="datenschutz.html" data-i18n="footer.l2">Gizlilik Sözleşmesi</a>')
html = html.replace('<a href="#">Kullanım Koşulları</a>', '<a href="impressum.html" data-i18n="footer.use_terms">Kullanım Koşulları</a>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html navigation links.")

# 3. Add CSS laptop viewport fix to style.css
with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

laptop_fix = """
        /* Navigation fit for laptops with 9 items */
        @media (min-width: 1025px) and (max-width: 1400px) {
            .nav-menu {
                gap: 14px !important;
            }
            .nav-link {
                font-size: 0.72rem !important;
            }
            .btn-header-consult {
                padding: 8px 14px !important;
                font-size: 0.75rem !important;
            }
        }
"""
# Append right before the responsive section at max-width 1024px
css = css.replace('/* Responsive */\r\n        @media (max-width: 1024px) {', laptop_fix + '\n        /* Responsive */\n        @media (max-width: 1024px) {')
css = css.replace('/* Responsive */\n        @media (max-width: 1024px) {', laptop_fix + '\n        /* Responsive */\n        @media (max-width: 1024px) {')

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated assets/style.css with responsive laptop fix.")

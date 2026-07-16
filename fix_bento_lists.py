import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Pillar 1 list
p1_old = '''                        <ul class="card-points">
                            <li>Grundschule, Mittel- und Oberstufe</li>
                            <li>Tüm yaygın okul derslerinde özel destek</li>
                            <li>Birebir ve odaklanmış küçük gruplar</li>
                            <li>BuT devlet yardımı ile tamamen ücretsiz</li>
                        </ul>'''
p1_new = '''                        <ul class="card-points">
                            <li data-i18n="pillar1.li1">Grundschule, Mittel- und Oberstufe</li>
                            <li data-i18n="pillar1.li2">Tüm yaygın okul derslerinde özel destek</li>
                            <li data-i18n="pillar1.li3">Birebir ve odaklanmış küçük gruplar</li>
                            <li data-i18n="pillar1.li4">BuT devlet yardımı ile tamamen ücretsiz</li>
                        </ul>'''
html = html.replace(p1_old, p1_new)

# Replace Pillar 2 list
p2_old = '''                        <ul class="card-points">
                            <li>Almanya'da Lisans ve Yüksek Lisans</li>
                            <li>Ausbildung (Mesleki Eğitim) yerleşimi</li>
                            <li>Akademik uygunluk ve vize dosyası</li>
                            <li>Kişisel dosya rehberliği & danışmanlık</li>
                        </ul>'''
p2_new = '''                        <ul class="card-points">
                            <li data-i18n="pillar2.li1">Almanya'da Lisans ve Yüksek Lisans</li>
                            <li data-i18n="pillar2.li2">Ausbildung (Mesleki Eğitim) yerleşimi</li>
                            <li data-i18n="pillar2.li3">Akademik uygunluk ve vize dosyası</li>
                            <li data-i18n="pillar2.li4">Kişisel dosya rehberliği & danışmanlık</li>
                        </ul>'''
html = html.replace(p2_old, p2_new)

# Replace Pillar 3 list
p3_old = '''                        <ul class="card-points">
                            <li>Online Deutschkurse (A1 - C1)</li>
                            <li>Online Englischkurse (A1 - C1)</li>
                            <li>Nitelikli eğitim kadrosuyla canlı ders</li>
                            <li>Türkiye'den esnek saatli katılım modeli</li>
                        </ul>'''
p3_new = '''                        <ul class="card-points">
                            <li data-i18n="pillar3.li1">Online Deutschkurse (A1 - C1)</li>
                            <li data-i18n="pillar3.li2">Online Englischkurse (A1 - C1)</li>
                            <li data-i18n="pillar3.li3">Nitelikli eğitim kadrosuyla canlı ders</li>
                            <li data-i18n="pillar3.li4">Türkiye'den esnek saatli katılım modeli</li>
                        </ul>'''
html = html.replace(p3_old, p3_new)

html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=35', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update lang.js
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    lang = f.read()

# TR Additions
tr_add = '''        "pillar1.btn": "Ders Desteği Başvurusu",
        "pillar1.li1": "İlkokul, Ortaokul ve Lise",
        "pillar1.li2": "Tüm okul derslerinde özel destek",
        "pillar1.li3": "Birebir ve odaklanmış küçük gruplar",
        "pillar1.li4": "BuT yardımı ile tamamen ücretsiz",
        "pillar2.title": "Almanya için <em>Kabul Danışmanlığı</em>",
        "pillar2.tag": "ADAY ODAKLI / TÜRKÇE",
        "pillar2.btn": "Kabul Danışmanlığını Keşfet",
        "pillar2.li1": "Almanya'da Lisans ve Yüksek Lisans",
        "pillar2.li2": "Ausbildung (Mesleki Eğitim) yerleşimi",
        "pillar2.li3": "Akademik uygunluk ve vize dosyası",
        "pillar2.li4": "Kişisel dosya rehberliği & danışmanlık",
        "pillar3.title": "Online <em>Dil Kursları</em>",
        "pillar3.tag": "TÜRKÇE AĞIRLIKLI / CANLI",
        "pillar3.btn": "Dil Kursuna Kaydol",
        "pillar3.li1": "Online Almanca Kursları (A1 - C1)",
        "pillar3.li2": "Online İngilizce Kursları (A1 - C1)",
        "pillar3.li3": "Nitelikli eğitim kadrosuyla canlı ders",
        "pillar3.li4": "Türkiye'den esnek saatli katılım modeli",'''

lang = re.sub(r'"pillar1\.btn":\s*"Ders Desteği Başvurusu",\s*"pillar2\.title":\s*"Bildungsberatung <em>für Deutschland</em>",\s*"pillar2\.tag":\s*"ADAY ODAKLI / TÜRKÇE",\s*"pillar2\.btn":\s*"Kabul Danışmanlığını Keşfet",\s*"pillar3\.title":\s*"Online <em>Sprachkurse</em>",\s*"pillar3\.tag":\s*"TÜRKÇE AĞIRLIKLI / CANLI",\s*"pillar3\.btn":\s*"Dil Kursuna Kaydol",', tr_add, lang)

# In case the regex above failed because the original text was different:
tr_old = '''        "pillar1.btn": "Ders Desteği Başvurusu",
        "pillar2.title": "Bildungsberatung <em>für Deutschland</em>",
        "pillar2.tag": "ADAY ODAKLI / TÜRKÇE",
        "pillar2.btn": "Kabul Danışmanlığını Keşfet",
        "pillar3.title": "Online <em>Sprachkurse</em>",
        "pillar3.tag": "TÜRKÇE AĞIRLIKLI / CANLI",
        "pillar3.btn": "Dil Kursuna Kaydol",'''
lang = lang.replace(tr_old, tr_add)


# EN Additions
en_add = '''        "pillar1.btn": "Apply for Tutoring",
        "pillar1.li1": "Primary, Middle, and High School",
        "pillar1.li2": "Tutoring in all common school subjects",
        "pillar1.li3": "One-on-one and focused small groups",
        "pillar1.li4": "Completely free with BuT state subsidy",
        "pillar2.title": "Admission Consulting <em>for Germany</em>",
        "pillar2.tag": "CANDIDATE ORIENTED",
        "pillar2.btn": "Explore Consulting",
        "pillar2.li1": "Bachelor's and Master's in Germany",
        "pillar2.li2": "Ausbildung (Vocational) placement",
        "pillar2.li3": "Academic eligibility and visa file",
        "pillar2.li4": "Personal file guidance & consulting",
        "pillar3.title": "Online <em>Language Courses</em>",
        "pillar3.tag": "TURKISH ORIENTED / LIVE",
        "pillar3.btn": "Enroll in Course",
        "pillar3.li1": "Online German Courses (A1 - C1)",
        "pillar3.li2": "Online English Courses (A1 - C1)",
        "pillar3.li3": "Live classes with qualified teaching staff",
        "pillar3.li4": "Flexible attendance model from Turkey",'''

en_old = '''        "pillar1.btn": "Apply for Tutoring",
        "pillar2.title": "Admission Consulting <em>for Germany</em>",
        "pillar2.tag": "CANDIDATE ORIENTED",
        "pillar2.btn": "Explore Consulting",
        "pillar3.title": "Online <em>Language Courses</em>",
        "pillar3.tag": "TURKISH ORIENTED / LIVE",
        "pillar3.btn": "Enroll in Course",'''
lang = lang.replace(en_old, en_add)

# DE Additions
de_add = '''        "pillar1.btn": "Nachhilfe Beantragen",
        "pillar1.li1": "Grundschule, Mittel- und Oberstufe",
        "pillar1.li2": "Nachhilfe in allen gängigen Schulfächern",
        "pillar1.li3": "Einzelunterricht und fokussierte Kleingruppen",
        "pillar1.li4": "Komplett kostenlos mit BuT-Förderung",
        "pillar2.title": "Bildungsberatung <em>für Deutschland</em>",
        "pillar2.tag": "KANDIDATENORIENTIERT",
        "pillar2.btn": "Beratung Entdecken",
        "pillar2.li1": "Bachelor und Master in Deutschland",
        "pillar2.li2": "Ausbildungsplatzvermittlung",
        "pillar2.li3": "Akademische Eignung und Visumakte",
        "pillar2.li4": "Persönliche Aktenführung & Beratung",
        "pillar3.title": "Online <em>Sprachkurse</em>",
        "pillar3.tag": "TÜRKISCH ORIENTIERT / LIVE",
        "pillar3.btn": "Zum Sprachkurs Anmelden",
        "pillar3.li1": "Online Deutschkurse (A1 - C1)",
        "pillar3.li2": "Online Englischkurse (A1 - C1)",
        "pillar3.li3": "Live-Unterricht mit qualifiziertem Lehrpersonal",
        "pillar3.li4": "Flexibles Teilnahmemodell aus der Türkei",'''

de_old = '''        "pillar1.btn": "Nachhilfe Beantragen",
        "pillar2.title": "Bildungsberatung <em>für Deutschland</em>",
        "pillar2.tag": "KANDIDATENORIENTIERT",
        "pillar2.btn": "Beratung Entdecken",
        "pillar3.title": "Online <em>Sprachkurse</em>",
        "pillar3.tag": "TÜRKISCH ORIENTIERT / LIVE",
        "pillar3.btn": "Zum Sprachkurs Anmelden",'''
lang = lang.replace(de_old, de_add)

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(lang)


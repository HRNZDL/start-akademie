# -*- coding: utf-8 -*-
import os, re

DIR = r"c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie"
INDEX = os.path.join(DIR, "index.html")
LANG_JS = os.path.join(DIR, "assets", "lang.js")

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

applied = []

def patch(old, new):
    global html
    if old in html:
        html = html.replace(old, new, 1)
        applied.append(old[:40])
    # silently skip if not found

# Services section header
patch('<span class="section-tag">Odak Alanlarımız</span>',
      '<span class="section-tag" data-i18n="idx.srv.section.tag">Odak Alanlarımız</span>')
patch('<h2>Eğitim ve Kariyer Hizmetlerimiz</h2>',
      '<h2 data-i18n="idx.srv.section.title">Eğitim ve Kariyer Hizmetlerimiz</h2>')

# Card 1: Üniversite
patch('<h3>Üniversite</h3>',
      '<h3 data-i18n="idx.srv.uni.title">Üniversite</h3>')
patch('Lisans, yüksek lisans, Studienkolleg ve üniversite başvurularında kişiye özel yol haritası.',
      '<span data-i18n="idx.srv.uni.desc">Lisans, yüksek lisans, Studienkolleg ve üniversite başvurularında kişiye özel yol haritası.</span>')
patch('> Lisans & Yüksek lisans</li>',
      '><span data-i18n="idx.srv.uni.li1"> Lisans & Yüksek lisans</span></li>')
patch('> Studienkolleg</li>',
      '><span data-i18n="idx.srv.uni.li2"> Studienkolleg</span></li>')
patch('> Üniversite ve bölüm seçimi</li>',
      '><span data-i18n="idx.srv.uni.li3"> Üniversite ve bölüm seçimi</span></li>')
patch('> uni-assist ve doğrudan başvurular</li>',
      '><span data-i18n="idx.srv.uni.li4"> uni-assist ve doğrudan başvurular</span></li>')
patch('>Üniversite Danışmanlığını İnceleyin</a>',
      ' data-i18n="idx.srv.uni.btn">Üniversite Danışmanlığını İnceleyin</a>')

# Card 2: Dil Kursları
patch('<h3>Dil Kursları</h3>',
      '<h3 data-i18n="idx.srv.dil.title">Dil Kursları</h3>')
patch("Almanya'daki üniversite dil kursları, DSH hazırlık programları ve özel dil okullarına başvuru desteği.",
      '<span data-i18n="idx.srv.dil.desc">Almanya\'daki üniversite dil kursları, DSH hazırlık programları ve özel dil okullarına başvuru desteği.</span>')
patch('> Üniversiteye bağlı dil kursları</li>',
      '><span data-i18n="idx.srv.dil.li1"> Üniversiteye bağlı dil kursları</span></li>')
patch('> DSH / studienvorbereitender Deutschkurs</li>',
      '><span data-i18n="idx.srv.dil.li2"> DSH / studienvorbereitender Deutschkurs</span></li>')
patch('> Özel dil okulları</li>',
      '><span data-i18n="idx.srv.dil.li3"> Özel dil okulları</span></li>')
patch('> Kurs seçimi ve başvuru</li>',
      '><span data-i18n="idx.srv.dil.li4"> Kurs seçimi ve başvuru</span></li>')
patch('>Dil Kurslarını İnceleyin</a>',
      ' data-i18n="idx.srv.dil.btn">Dil Kurslarını İnceleyin</a>')

# Card 3: Ausbildung
patch('Meslek seçimi, Almanca başvuru dosyası, işletme ve okul başvuruları için danışmanlık.',
      '<span data-i18n="idx.srv.aus.desc">Meslek seçimi, Almanca başvuru dosyası, işletme ve okul başvuruları için danışmanlık.</span>')
patch('> Uygunluk değerlendirmesi</li>',
      '><span data-i18n="idx.srv.aus.li1"> Uygunluk değerlendirmesi</span></li>')
patch('> Meslek alanı seçimi</li>',
      '><span data-i18n="idx.srv.aus.li2"> Meslek alanı seçimi</span></li>')
patch('> Lebenslauf ve Anschreiben</li>',
      '><span data-i18n="idx.srv.aus.li3"> Lebenslauf ve Anschreiben</span></li>')
patch('> İşletme ve okul başvuruları</li>',
      '><span data-i18n="idx.srv.aus.li4"> İşletme ve okul başvuruları</span></li>')
patch('>Ausbildung Sürecini İnceleyin</a>',
      ' data-i18n="idx.srv.aus.btn">Ausbildung Sürecini İnceleyin</a>')

# Card 4: Denklik
patch('<h3>Denklik</h3>',
      '<h3 data-i18n="idx.srv.dnk.title">Denklik</h3>')
patch("Okul, akademik ve mesleki diplomaların Almanya'daki değerlendirme ve tanınma süreçleri.",
      '<span data-i18n="idx.srv.dnk.desc">Okul, akademik ve mesleki diplomaların Almanya\'daki değerlendirme ve tanınma süreçleri.</span>')
patch('> Lise ve Açık Lise</li>',
      '><span data-i18n="idx.srv.dnk.li1"> Lise ve Açık Lise</span></li>')
patch('> Ön lisans & Meslek diploması</li>',
      '><span data-i18n="idx.srv.dnk.li2"> Ön lisans & Meslek diploması</span></li>')
patch('> Öğretmenlik</li>',
      '><span data-i18n="idx.srv.dnk.li3"> Öğretmenlik</span></li>')
patch('> Sağlık meslekleri</li>',
      '><span data-i18n="idx.srv.dnk.li4"> Sağlık meslekleri</span></li>')
patch('>Denklik Hizmetlerini İnceleyin</a>',
      ' data-i18n="idx.srv.dnk.btn">Denklik Hizmetlerini İnceleyin</a>')

# Card 5: Değişim
patch('<h3>Değişim ve Yaz Programları</h3>',
      '<h3 data-i18n="idx.srv.dgm.title">Değişim ve Yaz Programları</h3>')
patch('Erasmus, staj ve üniversite öğrencilerine yönelik kısa süreli Almanya programları.',
      '<span data-i18n="idx.srv.dgm.desc">Erasmus, staj ve üniversite öğrencilerine yönelik kısa süreli Almanya programları.</span>')
patch('> Erasmus öğrenim</li>',
      '><span data-i18n="idx.srv.dgm.li1"> Erasmus öğrenim</span></li>')
patch('> Erasmus staj</li>',
      '><span data-i18n="idx.srv.dgm.li2"> Erasmus staj</span></li>')
patch("> Almanya'da staj</li>",
      '><span data-i18n="idx.srv.dgm.li3"> Almanya\'da staj</span></li>')
patch('> Yaz dönemi çalışma</li>',
      '><span data-i18n="idx.srv.dgm.li4"> Yaz dönemi çalışma</span></li>')
patch('>Programları İnceleyin</a>',
      ' data-i18n="idx.srv.dgm.btn">Programları İnceleyin</a>')

# Card 6: Konaklama
patch('<h3 style="margin-bottom: 0;">Konaklama</h3>',
      '<h3 style="margin-bottom: 0;" data-i18n="idx.srv.kon.title">Konaklama</h3>')
patch("Öğrenciler için konaklama araştırması ve Almanya'ya varış sonrası ilk yerleşim desteği.",
      '<span data-i18n="idx.srv.kon.desc">Öğrenciler için konaklama araştırması ve Almanya\'ya varış sonrası ilk yerleşim desteği.</span>')
patch('> Öğrenci konaklaması</li>',
      '><span data-i18n="idx.srv.kon.li1"> Öğrenci konaklaması</span></li>')
patch('> Rhein-Main bölgesi</li>',
      '><span data-i18n="idx.srv.kon.li2"> Rhein-Main bölgesi</span></li>')
patch('> Ön talep</li>',
      '><span data-i18n="idx.srv.kon.li3"> Ön talep</span></li>')
patch('> Varış ve ilk yerleşim</li>',
      '><span data-i18n="idx.srv.kon.li4"> Varış ve ilk yerleşim</span></li>')
patch('>Konaklama Hizmetini İnceleyin</a>',
      ' data-i18n="idx.srv.kon.btn">Konaklama Hizmetini İnceleyin</a>')

with open(INDEX, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"index.html: {len(applied)} patches applied")

# inject extra lang.js keys
EXTRA = {
    "idx.srv.section.tag":   {"en": "Our Focus Areas",                     "de": "Unsere Schwerpunktbereiche"},
    "idx.srv.section.title": {"en": "Education and Career Services",       "de": "Bildungs- und Karrieredienste"},
    "idx.srv.dnk.desc":      {"en": "Assessment and recognition of school, academic and vocational diplomas in Germany.", "de": "Bewertung und Anerkennung von schulischen, akademischen und beruflichen Diplomen in Deutschland."},
    "idx.srv.aus.desc":      {"en": "Consulting for profession selection, German application file, company and school applications.", "de": "Beratung bei der Berufswahl, deutschen Bewerbungsmappe sowie Unternehmens- und Schulbewerbungen."},
    "idx.srv.dgm.desc":      {"en": "Erasmus, internship and short-term Germany programmes for university students.", "de": "Erasmus, Praktikum und kurzfristige Deutschland-Programme für Universitätsstudierende."},
    "idx.srv.kon.desc":      {"en": "Accommodation research for students and first settlement support after arrival in Germany.", "de": "Unterkunftsrecherche für Studierende und Unterstützung bei der ersten Eingewöhnung nach der Ankunft in Deutschland."},
    "idx.srv.dnk.li1":       {"en": "High School and Open School",         "de": "Gymnasium und Abendschule"},
    "idx.srv.dnk.li2":       {"en": "Associate Degree & Vocational Diploma", "de": "Fachhochschulabschluss & Berufsabschluss"},
    "idx.srv.dnk.li3":       {"en": "Teaching profession",                 "de": "Lehramt"},
    "idx.srv.dnk.li4":       {"en": "Healthcare professions",              "de": "Gesundheitsberufe"},
    "idx.srv.aus.li3":       {"en": "Lebenslauf and Anschreiben",          "de": "Lebenslauf und Anschreiben"},
    "idx.srv.aus.li4":       {"en": "Company and school applications",     "de": "Unternehmens- und Schulbewerbungen"},
    "idx.srv.dgm.li4":       {"en": "Summer work",                        "de": "Sommerarbeit"},
    "idx.srv.kon.li1":       {"en": "Student accommodation",              "de": "Studentenunterkunft"},
    "idx.srv.kon.li2":       {"en": "Rhein-Main region",                  "de": "Rhein-Main-Gebiet"},
    "idx.srv.kon.li3":       {"en": "Preliminary request",                "de": "Voranfrage"},
    "idx.srv.kon.li4":       {"en": "Arrival & first settlement",         "de": "Ankunft & erste Eingewöhnung"},
    "idx.srv.uni.li1":       {"en": "Bachelor & Master",                  "de": "Bachelor & Master"},
    "idx.srv.uni.li2":       {"en": "Studienkolleg",                      "de": "Studienkolleg"},
    "idx.srv.uni.li3":       {"en": "University and department selection", "de": "Universitäts- und Fachauswahl"},
    "idx.srv.uni.li4":       {"en": "uni-assist and direct applications",  "de": "uni-assist und Direktbewerbungen"},
    "idx.srv.dil.li1":       {"en": "University-affiliated language courses", "de": "Universitätseigene Sprachkurse"},
    "idx.srv.dil.li2":       {"en": "DSH / studienvorbereitender Deutschkurs", "de": "DSH / Studienvorbereitender Deutschkurs"},
    "idx.srv.dil.li3":       {"en": "Private language schools",           "de": "Private Sprachschulen"},
    "idx.srv.dil.li4":       {"en": "Course selection and application",   "de": "Kursauswahl und Bewerbung"},
    "idx.srv.aus.li1":       {"en": "Suitability assessment",             "de": "Eignungsbewertung"},
    "idx.srv.aus.li2":       {"en": "Profession sector selection",        "de": "Berufsbranchenwahl"},
    "idx.srv.dgm.li1":       {"en": "Erasmus study",                     "de": "Erasmus-Studium"},
    "idx.srv.dgm.li2":       {"en": "Erasmus internship",                "de": "Erasmus-Praktikum"},
    "idx.srv.dgm.li3":       {"en": "Internship in Germany",             "de": "Praktikum in Deutschland"},
}

with open(LANG_JS, 'r', encoding='utf-8') as f:
    js = f.read()

en_lines = ""
de_lines = ""
for key, vals in EXTRA.items():
    en_v = vals["en"].replace('"', '\\"')
    de_v = vals["de"].replace('"', '\\"')
    en_lines += f'        "{key}": "{en_v}",\n'
    de_lines += f'        "{key}": "{de_v}",\n'

en_pos = js.find('"en": {')
if en_pos != -1:
    insert_at = js.find('\n', en_pos) + 1
    js = js[:insert_at] + en_lines + js[insert_at:]

de_pos = js.find('"de": {')
if de_pos != -1:
    insert_at = js.find('\n', de_pos) + 1
    js = js[:insert_at] + de_lines + js[insert_at:]

with open(LANG_JS, 'w', encoding='utf-8') as f:
    f.write(js)

print(f"lang.js: {len(EXTRA)} extra service card keys added")

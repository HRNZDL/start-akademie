import sys
sys.stdout.reconfigure(encoding='utf-8')
# -*- coding: utf-8 -*-
"""
Patches index.html service cards and other hard-coded sections with data-i18n attributes.
"""
import os

DIR = r"c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie"
INDEX = os.path.join(DIR, "index.html")

PATCHES = [
    # ── Services section header ──────────────────────────────────────
    ('<span class="section-tag">Odak Alanlarımız</span>',
     '<span class="section-tag" data-i18n="idx.srv.section.tag">Odak Alanlarımız</span>'),
    ('<h2>Eğitim ve Kariyer Hizmetlerimiz</h2>',
     '<h2 data-i18n="idx.srv.section.title">Eğitim ve Kariyer Hizmetlerimiz</h2>'),

    # ── Card 1: Üniversite ───────────────────────────────────────────
    ('<h3>Üniversite</h3>',
     '<h3 data-i18n="idx.srv.uni.title">Üniversite</h3>'),
    ('<p style="color: var(--text-muted); margin-bottom: 16px;">Lisans, yüksek lisans, Studienkolleg ve üniversite başvurularında kişiye özel yol haritası.</p>',
     '<p style="color: var(--text-muted); margin-bottom: 16px;" data-i18n="idx.srv.uni.desc">Lisans, yüksek lisans, Studienkolleg ve üniversite başvurularında kişiye özel yol haritası.</p>'),
    ('</i> Lisans &amp; Yüksek lisans</li>',
     '</i><span data-i18n="idx.srv.uni.li1"> Lisans &amp; Yüksek lisans</span></li>'),
    ('</i> Studienkolleg</li>',
     '</i><span data-i18n="idx.srv.uni.li2"> Studienkolleg</span></li>'),
    ('</i> Üniversite ve bölüm seçimi</li>',
     '</i><span data-i18n="idx.srv.uni.li3"> Üniversite ve bölüm seçimi</span></li>'),
    ('</i> uni-assist ve doğrudan başvurular</li>',
     '</i><span data-i18n="idx.srv.uni.li4"> uni-assist ve doğrudan başvurular</span></li>'),
    ('>Üniversite Danışmanlığını İnceleyin</a>',
     ' data-i18n="idx.srv.uni.btn">Üniversite Danışmanlığını İnceleyin</a>'),

    # ── Card 2: Dil Kursları ─────────────────────────────────────────
    ('<h3>Dil Kursları</h3>',
     '<h3 data-i18n="idx.srv.dil.title">Dil Kursları</h3>'),
    ('<p style="color: var(--text-muted); margin-bottom: 16px;">Almanya\'daki üniversite dil kursları, DSH hazırlık programları ve özel dil okullarına başvuru desteği.</p>',
     '<p style="color: var(--text-muted); margin-bottom: 16px;" data-i18n="idx.srv.dil.desc">Almanya\'daki üniversite dil kursları, DSH hazırlık programları ve özel dil okullarına başvuru desteği.</p>'),
    ('</i> Üniversiteye bağlı dil kursları</li>',
     '</i><span data-i18n="idx.srv.dil.li1"> Üniversiteye bağlı dil kursları</span></li>'),
    ('</i> DSH / studienvorbereitender Deutschkurs</li>',
     '</i><span data-i18n="idx.srv.dil.li2"> DSH / studienvorbereitender Deutschkurs</span></li>'),
    ('</i> Özel dil okulları</li>',
     '</i><span data-i18n="idx.srv.dil.li3"> Özel dil okulları</span></li>'),
    ('</i> Kurs seçimi ve başvuru</li>',
     '</i><span data-i18n="idx.srv.dil.li4"> Kurs seçimi ve başvuru</span></li>'),
    ('>Dil Kurslarını İnceleyin</a>',
     ' data-i18n="idx.srv.dil.btn">Dil Kurslarını İnceleyin</a>'),

    # ── Card 3: Ausbildung ───────────────────────────────────────────
    ('<p style="color: var(--text-muted); margin-bottom: 16px;">Meslek seçimi, Almanca başvuru dosyası, işletme ve okul başvuruları için danışmanlık.</p>',
     '<p style="color: var(--text-muted); margin-bottom: 16px;" data-i18n="idx.srv.aus.desc">Meslek seçimi, Almanca başvuru dosyası, işletme ve okul başvuruları için danışmanlık.</p>'),
    ('</i> Uygunluk değerlendirmesi</li>',
     '</i><span data-i18n="idx.srv.aus.li1"> Uygunluk değerlendirmesi</span></li>'),
    ('</i> Meslek alanı seçimi</li>',
     '</i><span data-i18n="idx.srv.aus.li2"> Meslek alanı seçimi</span></li>'),
    ('</i> Lebenslauf ve Anschreiben</li>',
     '</i><span data-i18n="idx.srv.aus.li3"> Lebenslauf ve Anschreiben</span></li>'),
    ('</i> İşletme ve okul başvuruları</li>',
     '</i><span data-i18n="idx.srv.aus.li4"> İşletme ve okul başvuruları</span></li>'),
    ('>Ausbildung Sürecini İnceleyin</a>',
     ' data-i18n="idx.srv.aus.btn">Ausbildung Sürecini İnceleyin</a>'),

    # ── Card 4: Denklik ──────────────────────────────────────────────
    ('<h3>Denklik</h3>',
     '<h3 data-i18n="idx.srv.dnk.title">Denklik</h3>'),
    ('<p style="color: var(--text-muted); margin-bottom: 16px;">Okul, akademik ve mesleki diplomaların Almanya\'daki değerlendirme ve tanınma süreçleri.</p>',
     '<p style="color: var(--text-muted); margin-bottom: 16px;" data-i18n="idx.srv.dnk.desc">Okul, akademik ve mesleki diplomaların Almanya\'daki değerlendirme ve tanınma süreçleri.</p>'),
    ('</i> Lise ve Açık Lise</li>',
     '</i><span data-i18n="idx.srv.dnk.li1"> Lise ve Açık Lise</span></li>'),
    ('</i> Ön lisans &amp; Meslek diploması</li>',
     '</i><span data-i18n="idx.srv.dnk.li2"> Ön lisans &amp; Meslek diploması</span></li>'),
    ('</i> Öğretmenlik</li>',
     '</i><span data-i18n="idx.srv.dnk.li3"> Öğretmenlik</span></li>'),
    ('</i> Sağlık meslekleri</li>',
     '</i><span data-i18n="idx.srv.dnk.li4"> Sağlık meslekleri</span></li>'),
    ('>Denklik Hizmetlerini İnceleyin</a>',
     ' data-i18n="idx.srv.dnk.btn">Denklik Hizmetlerini İnceleyin</a>'),

    # ── Card 5: Değişim ──────────────────────────────────────────────
    ('<h3>Değişim ve Yaz Programları</h3>',
     '<h3 data-i18n="idx.srv.dgm.title">Değişim ve Yaz Programları</h3>'),
    ('<p style="color: var(--text-muted); margin-bottom: 16px;">Erasmus, staj ve üniversite öğrencilerine yönelik kısa süreli Almanya programları.</p>',
     '<p style="color: var(--text-muted); margin-bottom: 16px;" data-i18n="idx.srv.dgm.desc">Erasmus, staj ve üniversite öğrencilerine yönelik kısa süreli Almanya programları.</p>'),
    ('</i> Erasmus öğrenim</li>',
     '</i><span data-i18n="idx.srv.dgm.li1"> Erasmus öğrenim</span></li>'),
    ('</i> Erasmus staj</li>',
     '</i><span data-i18n="idx.srv.dgm.li2"> Erasmus staj</span></li>'),
    ('</i> Almanya\'da staj</li>',
     '</i><span data-i18n="idx.srv.dgm.li3"> Almanya\'da staj</span></li>'),
    ('</i> Yaz dönemi çalışma</li>',
     '</i><span data-i18n="idx.srv.dgm.li4"> Yaz dönemi çalışma</span></li>'),
    ('>Programları İnceleyin</a>',
     ' data-i18n="idx.srv.dgm.btn">Programları İnceleyin</a>'),

    # ── Card 6: Konaklama ────────────────────────────────────────────
    ('<h3 style="margin-bottom: 0;">Konaklama</h3>',
     '<h3 style="margin-bottom: 0;" data-i18n="idx.srv.kon.title">Konaklama</h3>'),
    ('<p style="color: var(--text-muted); margin-bottom: 16px; margin-top: 16px;">Öğrenciler için konaklama araştırması ve Almanya\'ya varış sonrası ilk yerleşim desteği.</p>',
     '<p style="color: var(--text-muted); margin-bottom: 16px; margin-top: 16px;" data-i18n="idx.srv.kon.desc">Öğrenciler için konaklama araştırması ve Almanya\'ya varış sonrası ilk yerleşim desteği.</p>'),
    ('</i> Öğrenci konaklaması</li>',
     '</i><span data-i18n="idx.srv.kon.li1"> Öğrenci konaklaması</span></li>'),
    ('</i> Rhein-Main bölgesi</li>',
     '</i><span data-i18n="idx.srv.kon.li2"> Rhein-Main bölgesi</span></li>'),
    ('</i> Ön talep</li>',
     '</i><span data-i18n="idx.srv.kon.li3"> Ön talep</span></li>'),
    ('</i> Varış ve ilk yerleşim</li>',
     '</i><span data-i18n="idx.srv.kon.li4"> Varış ve ilk yerleşim</span></li>'),
    ('>Konaklama Hizmetini İnceleyin</a>',
     ' data-i18n="idx.srv.kon.btn">Konaklama Hizmetini İnceleyin</a>'),
]

# Also add missing idx.srv.* keys to lang.js
EXTRA_TRANSLATIONS = {
    "idx.srv.section.tag":   {"en": "Our Focus Areas",               "de": "Unsere Schwerpunktbereiche"},
    "idx.srv.section.title": {"en": "Education and Career Services", "de": "Bildungs- und Karrieredienste"},
    "idx.srv.dnk.li1":  {"en": "High School and Open School",               "de": "Gymnasium und Abendschule"},
    "idx.srv.dnk.li2":  {"en": "Associate Degree & Vocational Diploma",     "de": "Fachhochschulabschluss & Berufsabschluss"},
    "idx.srv.dnk.li3":  {"en": "Teaching profession",                       "de": "Lehramt"},
    "idx.srv.dnk.li4":  {"en": "Healthcare professions",                    "de": "Gesundheitsberufe"},
    "idx.srv.aus.li3":  {"en": "Lebenslauf and Anschreiben",                "de": "Lebenslauf und Anschreiben"},
    "idx.srv.aus.li4":  {"en": "Company and school applications",           "de": "Unternehmens- und Schulbewerbungen"},
    "idx.srv.dgm.li4":  {"en": "Summer work",                              "de": "Sommerarbeit"},
    "idx.srv.kon.li1":  {"en": "Student accommodation",                    "de": "Studentenunterkunft"},
    "idx.srv.kon.li2":  {"en": "Rhein-Main region",                        "de": "Rhein-Main-Gebiet"},
    "idx.srv.kon.li3":  {"en": "Preliminary request",                      "de": "Voranfrage"},
    "idx.srv.kon.li4":  {"en": "Arrival & first settlement",               "de": "Ankunft & erste Eingewöhnung"},
}

LANG_JS = os.path.join(DIR, "assets", "lang.js")

def main():
    with open(INDEX, 'r', encoding='utf-8') as f:
        html = f.read()

    applied = 0
    for search, replace in PATCHES:
        if search in html:
            html = html.replace(search, replace, 1)
            applied += 1
        else:
            print(f"  NOT FOUND: {search[:60]}...")

    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"index.html: {applied}/{len(PATCHES)} patches applied")

    # inject extra lang.js keys
    with open(LANG_JS, 'r', encoding='utf-8') as f:
        js = f.read()

    en_lines = ""
    de_lines = ""
    for key, vals in EXTRA_TRANSLATIONS.items():
        en_lines += f'        "{key}": "{vals["en"].replace(chr(34), chr(92)+chr(34))}",\n'
        de_lines += f'        "{key}": "{vals["de"].replace(chr(34), chr(92)+chr(34))}",\n'

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
    print(f"lang.js: {len(EXTRA_TRANSLATIONS)} extra keys added")

if __name__ == "__main__":
    main()

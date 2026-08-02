# -*- coding: utf-8 -*-
import re

html_content = open('index.html', 'r', encoding='utf-8').read()

pillars_html = '''
    <!-- ══════════════════════════════════════════
         THE 3 PILLARS (HİZMET KANATLARI)
         ══════════════════════════════════════════ -->
    <section class="section-padding" id="pillars">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 64px;">
                <span class="section-tag" data-i18n="pillars.tag">Start Programları</span>
                <h2 data-i18n="pillars.title">Geleceğe Ulaşan Üç Eğitim Kanadı</h2>
                <p style="margin-top: 16px; font-size: 1.05rem;" data-i18n="pillars.desc">Almanya yerelindeki okul desteklerinden, üniversite kabul ve hazırlık kurslarına kadar hedefinize özel kurumsal eğitim çözümlerimiz.</p>
            </div>
            
            <div class="bento-grid">
                <!-- Pillar 1: Nachhilfe -->
                <div class="bento-card">
                    <div>
                        <div class="bento-icon" style="background: rgba(43, 112, 250, 0.1); color: var(--primary);">
                            <i data-lucide="book-open"></i>
                        </div>
                        <h3 data-i18n="pillar1.title" style="margin-bottom: 16px; font-size: 1.5rem;">Nachhilfe</h3>
                        <p data-i18n="pillar1.desc" style="color: var(--text-muted); line-height: 1.6; margin-bottom: 24px;">Okul öğrencileri için bireysel ders, Lernförderung, ödev desteği ve akademik takip.</p>
                    </div>
                    <a href="https://www.startakademie.de" target="_blank" class="btn btn-outline" style="width: 100%; text-align: center;" data-i18n="pillar1.btn">Nachhilfe Sitesine Git</a>
                </div>

                <!-- Pillar 2: Eğitim ve Kariyer -->
                <div class="bento-card" style="background: linear-gradient(145deg, var(--primary), var(--secondary)); border-color: transparent;">
                    <div style="color: white;">
                        <div class="bento-icon" style="background: rgba(255, 255, 255, 0.2); color: white;">
                            <i data-lucide="graduation-cap"></i>
                        </div>
                        <h3 data-i18n="pillar2.title" style="margin-bottom: 16px; font-size: 1.5rem;">Eğitim ve Kariyer</h3>
                        <p data-i18n="pillar2.desc" style="color: rgba(255, 255, 255, 0.9); line-height: 1.6; margin-bottom: 24px;">Üniversite, dil kursları, Ausbildung, denklik, değişim programları, konaklama ve Almanya’daki ilk adımlar.</p>
                    </div>
                    <a href="#services" class="btn btn-light" style="width: 100%; text-align: center;" data-i18n="pillar2.btn">Hizmetlerimizi İnceleyin</a>
                </div>

                <!-- Pillar 3: Online Dil Kursları -->
                <div class="bento-card">
                    <div>
                        <div class="bento-icon" style="background: rgba(30, 209, 161, 0.1); color: var(--accent);">
                            <i data-lucide="monitor-play"></i>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
                            <h3 data-i18n="pillar3.title" style="margin-bottom: 0; font-size: 1.5rem;">Online Dil Kursları</h3>
                            <span style="background: rgba(255, 171, 0, 0.1); color: #ffab00; padding: 4px 12px; border-radius: 12px; font-size: 0.8rem; font-weight: 600;" data-i18n="pillar3.tag">Ön talep alınıyor</span>
                        </div>
                        <p data-i18n="pillar3.desc" style="color: var(--text-muted); line-height: 1.6; margin-bottom: 24px;">Canlı online Almanca kursları ve seviye bazlı grup eğitimleri.</p>
                    </div>
                    <a href="https://www.startakademie.online" target="_blank" class="btn btn-outline" style="width: 100%; text-align: center;" data-i18n="pillar3.btn">Online Kurs Sitesine Git</a>
                </div>
            </div>
        </div>
    </section>
'''

target_str = '<!-- ══════════════════════════════════════════\n         PARTNER VE SEÇKİN ÜNİVERSİTELER'
if 'id="pillars"' not in html_content:
    html_content = html_content.replace(target_str, pillars_html + '\n    ' + target_str)
    open('index.html', 'w', encoding='utf-8').write(html_content)

lang = open('assets/lang.js', 'r', encoding='utf-8').read()

# TR
lang = re.sub(r'"pillar1\.title":.*?"pillar3\.btn":.*?"', r'''"pillar1.title": "Nachhilfe",
        "pillar1.desc": "Okul öğrencileri için bireysel ders, Lernförderung, ödev desteği ve akademik takip.",
        "pillar1.btn": "Nachhilfe Sitesine Git",
        "pillar2.title": "Eğitim ve Kariyer",
        "pillar2.desc": "Üniversite, dil kursları, Ausbildung, denklik, değişim programları, konaklama ve Almanya'daki ilk adımlar.",
        "pillar2.btn": "Hizmetlerimizi İnceleyin",
        "pillar3.title": "Online Dil Kursları",
        "pillar3.tag": "Ön talep alınıyor",
        "pillar3.desc": "Canlı online Almanca kursları ve seviye bazlı grup eğitimleri.",
        "pillar3.btn": "Online Kurs Sitesine Git"''', lang, count=1, flags=re.DOTALL)

# EN
lang = re.sub(r'"pillar1\.title":.*?"pillar3\.btn":.*?"', r'''"pillar1.title": "Nachhilfe",
        "pillar1.desc": "Private lessons, Lernförderung, homework support, and academic tracking for school students.",
        "pillar1.btn": "Visit Nachhilfe Site",
        "pillar2.title": "Education and Career",
        "pillar2.desc": "University, language courses, Ausbildung, equivalence, exchange programs, accommodation, and first steps in Germany.",
        "pillar2.btn": "Explore Our Services",
        "pillar3.title": "Online Language Courses",
        "pillar3.tag": "Pre-registration open",
        "pillar3.desc": "Live online German courses and level-based group training.",
        "pillar3.btn": "Visit Online Course Site"''', lang, count=1, flags=re.DOTALL)

# DE
lang = re.sub(r'"pillar1\.title":.*?"pillar3\.btn":.*?"', r'''"pillar1.title": "Nachhilfe",
        "pillar1.desc": "Einzelunterricht, Lernförderung, Hausaufgabenbetreuung und akademische Begleitung für Schüler.",
        "pillar1.btn": "Nachhilfe-Seite Besuchen",
        "pillar2.title": "Bildung und Karriere",
        "pillar2.desc": "Universität, Sprachkurse, Ausbildung, Anerkennung, Austauschprogramme, Unterkunft und die ersten Schritte in Deutschland.",
        "pillar2.btn": "Unsere Dienstleistungen Entdecken",
        "pillar3.title": "Online-Sprachkurse",
        "pillar3.tag": "Vorabanmeldungen möglich",
        "pillar3.desc": "Live-Online-Deutschkurse und niveaubezogenes Gruppentraining.",
        "pillar3.btn": "Online-Kurs-Seite Besuchen"''', lang, count=1, flags=re.DOTALL)

open('assets/lang.js', 'w', encoding='utf-8').write(lang)

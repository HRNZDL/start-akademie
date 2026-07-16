import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    # Nachhilfe Section
    '<span class="section-tag">Individuelle Förderung</span>': '<span class="section-tag" data-i18n="nachhilfe.tag">Individuelle Förderung</span>',
    '<h2>Nachhilfe in Rüsselsheim</h2>': '<h2 data-i18n="nachhilfe.title">Nachhilfe in Rüsselsheim</h2>',
    '<p style="margin-top: 16px; font-size: 1.05rem;">Wir unterstützen Ihr Kind flexibel, persönlich und zielorientiert – für bessere Noten, mehr Sicherheit und mehr Motivation im Schulalltag.</p>': '<p style="margin-top: 16px; font-size: 1.05rem;" data-i18n="nachhilfe.desc">Wir unterstützen Ihr Kind flexibel, persönlich und zielorientiert – für bessere Noten, mehr Sicherheit und mehr Motivation im Schulalltag.</p>',
    '<h3 style="margin-bottom: 24px; font-size: 1.4rem;">Fächer für die Klassen 1–13</h3>': '<h3 style="margin-bottom: 24px; font-size: 1.4rem;" data-i18n="nachhilfe.subjects.title">Fächer für die Klassen 1–13</h3>',
    '<h4 style="font-size: 1rem; margin-bottom: 12px; color: var(--gold);">1. Hauptfächer</h4>': '<h4 style="font-size: 1rem; margin-bottom: 12px; color: var(--gold);" data-i18n="nachhilfe.subjects.group1">1. Hauptfächer</h4>',
    '<h4 style="font-size: 1rem; margin-bottom: 12px; color: var(--gold);">2. Naturwissenschaften</h4>': '<h4 style="font-size: 1rem; margin-bottom: 12px; color: var(--gold);" data-i18n="nachhilfe.subjects.group2">2. Naturwissenschaften</h4>',
    '<h4 style="font-size: 1rem; margin-bottom: 12px; color: var(--gold);">3. Weitere Fächer & Schulformen</h4>': '<h4 style="font-size: 1rem; margin-bottom: 12px; color: var(--gold);" data-i18n="nachhilfe.subjects.group3">3. Weitere Fächer & Schulformen</h4>',
    '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">Geschichte, Französisch, Spanisch, Latein, DaF.<br><strong>Von der Grundschule bis zur Oberstufe.</strong></p>': '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;" data-i18n="nachhilfe.subjects.group3_desc">Geschichte, Französisch, Spanisch, Latein, DaF.<br><strong>Von der Grundschule bis zur Oberstufe.</strong></p>',
    
    '<h3 style="margin-bottom: 24px; font-size: 1.4rem;">Unsere Unterrichtsmodelle</h3>': '<h3 style="margin-bottom: 24px; font-size: 1.4rem;" data-i18n="nachhilfe.models.title">Unsere Unterrichtsmodelle</h3>',
    '<li><strong>Einzelunterricht & Kleingruppen:</strong> Individuelle Förderung ganz nach den Bedürfnissen Ihres Kindes.</li>': '<li data-i18n="nachhilfe.models.m1_desc"><strong data-i18n="nachhilfe.models.m1">Einzelunterricht & Kleingruppen:</strong> Individuelle Förderung ganz nach den Bedürfnissen Ihres Kindes.</li>',
    '<li><strong>Tandemunterricht:</strong> Zwei Schüler, ein Ziel. Gemeinsam lernen, zusammen weiterkommen.</li>': '<li data-i18n="nachhilfe.models.m2_desc"><strong data-i18n="nachhilfe.models.m2">Tandemunterricht:</strong> Zwei Schüler, ein Ziel. Gemeinsam lernen, zusammen weiterkommen.</li>',
    '<li><strong>Hausaufgabenbetreuung:</strong> Wir unterstützen bei Hausaufgaben und sorgen für mehr Sicherheit.</li>': '<li data-i18n="nachhilfe.models.m3_desc"><strong data-i18n="nachhilfe.models.m3">Hausaufgabenbetreuung:</strong> Wir unterstützen bei Hausaufgaben und sorgen für mehr Sicherheit.</li>',
    '<li><strong>Klausur- und Prüfungsvorbereitung:</strong> Gezielte Vorbereitung für Klassenarbeiten und Abschlüsse.</li>': '<li data-i18n="nachhilfe.models.m4_desc"><strong data-i18n="nachhilfe.models.m4">Klausur- und Prüfungsvorbereitung:</strong> Gezielte Vorbereitung für Klassenarbeiten und Abschlüsse.</li>',
    '<li><strong>Online-Unterricht:</strong> Flexibel lernen – auch von zu Hause aus, im Einzelunterricht.</li>': '<li data-i18n="nachhilfe.models.m5_desc"><strong data-i18n="nachhilfe.models.m5">Online-Unterricht:</strong> Flexibel lernen – auch von zu Hause aus, im Einzelunterricht.</li>',
    
    '<span class="section-tag" style="background: var(--gold); color: #000;">NEU</span>': '<span class="section-tag" style="background: var(--gold); color: #000;" data-i18n="flat.tag">NEU</span>',
    '<h3 style="font-size: 1.8rem; margin: 12px 0;">Hausaufgaben-Flat <span style="color: var(--gold);">150 € / Monat</span></h3>': '<h3 style="font-size: 1.8rem; margin: 12px 0;" data-i18n="flat.title">Hausaufgaben-Flat <span style="color: var(--gold);">150 € / Monat</span></h3>',
    '<p style="font-size: 1.05rem; margin-bottom: 16px;">Für Schülerinnen und Schüler der <strong>3.–8. Klasse</strong>. 4x pro Woche.</p>': '<p style="font-size: 1.05rem; margin-bottom: 16px;" data-i18n="flat.subtitle">Für Schülerinnen und Schüler der <strong>3.–8. Klasse</strong>. 4x pro Woche.</p>',
    '<li>Feste Zeiten & klare Struktur</li>': '<li data-i18n="flat.p1">Feste Zeiten & klare Struktur</li>',
    '<li>Kontrolle auf Richtigkeit & Vollständigkeit</li>': '<li data-i18n="flat.p2">Kontrolle auf Richtigkeit & Vollständigkeit</li>',
    '<li>Selbstständiges Arbeiten fördern</li>': '<li data-i18n="flat.p3">Selbstständiges Arbeiten fördern</li>',
    
    '<h4 style="font-size: 1rem; margin-bottom: 16px; color: var(--gold);">Ablauf der Betreuung:</h4>': '<h4 style="font-size: 1rem; margin-bottom: 16px; color: var(--gold);" data-i18n="flat.steps.title">Ablauf der Betreuung:</h4>',
    '<li><strong>Ankommen:</strong> Feste Zeiten zur Betreuung.</li>': '<li data-i18n="flat.step1"><strong>Ankommen:</strong> Feste Zeiten zur Betreuung.</li>',
    '<li><strong>Selbstständig arbeiten:</strong> Hausaufgaben ruhig erledigen.</li>': '<li data-i18n="flat.step2"><strong>Selbstständig arbeiten:</strong> Hausaufgaben ruhig erledigen.</li>',
    '<li><strong>Unterstützung:</strong> Lehrkräfte helfen bei Fragen.</li>': '<li data-i18n="flat.step3"><strong>Unterstützung:</strong> Lehrkräfte helfen bei Fragen.</li>',
    '<li><strong>Kontrolle:</strong> Prüfung auf Richtigkeit.</li>': '<li data-i18n="flat.step4"><strong>Kontrolle:</strong> Prüfung auf Richtigkeit.</li>',
    '<li><strong>Fertig?:</strong> Kind darf nach Hause gehen.</li>': '<li data-i18n="flat.step5"><strong>Fertig?:</strong> Kind darf nach Hause gehen.</li>',
    '<li><strong>Keine Hausaufgaben?:</strong> Sinnvoll lernen (Lesen, Übungsblätter).</li>': '<li data-i18n="flat.step6"><strong>Keine Hausaufgaben?:</strong> Sinnvoll lernen (Lesen, Übungsblätter).</li>',

    '<span class="section-tag" style="background: rgba(33, 150, 243, 0.1); color: var(--text);">Bildung und Teilhabe (BuT)</span>': '<span class="section-tag" style="background: rgba(33, 150, 243, 0.1); color: var(--text);" data-i18n="but.tag">Bildung und Teilhabe (BuT)</span>',
    '<h3 style="font-size: 1.8rem; margin-top: 12px;">Kostenlose Nachhilfe für Ihr Kind!</h3>': '<h3 style="font-size: 1.8rem; margin-top: 12px;" data-i18n="but.title">Kostenlose Nachhilfe für Ihr Kind!</h3>',
    '<p style="margin-top: 8px;">Wir helfen Ihnen beim BuT-Antrag und begleiten Ihr Kind auf dem Weg zum Lernerfolg.</p>': '<p style="margin-top: 8px;" data-i18n="but.desc">Wir helfen Ihnen beim BuT-Antrag und begleiten Ihr Kind auf dem Weg zum Lernerfolg.</p>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 16px; color: var(--gold);"><i data-lucide="users" style="width: 18px; height: 18px; display: inline-block; vertical-align: middle; margin-right: 8px;"></i> Wer kann BuT bekommen?</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 16px; color: var(--gold);"><i data-lucide="users" style="width: 18px; height: 18px; display: inline-block; vertical-align: middle; margin-right: 8px;"></i> <span data-i18n="but.who.title">Wer kann BuT bekommen?</span></h4>',
    '<li>Bürgergeld</li>': '<li data-i18n="but.who.p1">Bürgergeld</li>',
    '<li>Wohngeld</li>': '<li data-i18n="but.who.p2">Wohngeld</li>',
    '<li>Kinderzuschlag</li>': '<li data-i18n="but.who.p3">Kinderzuschlag</li>',
    '<li>Sozialhilfe / Asylbewerberleistungen</li>': '<li data-i18n="but.who.p4">Sozialhilfe / Asylbewerberleistungen</li>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 16px; color: var(--gold);"><i data-lucide="file-text" style="width: 18px; height: 18px; display: inline-block; vertical-align: middle; margin-right: 8px;"></i> So beantragen Sie BuT (6 Schritte)</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 16px; color: var(--gold);"><i data-lucide="file-text" style="width: 18px; height: 18px; display: inline-block; vertical-align: middle; margin-right: 8px;"></i> <span data-i18n="but.how.title">So beantragen Sie BuT (6 Schritte)</span></h4>',
    '<li>Formular bei uns anfragen oder abholen</li>': '<li data-i18n="but.how.s1">Formular bei uns anfragen oder abholen</li>',
    '<li>Antrag ausfüllen</li>': '<li data-i18n="but.how.s2">Antrag ausfüllen</li>',
    '<li>Schule ergänzt die Bestätigung</li>': '<li data-i18n="but.how.s3">Schule ergänzt die Bestätigung</li>',
    '<li>Unterlagen an die zuständige Stelle senden</li>': '<li data-i18n="but.how.s4">Unterlagen an die zuständige Stelle senden</li>',
    '<li>Bewilligung erhalten</li>': '<li data-i18n="but.how.s5">Bewilligung erhalten</li>',
    '<li>Mit dem Bescheid bei Start Akademie anmelden</li>': '<li data-i18n="but.how.s6">Mit dem Bescheid bei Start Akademie anmelden</li>',

    # Wizard Section
    '<span class="section-tag">Hızlı Denklik Testi</span>': '<span class="section-tag" data-i18n="wizard.tag">Hızlı Denklik Testi</span>',
    '<h2>Almanya Üniversite Uygunluk Sihirbazı</h2>': '<h2 data-i18n="wizard.title">Almanya Üniversite Uygunluk Sihirbazı</h2>',
    '<p style="margin-top: 12px; font-size: 0.95rem;">Lise mezuniyet bilginize göre doğrudan Almanya devlet üniversitesine kabul alıp alamayacağınızı 4 adımda hızlıca kontrol edin.</p>': '<p style="margin-top: 12px; font-size: 0.95rem;" data-i18n="wizard.desc">Lise mezuniyet bilginize göre doğrudan Almanya devlet üniversitesine kabul alıp alamayacağınızı 4 adımda hızlıca kontrol edin.</p>',
    '<h4 style="font-size: 1.2rem; text-align: center;">1. Mezun olduğunuz / olacağınız lise türü hangisidir?</h4>': '<h4 style="font-size: 1.2rem; text-align: center;" data-i18n="wizard.step1.q">1. Mezun olduğunuz / olacağınız lise türü hangisidir?</h4>',
    '<button class="wizard-btn-option" onclick="nextWizardStep(2, \'anadolu\')">Anadolu veya Fen Lisesi</button>': '<button class="wizard-btn-option" onclick="nextWizardStep(2, \'anadolu\')" data-i18n="wizard.step1.o1">Anadolu veya Fen Lisesi</button>',
    '<button class="wizard-btn-option" onclick="nextWizardStep(2, \'meslek\')">Meslek veya İmam Hatip Lisesi</button>': '<button class="wizard-btn-option" onclick="nextWizardStep(2, \'meslek\')" data-i18n="wizard.step1.o2">Meslek veya İmam Hatip Lisesi</button>',
    '<h4 style="font-size: 1.2rem; text-align: center;">2. Uluslararası bir diplomanız var mı? (IB, Abitur, AP vb.)</h4>': '<h4 style="font-size: 1.2rem; text-align: center;" data-i18n="wizard.step2.q">2. Uluslararası bir diplomanız var mı? (IB, Abitur, AP vb.)</h4>',
    '<button class="wizard-btn-option" onclick="nextWizardStep(3, \'yes\')">Evet (IB / Abitur / AP mevcut)</button>': '<button class="wizard-btn-option" onclick="nextWizardStep(3, \'yes\')" data-i18n="wizard.step2.o1">Evet (IB / Abitur / AP mevcut)</button>',
    '<button class="wizard-btn-option" onclick="nextWizardStep(3, \'no\')">Hayır (Sadece YKS / Lise Diploması)</button>': '<button class="wizard-btn-option" onclick="nextWizardStep(3, \'no\')" data-i18n="wizard.step2.o2">Hayır (Sadece YKS / Lise Diploması)</button>',
    '<h4 style="font-size: 1.2rem; text-align: center;">3. Güncel Almanca dil seviyeniz nedir?</h4>': '<h4 style="font-size: 1.2rem; text-align: center;" data-i18n="wizard.step3.q">3. Güncel Almanca dil seviyeniz nedir?</h4>',
    '<button class="wizard-btn-option" onclick="nextWizardStep(4, \'b1\')">B1 ve Üzeri</button>': '<button class="wizard-btn-option" onclick="nextWizardStep(4, \'b1\')" data-i18n="wizard.step3.o1">B1 ve Üzeri</button>',
    '<button class="wizard-btn-option" onclick="nextWizardStep(4, \'zero\')">Başlangıç Seviyesi / Hiç Yok</button>': '<button class="wizard-btn-option" onclick="nextWizardStep(4, \'zero\')" data-i18n="wizard.step3.o2">Başlangıç Seviyesi / Hiç Yok</button>',
    '<h4 style="font-size: 1.2rem; text-align: center;">4. YKS sınavına girdiniz mi ve bir üniversiteye yerleştiniz mi?</h4>': '<h4 style="font-size: 1.2rem; text-align: center;" data-i18n="wizard.step4.q">4. YKS sınavına girdiniz mi ve bir üniversiteye yerleştiniz mi?</h4>',
    '<button class="wizard-btn-option" onclick="showWizardResult(\'yes\')">Evet, 4 yıllık bölüme yerleştim</button>': '<button class="wizard-btn-option" onclick="showWizardResult(\'yes\')" data-i18n="wizard.step4.o1">Evet, 4 yıllık bölüme yerleştim</button>',
    '<button class="wizard-btn-option" onclick="showWizardResult(\'no\')">Hayır, henüz girmedim/yerleşmedim</button>': '<button class="wizard-btn-option" onclick="showWizardResult(\'no\')" data-i18n="wizard.step4.o2">Hayır, henüz girmedim/yerleşmedim</button>',
    '<div id="result-title" style="font-family: var(--font-serif); font-style: italic; font-size: 2.2rem; color: var(--gold); margin-bottom: 16px;">Değerlendiriliyor...</div>': '<div id="result-title" style="font-family: var(--font-display); font-weight: 700; font-size: 2.2rem; color: var(--gold); margin-bottom: 16px;" data-i18n="wizard.loading">Değerlendiriliyor...</div>',
    '<a href="#contact" class="btn btn-primary">Birebir Analiz Randevusu Alın</a>': '<a href="#contact" class="btn btn-primary" data-i18n="wizard.btn">Birebir Analiz Randevusu Alın</a>',

    # Camp Section
    '<span class="section-tag">Abitur & Oberstufe Boost</span>': '<span class="section-tag" data-i18n="camp.tag">Abitur & Oberstufe Boost</span>',
    '<h2>Sommercamps & Intensivkurse 2026</h2>': '<h2 data-i18n="camp.title">Sommercamps & Intensivkurse 2026</h2>',
    '<p style="margin-top: 16px; font-size: 1.05rem;">Bereiten Sie sich gezielt auf die Oberstufe oder das Abitur vor – entweder intensiv vor Ort in Rüsselsheim oder flexibel im Online-Einzelunterricht.</p>': '<p style="margin-top: 16px; font-size: 1.05rem;" data-i18n="camp.desc">Bereiten Sie sich gezielt auf die Oberstufe oder das Abitur vor – entweder intensiv vor Ort in Rüsselsheim oder flexibel im Online-Einzelunterricht.</p>',
    
    '<span class="section-tag" style="background: var(--gold); color: #000;">Intensivcamp vor Ort</span>': '<span class="section-tag" style="background: var(--gold); color: #000;" data-i18n="camp.inperson.tag">Intensivcamp vor Ort</span>',
    '<h3 style="font-size: 1.8rem; margin: 12px 0;">Stark in die 12. Klasse</h3>': '<h3 style="font-size: 1.8rem; margin: 12px 0;" data-i18n="camp.inperson.title">Stark in die 12. Klasse</h3>',
    '<p style="font-size: 1.05rem; margin-bottom: 24px;">Der Übergang in die 12. Klasse ist ein entscheidender Schritt. Mit unserem Intensivcamp bereiten wir Schülerinnen und Schüler gezielt auf die Anforderungen der Oberstufe vor.</p>': '<p style="font-size: 1.05rem; margin-bottom: 24px;" data-i18n="camp.inperson.desc">Der Übergang in die 12. Klasse ist ein entscheidender Schritt. Mit unserem Intensivcamp bereiten wir Schülerinnen und Schüler gezielt auf die Anforderungen der Oberstufe vor.</p>',
    '<span style="font-size: 0.95rem;">Mathematik Oberstufe</span>': '<span style="font-size: 0.95rem;" data-i18n="camp.inperson.f1">Mathematik Oberstufe</span>',
    '<span style="font-size: 0.95rem;">Deutsch: Analyse & Schreibtraining</span>': '<span style="font-size: 0.95rem;" data-i18n="camp.inperson.f2">Deutsch: Analyse & Schreibtraining</span>',
    '<span style="font-size: 0.95rem;">Englisch: Essay & Textanalyse</span>': '<span style="font-size: 0.95rem;" data-i18n="camp.inperson.f3">Englisch: Essay & Textanalyse</span>',
    '<span style="font-size: 0.95rem;">Klausurtraining & Lernstrategien</span>': '<span style="font-size: 0.95rem;" data-i18n="camp.inperson.f4">Klausurtraining & Lernstrategien</span>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 8px;">Camp-Termine 2026</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 8px;" data-i18n="camp.inperson.dates">Camp-Termine 2026</h4>',
    '<li><i data-lucide="calendar" style="width: 14px; height: 14px; margin-right: 8px; color: var(--gold);"></i> Samstag, 25.07.2026</li>': '<li><i data-lucide="calendar" style="width: 14px; height: 14px; margin-right: 8px; color: var(--gold);"></i> <span data-i18n="camp.inperson.d1">Samstag, 25.07.2026</span></li>',
    '<li><i data-lucide="calendar" style="width: 14px; height: 14px; margin-right: 8px; color: var(--gold);"></i> Samstag, 01.08.2026</li>': '<li><i data-lucide="calendar" style="width: 14px; height: 14px; margin-right: 8px; color: var(--gold);"></i> <span data-i18n="camp.inperson.d2">Samstag, 01.08.2026</span></li>',
    '<li><i data-lucide="calendar" style="width: 14px; height: 14px; margin-right: 8px; color: var(--gold);"></i> Samstag, 15.08.2026</li>': '<li><i data-lucide="calendar" style="width: 14px; height: 14px; margin-right: 8px; color: var(--gold);"></i> <span data-i18n="camp.inperson.d3">Samstag, 15.08.2026</span></li>',
    '<li><i data-lucide="calendar" style="width: 14px; height: 14px; margin-right: 8px; color: var(--gold);"></i> Samstag, 22.08.2026</li>': '<li><i data-lucide="calendar" style="width: 14px; height: 14px; margin-right: 8px; color: var(--gold);"></i> <span data-i18n="camp.inperson.d4">Samstag, 22.08.2026</span></li>',
    '<p><i data-lucide="clock" style="width: 14px; height: 14px; margin-right: 4px; vertical-align: text-bottom;"></i> 09:00 - 16:30 Uhr</p>': '<p><i data-lucide="clock" style="width: 14px; height: 14px; margin-right: 4px; vertical-align: text-bottom;"></i> <span data-i18n="camp.inperson.info1">09:00 - 16:30 Uhr</span></p>',
    '<p style="margin-top: 8px;"><i data-lucide="users" style="width: 14px; height: 14px; margin-right: 4px; vertical-align: text-bottom;"></i> 5 bis max. 8 Teilnehmende</p>': '<p style="margin-top: 8px;"><i data-lucide="users" style="width: 14px; height: 14px; margin-right: 4px; vertical-align: text-bottom;"></i> <span data-i18n="camp.inperson.info2">5 bis max. 8 Teilnehmende</span></p>',
    '<p style="margin-top: 8px;"><i data-lucide="map-pin" style="width: 14px; height: 14px; margin-right: 4px; vertical-align: text-bottom;"></i> Start Akademie - Rüsselsheim</p>': '<p style="margin-top: 8px;"><i data-lucide="map-pin" style="width: 14px; height: 14px; margin-right: 4px; vertical-align: text-bottom;"></i> <span data-i18n="camp.inperson.info3">Start Akademie - Rüsselsheim</span></p>',
    '<a href="#contact" class="btn btn-primary" style="width: 100%; margin-top: 24px; padding: 12px;">Jetzt Platz anfragen</a>': '<a href="#contact" class="btn btn-primary" style="width: 100%; margin-top: 24px; padding: 12px;" data-i18n="camp.inperson.btn">Jetzt Platz anfragen</a>',
    
    '<h3 style="font-size: 1.6rem;">Online Sommerkurse Englisch (1:1)</h3>': '<h3 style="font-size: 1.6rem;" data-i18n="camp.online.title">Online Sommerkurse Englisch (1:1)</h3>',
    '<p style="font-size: 1rem; color: var(--text-muted); margin-top: 8px;">4 Wochen (06.07. – 31.07.2026) | Montag bis Freitag, 90 Min. täglich | 20 Unterrichtseinheiten</p>': '<p style="font-size: 1rem; color: var(--text-muted); margin-top: 8px;" data-i18n="camp.online.desc">4 Wochen (06.07. – 31.07.2026) | Montag bis Freitag, 90 Min. täglich | 20 Unterrichtseinheiten</p>',
    '<span class="section-tag" style="background: var(--surface);">11. Klasse</span>': '<span class="section-tag" style="background: var(--surface);" data-i18n="camp.class11.tag">11. Klasse</span>',
    '<h4 style="font-size: 1.2rem; margin: 16px 0;">Vorbereitung Oberstufe</h4>': '<h4 style="font-size: 1.2rem; margin: 16px 0;" data-i18n="camp.class11.title">Vorbereitung Oberstufe</h4>',
    '<li><strong>Grammar & Writing:</strong> Zeiten, Passiv, Reported Speech, Essays.</li>': '<li data-i18n="camp.class11.p1"><strong>Grammar & Writing:</strong> Zeiten, Passiv, Essays.</li>',
    '<li><strong>Textanalyse & Literatur:</strong> Kurzgeschichten, Romane interpretieren.</li>': '<li data-i18n="camp.class11.p2"><strong>Textanalyse & Literatur:</strong> Kurzgeschichten interpretieren.</li>',
    '<li><strong>Kultur & Medien:</strong> UK/USA Politik kritisch verstehen.</li>': '<li data-i18n="camp.class11.p3"><strong>Kultur & Medien:</strong> UK/USA Politik verstehen.</li>',
    '<li><strong>Argumentation:</strong> Standpunkte begründen.</li>': '<li data-i18n="camp.class11.p4"><strong>Argumentation:</strong> Standpunkte begründen.</li>',

    '<span class="section-tag" style="background: var(--surface);">12. Klasse</span>': '<span class="section-tag" style="background: var(--surface);" data-i18n="camp.class12.tag">12. Klasse</span>',
    '<h4 style="font-size: 1.2rem; margin: 16px 0;">Qualifikationsphase</h4>': '<h4 style="font-size: 1.2rem; margin: 16px 0;" data-i18n="camp.class12.title">Qualifikationsphase</h4>',
    '<li><strong>Textanalyse:</strong> Komplexe Texte, Shakespeare, Gedichte.</li>': '<li data-i18n="camp.class12.p1"><strong>Textanalyse:</strong> Komplexe Texte, Shakespeare.</li>',
    '<li><strong>Academic Writing:</strong> Comment, Discussion auf hohem Niveau.</li>': '<li data-i18n="camp.class12.p2"><strong>Academic Writing:</strong> Comment, Discussion.</li>',
    '<li><strong>Medien & Politik:</strong> Globale Themen kritisch bewerten.</li>': '<li data-i18n="camp.class12.p3"><strong>Medien & Politik:</strong> Globale Themen bewerten.</li>',
    '<li><strong>Mediation:</strong> Komplexe Inhalte souverän vermitteln.</li>': '<li data-i18n="camp.class12.p4"><strong>Mediation:</strong> Inhalte souverän vermitteln.</li>',

    '<span class="section-tag" style="background: rgba(212, 175, 100, 0.15); color: var(--gold);">13. Klasse</span>': '<span class="section-tag" style="background: rgba(212, 175, 100, 0.15); color: var(--gold);" data-i18n="camp.class13.tag">13. Klasse</span>',
    '<h4 style="font-size: 1.2rem; margin: 16px 0;">Finaler Abitur-Boost</h4>': '<h4 style="font-size: 1.2rem; margin: 16px 0;" data-i18n="camp.class13.title">Finaler Abitur-Boost</h4>',
    '<li><strong>Diskursanalyse:</strong> Rhetorische Analyse und Synthese.</li>': '<li data-i18n="camp.class13.p1"><strong>Diskursanalyse:</strong> Rhetorische Analyse.</li>',
    '<li><strong>Abitur Writing:</strong> Struktur und Präzision unter Prüfungsbedingungen.</li>': '<li data-i18n="camp.class13.p2"><strong>Abitur Writing:</strong> Struktur & Präzision.</li>',
    '<li><strong>Gesellschaft:</strong> Demokratie und Identität kritisch analysieren.</li>': '<li data-i18n="camp.class13.p3"><strong>Gesellschaft:</strong> Demokratie kritisch analysieren.</li>',
    '<li><strong>Argumentation:</strong> Gegenargumente differenziert integrieren.</li>': '<li data-i18n="camp.class13.p4"><strong>Argumentation:</strong> Gegenargumente integrieren.</li>',
    '<a href="#contact" class="btn btn-outline">Sommerkurs Buchen</a>': '<a href="#contact" class="btn btn-outline" data-i18n="camp.online.btn">Sommerkurs Buchen</a>',

    # Visa & FAQ Section
    '<span class="section-tag">Önemli Bilgilendirme</span>': '<span class="section-tag" data-i18n="visa.tag">Önemli Bilgilendirme</span>',
    '<h2>Öğrenci Vizesi ve Çalışma Hakkı</h2>': '<h2 data-i18n="visa.title">Öğrenci Vizesi ve Çalışma Hakkı</h2>',
    '<p style="margin-top: 16px; font-size: 1.05rem;">Almanya\'da eğitim planlayan öğrenciler için vize süreci, finansman ve resmi evrak hazırlığı büyük önem taşır.</p>': '<p style="margin-top: 16px; font-size: 1.05rem;" data-i18n="visa.desc">Almanya\'da eğitim planlayan öğrenciler için vize süreci, finansman ve resmi evrak hazırlığı büyük önem taşır.</p>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 8px;">1. Öğrenci Vizesi</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 8px;" data-i18n="visa.item1.title">1. Öğrenci Vizesi</h4>',
    '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">Genellikle kabul belgesi, pasaport, finansman kanıtı (Sperrkonto), sağlık sigortası ve akademik belgeler gerekir.</p>': '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;" data-i18n="visa.item1.desc">Genellikle kabul belgesi, pasaport, finansman kanıtı (Sperrkonto), sağlık sigortası ve akademik belgeler gerekir.</p>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 8px;">2. Çalışma Hakkı</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 8px;" data-i18n="visa.item2.title">2. Çalışma Hakkı</h4>',
    '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">Uluslararası öğrenciler Almanya\'da yılda <strong>140 tam gün</strong> veya <strong>280 yarım gün</strong> çalışma hakkına sahiptir.</p>': '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;" data-i18n="visa.item2.desc">Uluslararası öğrenciler Almanya\'da yılda <strong>140 tam gün</strong> oder <strong>280 yarım gün</strong> çalışma hakkına sahiptir.</p>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 8px;">3. Oturum Süreci</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 8px;" data-i18n="visa.item3.title">3. Oturum Süreci</h4>',
    '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">Eğitim amacıyla verilen oturum izni, öğrenim sürecine bağlı olarak uzatılabilir.</p>': '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;" data-i18n="visa.item3.desc">Eğitim amacıyla verilen oturum izni, öğrenim sürecine bağlı olarak uzatılabilir.</p>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 8px;">4. Mezuniyet Sonrası</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 8px;" data-i18n="visa.item4.title">4. Mezuniyet Sonrası</h4>',
    '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">Mezunlar, uygun koşullarda iş arama süresi ve sonrasında çalışma oturumuna geçiş imkânına sahip olabilir.</p>': '<p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;" data-i18n="visa.item4.desc">Mezunlar, uygun koşullarda iş arama süresi ve sonrasında çalışma oturumuna geçiş imkânına sahip olabilir.</p>',
    '<p style="font-size: 0.9rem; margin: 0;"><strong>Uyarı:</strong> Vize kararı yalnızca yetkili resmi makamlar tarafından verilir. Başvuru dosyasının eksiksiz hazırlanması bu süreçte büyük önem taşır.</p>': '<p style="font-size: 0.9rem; margin: 0;" data-i18n="visa.warning"><strong>Uyarı:</strong> Vize kararı yalnızca yetkili resmi makamlar tarafından verilir. Başvuru dosyasının eksiksiz hazırlanması bu süreçte büyük önem taşır.</p>',
    
    '<h2>Sık Sorulan Sorular</h2>': '<h2 data-i18n="faq.title">Sık Sorulan Sorular</h2>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);">1. Almanya\'da üniversite tamamen ücretsiz mi?</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);" data-i18n="faq.q1">1. Almanya\'da üniversite tamamen ücretsiz mi?</h4>',
    '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;">Birçok devlet üniversitesinde yüksek öğrenim harcı yoktur; ancak dönemlik katkı payı ve yaşam giderleri ayrıca planlanmalıdır.</p>': '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;" data-i18n="faq.a1">Birçok devlet üniversitesinde yüksek öğrenim harcı yoktur; ancak dönemlik katkı payı ve yaşam giderleri ayrıca planlanmalıdır.</p>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);">2. YKS olmadan başvuru yapılabilir mi?</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);" data-i18n="faq.q2">2. YKS olmadan başvuru yapılabilir mi?</h4>',
    '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;">Bu durum öğrencinin eğitim geçmişine göre değişir. Her dosya bireysel değerlendirilmelidir.</p>': '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;" data-i18n="faq.a2">Bu durum öğrencinin eğitim geçmişine göre değişir. Her dosya bireysel değerlendirilmelidir.</p>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);">3. Almanca bilmeden başvuru mümkün mü?</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);" data-i18n="faq.q3">3. Almanca bilmeden başvuru mümkün mü?</h4>',
    '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;">Bazı öğrenciler için dil kursu, şartlı kabul veya hazırlık seçenekleri değerlendirilebilir.</p>': '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;" data-i18n="faq.a3">Bazı öğrenciler için dil kursu, şartlı kabul veya hazırlık seçenekleri değerlendirilebilir.</p>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);">4. Öğrenciler Almanya\'da çalışabilir mi?</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);" data-i18n="faq.q4">4. Öğrenciler Almanya\'da çalışabilir mi?</h4>',
    '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;">Evet, resmi kurallar çerçevesinde yılda 140 tam gün veya 280 yarım gün çalışma hakkı bulunabilir.</p>': '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;" data-i18n="faq.a4">Evet, resmi kurallar çerçevesinde yılda 140 tam gün veya 280 yarım gün çalışma hakkı bulunabilir.</p>',
    '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);">5. Start Akademie kabul veya vize garantisi verir mi?</h4>': '<h4 style="font-size: 1.1rem; margin-bottom: 8px; color: var(--gold);" data-i18n="faq.q5">5. Start Akademie kabul veya vize garantisi verir mi?</h4>',
    '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;">Hayır. Nihai karar ilgili üniversite ve resmi makamlar tarafından verilir.</p>': '<p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;" data-i18n="faq.a5">Hayır. Nihai karar ilgili üniversite ve resmi makamlar tarafından verilir.</p>',
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully processed {len(replacements)} strings.")

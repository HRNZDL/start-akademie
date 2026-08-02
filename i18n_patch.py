# -*- coding: utf-8 -*-
"""
Adds data-i18n attributes to subpage HTML files and injects
high-quality EN/DE translations into lang.js.
No external API needed - translations are written directly.
"""
import os, re

DIR = r"c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie"
LANG_JS_PATH = os.path.join(DIR, "assets", "lang.js")

# ─────────────────────────────────────────────
# ALL TRANSLATIONS  (key: {en, de})
# ─────────────────────────────────────────────
TRANSLATIONS = {

    # ── uni.html ──────────────────────────────
    "uni.hero.badge":       {"en": "🎓 University Consulting", "de": "🎓 Universitätsberatung"},
    "uni.hero.title":       {"en": "University <em>Education</em> in Germany", "de": "Studium <em>in Deutschland</em>"},
    "uni.hero.subtitle":    {"en": "Step-by-step professional support from state university applications to student visa, language exams and enrolment.", "de": "Professionelle Unterstützung von der Bewerbung an staatlichen Universitäten bis zum Studentenvisum, Sprachprüfungen und Immatrikulation."},
    "uni.hero.btn":         {"en": "Free Initial Assessment →", "de": "Kostenlose Erstbewertung →"},
    "uni.overview.badge":   {"en": "Professional Support", "de": "Professionelle Unterstützung"},
    "uni.overview.title":   {"en": "Bachelor, Master and <em>Studienkolleg</em> Processes", "de": "Bachelor-, Master- und <em>Studienkolleg</em>-Verfahren"},
    "uni.overview.desc":    {"en": "The path to university in Germany is different for every student. The most suitable application strategy is determined according to your educational background and goals.", "de": "Der Weg zur Universität in Deutschland ist für jeden Studierenden anders. Die passende Bewerbungsstrategie wird anhand Ihrer schulischen Laufbahn und Ziele ermittelt."},
    "uni.card1.title":      {"en": "In Which Areas Do We Provide Support?", "de": "In welchen Bereichen unterstützen wir?"},
    "uni.card1.li1":        {"en": "Bachelor applications", "de": "Bachelor-Bewerbungen"},
    "uni.card1.li2":        {"en": "Master's applications", "de": "Master-Bewerbungen"},
    "uni.card1.li3":        {"en": "Studienkolleg guidance", "de": "Studienkolleg-Beratung"},
    "uni.card1.li4":        {"en": "Department and university selection", "de": "Fach- und Universitätsauswahl"},
    "uni.card1.li5":        {"en": "Conditional admission and language pathway assessment", "de": "Bedingte Zulassung und Sprachweg-Bewertung"},
    "uni.card2.title":      {"en": "Application Processes", "de": "Bewerbungsverfahren"},
    "uni.card2.li1":        {"en": "uni-assist and VPD procedures", "de": "uni-assist und VPD-Verfahren"},
    "uni.card2.li2":        {"en": "Direct university applications", "de": "Direkte Universitätsbewerbungen"},
    "uni.card2.li3":        {"en": "Document review and file organisation", "de": "Dokumentenprüfung und Aktenorganisation"},
    "uni.card2.li4":        {"en": "CV and motivation letter support", "de": "Lebenslauf- und Motivationsschreiben-Unterstützung"},
    "uni.card2.li5":        {"en": "Follow-up on missing document requests", "de": "Nachverfolgung fehlender Unterlagen"},
    "uni.card3.title":      {"en": "Who Is It Suitable For?", "de": "Für wen ist es geeignet?"},
    "uni.card3.li1":        {"en": "High school graduates", "de": "Gymnasialabsolventen"},
    "uni.card3.li2":        {"en": "Open school graduates", "de": "Absolventen offener Schulen"},
    "uni.card3.li3":        {"en": "University students", "de": "Universitätsstudierende"},
    "uni.card3.li4":        {"en": "Associate degree graduates", "de": "Absolventen mit Fachhochschulreife"},
    "uni.card3.li5":        {"en": "Bachelor's degree graduates", "de": "Bachelor-Absolventen"},
    "uni.badge1.title":     {"en": "Personalised Strategy", "de": "Maßgeschneiderte Strategie"},
    "uni.badge1.desc":      {"en": "Planning tailored to your goals", "de": "Planung nach Ihren Zielen"},
    "uni.badge2.title":     {"en": "Expert Consulting", "de": "Fachkundige Beratung"},
    "uni.badge2.desc":      {"en": "Up-to-date knowledge of the German education system", "de": "Aktuelles Wissen über das deutsche Bildungssystem"},
    "uni.badge3.title":     {"en": "Reliable Support", "de": "Zuverlässige Unterstützung"},
    "uni.badge3.desc":      {"en": "We are by your side from application to admission", "de": "Wir begleiten Sie von der Bewerbung bis zur Zulassung"},
    "uni.faq.title":        {"en": "Frequently Asked <em>Questions</em>", "de": "Häufig gestellte <em>Fragen</em>"},
    "uni.faq.q1":           {"en": "Is university in Germany free?", "de": "Ist das Studium in Deutschland kostenlos?"},
    "uni.faq.a1":           {"en": "Yes, there are no tuition fees at public universities. Only a semester contribution (Semesterbeitrag) is paid, usually between €250–400.", "de": "Ja, an staatlichen Universitäten werden keine Studiengebühren erhoben. Es wird nur ein Semesterbeitrag gezahlt, meist zwischen 250–400 €."},
    "uni.faq.q2":           {"en": "Is my YKS score sufficient?", "de": "Reicht mein YKS-Ergebnis aus?"},
    "uni.faq.a2":           {"en": "The YKS result meets the condition to validate a Turkish high school diploma in Germany; a specific score threshold is not required, just placement in a 4-year programme. Request a consultation for a detailed assessment.", "de": "Das YKS-Ergebnis erfüllt die Bedingung zur Anerkennung eines türkischen Schulabschlusses in Deutschland; eine bestimmte Punktzahl ist nicht erforderlich, nur eine Zulassung in einem 4-jährigen Programm. Beantragen Sie ein Beratungsgespräch für eine detaillierte Bewertung."},
    "uni.faq.q3":           {"en": "How long does it take to get an APS certificate?", "de": "Wie lange dauert es, ein APS-Zertifikat zu erhalten?"},
    "uni.faq.a3":           {"en": "APS Turkey office interview dates vary by demand. Generally 4–8 weeks from application to interview, plus 2–4 more weeks for results.", "de": "Die Interviewtermine des APS-Türkei-Büros variieren je nach Nachfrage. Im Allgemeinen 4–8 Wochen von der Bewerbung bis zum Interview, plus 2–4 weitere Wochen für die Ergebnisse."},
    "uni.faq.q4":           {"en": "Can I apply without knowing German?", "de": "Kann ich mich ohne Deutschkenntnisse bewerben?"},
    "uni.faq.a4":           {"en": "There are English-taught programmes (with IELTS/TOEFL). For German-taught programmes, a language course + conditional admission path can be followed.", "de": "Es gibt englischsprachige Studiengänge (mit IELTS/TOEFL). Für deutschsprachige Studiengänge kann ein Sprachkurs + bedingter Zulassungsweg eingeschlagen werden."},
    "uni.cta.title":        {"en": "Ready to Apply?", "de": "Bereit zur Bewerbung?"},
    "uni.cta.desc":         {"en": "Schedule a free initial meeting to plan your university application process in Germany.", "de": "Vereinbaren Sie ein kostenloses Erstgespräch, um Ihren Universitätsbewerbungsprozess in Deutschland zu planen."},
    "uni.cta.btn":          {"en": "Book Free Meeting →", "de": "Kostenloses Gespräch buchen →"},

    # ── dil.html ──────────────────────────────
    "dil.hero.badge":       {"en": "🗣️ Language Courses", "de": "🗣️ Sprachkurse"},
    "dil.hero.title":       {"en": "<em>Language Courses</em> in Germany", "de": "<em>Sprachkurse</em> in Deutschland"},
    "dil.hero.subtitle":    {"en": "We guide you to the right language course for your goals and handle the application process.", "de": "Wir leiten Sie zum richtigen Sprachkurs für Ihre Ziele und übernehmen den Anmeldeprozess."},
    "dil.hero.btn":         {"en": "Free Initial Meeting →", "de": "Kostenloses Erstgespräch →"},
    "dil.overview.badge":   {"en": "Language Course Types", "de": "Sprachkursarten"},
    "dil.overview.title":   {"en": "Which <em>Language Course</em> is Right for You?", "de": "Welcher <em>Sprachkurs</em> ist der Richtige für Sie?"},
    "dil.overview.desc":    {"en": "Language courses in Germany vary by purpose and target group. We find the most suitable option for your goals.", "de": "Sprachkurse in Deutschland variieren je nach Zweck und Zielgruppe. Wir finden die am besten geeignete Option für Ihre Ziele."},
    "dil.card1.title":      {"en": "University-Affiliated Language Courses", "de": "Universitätseigene Sprachkurse"},
    "dil.card1.li1":        {"en": "DSH preparation courses", "de": "DSH-Vorbereitungskurse"},
    "dil.card1.li2":        {"en": "TestDaF preparation", "de": "TestDaF-Vorbereitung"},
    "dil.card1.li3":        {"en": "studienvorbereitender Deutschkurs", "de": "Studienvorbereitender Deutschkurs"},
    "dil.card2.title":      {"en": "Private Language Schools", "de": "Private Sprachschulen"},
    "dil.card2.li1":        {"en": "Intensive German courses (A1–C1)", "de": "Intensiv-Deutschkurse (A1–C1)"},
    "dil.card2.li2":        {"en": "Evening and part-time courses", "de": "Abend- und Teilzeitkurse"},
    "dil.card2.li3":        {"en": "Online German courses", "de": "Online-Deutschkurse"},
    "dil.card3.title":      {"en": "Visa-Oriented Language Courses", "de": "Visumorientierte Sprachkurse"},
    "dil.card3.li1":        {"en": "Language courses that support visa applications", "de": "Sprachkurse zur Visumunterstützung"},
    "dil.card3.li2":        {"en": "Approved course certificates", "de": "Anerkannte Kurszertifikate"},
    "dil.card3.li3":        {"en": "Integration courses", "de": "Integrationskurse"},
    "dil.service.badge":    {"en": "Our Services", "de": "Unsere Dienstleistungen"},
    "dil.service.title":    {"en": "Language Course <em>Application Support</em>", "de": "Sprachkurs-<em>Anmeldeunterstützung</em>"},
    "dil.service.li1":      {"en": "Level and goal assessment", "de": "Niveau- und Zielbewertung"},
    "dil.service.li2":      {"en": "Suitable course research", "de": "Passende Kursrecherche"},
    "dil.service.li3":      {"en": "Application support", "de": "Bewerbungsunterstützung"},
    "dil.service.li4":      {"en": "Registration process follow-up", "de": "Begleitung des Anmeldeprozesses"},
    "dil.cta.title":        {"en": "Find the Right Language Course", "de": "Den richtigen Sprachkurs finden"},
    "dil.cta.desc":         {"en": "Tell us your language level and goals, and we will find the most suitable course for you.", "de": "Teilen Sie uns Ihr Sprachniveau und Ihre Ziele mit, und wir finden den am besten geeigneten Kurs für Sie."},
    "dil.cta.btn":          {"en": "Free Language Consultation →", "de": "Kostenlose Sprachberatung →"},

    # ── ausbildung.html ───────────────────────
    "aus.hero.badge":       {"en": "🔧 Ausbildung", "de": "🔧 Ausbildung"},
    "aus.hero.title":       {"en": "<em>Ausbildung</em> in Germany", "de": "<em>Ausbildung</em> in Deutschland"},
    "aus.hero.subtitle":    {"en": "We provide comprehensive support from choosing the right vocational training to the application process and visa.", "de": "Wir bieten umfassende Unterstützung von der Wahl der richtigen Berufsausbildung bis zum Bewerbungs- und Visumsprozess."},
    "aus.hero.btn":         {"en": "Free Initial Assessment →", "de": "Kostenlose Erstbewertung →"},
    "aus.overview.badge":   {"en": "Vocational Training", "de": "Berufsausbildung"},
    "aus.overview.title":   {"en": "What is <em>Ausbildung</em>?", "de": "Was ist eine <em>Ausbildung</em>?"},
    "aus.overview.desc":    {"en": "Ausbildung is a dual vocational training system in Germany. You work at a company and attend vocational school. Duration is typically 2–3.5 years.", "de": "Ausbildung ist ein duales Berufsausbildungssystem in Deutschland. Sie arbeiten in einem Unternehmen und besuchen die Berufsschule. Die Dauer beträgt in der Regel 2–3,5 Jahre."},
    "aus.card1.title":      {"en": "Our Support Areas", "de": "Unsere Unterstützungsbereiche"},
    "aus.card1.li1":        {"en": "Suitability analysis", "de": "Eignungsanalyse"},
    "aus.card1.li2":        {"en": "CV and application file", "de": "Lebenslauf und Bewerbungsmappe"},
    "aus.card1.li3":        {"en": "Company and school research", "de": "Unternehmens- und Schulrecherche"},
    "aus.card1.li4":        {"en": "Application submission", "de": "Einreichung der Bewerbung"},
    "aus.card1.li5":        {"en": "Interview preparation", "de": "Vorstellungsgesprächsvorbereitung"},
    "aus.card2.title":      {"en": "Visa Process", "de": "Visumsprozess"},
    "aus.card2.li1":        {"en": "Ausbildung visa application", "de": "Ausbildungsvisa-Antrag"},
    "aus.card2.li2":        {"en": "Document preparation", "de": "Dokumentenvorbereitung"},
    "aus.card2.li3":        {"en": "Consulate process follow-up", "de": "Konsulatsprozess-Nachverfolgung"},
    "aus.card2.li4":        {"en": "Blocked account guidance", "de": "Sperrkonto-Beratung"},
    "aus.card3.title":      {"en": "Who Is It Suitable For?", "de": "Für wen ist es geeignet?"},
    "aus.card3.li1":        {"en": "High school graduates (B1+ German)", "de": "Gymnasialabsolventen (B1+ Deutsch)"},
    "aus.card3.li2":        {"en": "Those who want to work in Germany", "de": "Personen, die in Deutschland arbeiten möchten"},
    "aus.card3.li3":        {"en": "Those who want to gain a profession quickly", "de": "Personen, die schnell einen Beruf erlernen möchten"},
    "aus.cta.title":        {"en": "Start Your Ausbildung Journey", "de": "Beginnen Sie Ihre Ausbildungsreise"},
    "aus.cta.desc":         {"en": "Book a free consultation to find the right Ausbildung programme and company for you.", "de": "Buchen Sie eine kostenlose Beratung, um das richtige Ausbildungsprogramm und Unternehmen für Sie zu finden."},
    "aus.cta.btn":          {"en": "Free Ausbildung Consultation →", "de": "Kostenlose Ausbildungsberatung →"},

    # ── denklik.html ──────────────────────────
    "dnk.hero.badge":       {"en": "📜 Degree Recognition", "de": "📜 Anerkennung"},
    "dnk.hero.title":       {"en": "Degree <em>Recognition</em> in Germany", "de": "Berufsanerkennung <em>in Deutschland</em>"},
    "dnk.hero.subtitle":    {"en": "We guide you through the equivalence recognition process for your academic or professional diploma in Germany.", "de": "Wir begleiten Sie durch das Anerkennungsverfahren Ihres akademischen oder beruflichen Abschlusses in Deutschland."},
    "dnk.hero.btn":         {"en": "Free Recognition Consultation →", "de": "Kostenlose Anerkennungsberatung →"},
    "dnk.overview.badge":   {"en": "Recognition Types", "de": "Anerkennungsarten"},
    "dnk.overview.title":   {"en": "Which <em>Recognition Process</em> Do You Need?", "de": "Welches <em>Anerkennungsverfahren</em> benötigen Sie?"},
    "dnk.overview.desc":    {"en": "Degree recognition in Germany varies according to the type of qualification. We identify the right path for you.", "de": "Die Anerkennung in Deutschland variiert je nach Art der Qualifikation. Wir ermitteln den richtigen Weg für Sie."},
    "dnk.card1.title":      {"en": "High School and Academic Diploma Procedures", "de": "Schulische und akademische Diplomverfahren"},
    "dnk.card1.badge":      {"en": "from €290", "de": "ab 290 €"},
    "dnk.card1.li1":        {"en": "Diploma and transcript equivalence check", "de": "Diplom- und Transkript-Äquivalenzprüfung"},
    "dnk.card1.li2":        {"en": "ZAB process guidance", "de": "ZAB-Verfahrensbegleitung"},
    "dnk.card1.li3":        {"en": "Preparation of missing documents", "de": "Vorbereitung fehlender Unterlagen"},
    "dnk.card1.li4":        {"en": "Statement of Comparability preparation", "de": "Vorbereitung der Vergleichbarkeitsaussage"},
    "dnk.card2.title":      {"en": "Professional Equivalence Procedures", "de": "Berufliche Anerkennungsverfahren"},
    "dnk.card2.badge":      {"en": "from €490", "de": "ab 490 €"},
    "dnk.card2.li1":        {"en": "Review of foreign vocational certificates", "de": "Prüfung ausländischer Berufsabschlüsse"},
    "dnk.card2.li2":        {"en": "Institution and authority matching", "de": "Institutions- und Behördenabgleich"},
    "dnk.card2.li3":        {"en": "Partial and full equivalence determination", "de": "Teil- und vollständige Äquivalenzbestimmung"},
    "dnk.card2.li4":        {"en": "Process follow-up and outcome evaluation", "de": "Prozessverfolgung und Ergebnisbewertung"},
    "dnk.card3.title":      {"en": "Profession-Specific Recognition Procedures", "de": "Berufsspezifische Anerkennungsverfahren"},
    "dnk.card3.badge":      {"en": "from €490", "de": "ab 490 €"},
    "dnk.card3.li1":        {"en": "Teaching, engineering, health, social services fields", "de": "Lehramt, Ingenieurwesen, Gesundheit, Soziales"},
    "dnk.card3.li2":        {"en": "State authority applications", "de": "Antragstellung bei Staatsbehörden"},
    "dnk.card3.li3":        {"en": "Expert review and evaluation", "de": "Fachgutachten und Bewertung"},
    "dnk.card3.li4":        {"en": "Complementary measure guidance", "de": "Beratung zu Ausgleichsmaßnahmen"},
    "dnk.cta.title":        {"en": "Start Your Recognition Process", "de": "Starten Sie Ihr Anerkennungsverfahren"},
    "dnk.cta.desc":         {"en": "Have your diploma recognised in Germany. Book your free consultation today.", "de": "Lassen Sie Ihr Diplom in Deutschland anerkennen. Buchen Sie noch heute Ihre kostenlose Beratung."},
    "dnk.cta.btn":          {"en": "Free Recognition Consultation →", "de": "Kostenlose Anerkennungsberatung →"},

    # ── degisim.html ──────────────────────────
    "dgm.hero.badge":       {"en": "☀️ Exchange & Summer Programmes", "de": "☀️ Austausch & Sommerprogramme"},
    "dgm.hero.title":       {"en": "Exchange & <em>Summer Programmes</em>", "de": "Austausch & <em>Sommerprogramme</em>"},
    "dgm.hero.subtitle":    {"en": "Experience Germany with Erasmus+, internship, summer school or work & travel programmes.", "de": "Erleben Sie Deutschland mit Erasmus+, Praktikum, Sommerschule oder Work & Travel-Programmen."},
    "dgm.hero.btn":         {"en": "Free Programme Consultation →", "de": "Kostenlose Programmberatung →"},
    "dgm.overview.badge":   {"en": "Programme Types", "de": "Programmarten"},
    "dgm.overview.title":   {"en": "Which <em>Programme</em> Suits You?", "de": "Welches <em>Programm</em> passt zu Ihnen?"},
    "dgm.overview.desc":    {"en": "Programmes that allow you to experience Germany vary by duration and purpose. We find the most suitable option for you.", "de": "Programme, die Ihnen Deutschland näherbringen, variieren nach Dauer und Zweck. Wir finden die passende Option für Sie."},
    "dgm.card1.title":      {"en": "Erasmus+ Study Exchange", "de": "Erasmus+ Studierenden-Austausch"},
    "dgm.card1.li1":        {"en": "Partner university matching", "de": "Partnerhochschulabgleich"},
    "dgm.card1.li2":        {"en": "Application and document preparation", "de": "Bewerbungs- und Dokumentenvorbereitung"},
    "dgm.card1.li3":        {"en": "Learning Agreement preparation", "de": "Learning Agreement-Vorbereitung"},
    "dgm.card1.li4":        {"en": "Accommodation support", "de": "Unterkunftsunterstützung"},
    "dgm.card2.title":      {"en": "Erasmus+ Internship Programme", "de": "Erasmus+ Praktikumsprogramm"},
    "dgm.card2.li1":        {"en": "Company research in Germany", "de": "Unternehmensrecherche in Deutschland"},
    "dgm.card2.li2":        {"en": "Internship application", "de": "Praktikumsbewerbung"},
    "dgm.card2.li3":        {"en": "Grant application support", "de": "Stipendienantrag-Unterstützung"},
    "dgm.card3.title":      {"en": "Internship in Germany", "de": "Praktikum in Deutschland"},
    "dgm.card3.li1":        {"en": "Paid internship research", "de": "Bezahlte Praktikumssuche"},
    "dgm.card3.li2":        {"en": "CV and cover letter tailored to Germany", "de": "Auf Deutschland zugeschnittener Lebenslauf und Anschreiben"},
    "dgm.card3.li3":        {"en": "Visa support", "de": "Visumunterstützung"},
    "dgm.card4.title":      {"en": "Summer School Programmes", "de": "Sommerschulprogramme"},
    "dgm.card4.li1":        {"en": "University summer schools", "de": "Universitäts-Sommerschulen"},
    "dgm.card4.li2":        {"en": "German language summer courses", "de": "Deutsche Sprach-Sommerkurse"},
    "dgm.card4.li3":        {"en": "Work & Travel options", "de": "Work & Travel-Optionen"},
    "dgm.cta.title":        {"en": "Explore Germany", "de": "Deutschland entdecken"},
    "dgm.cta.desc":         {"en": "Choose the programme that suits you and take your first step to Germany.", "de": "Wählen Sie das passende Programm und machen Sie Ihren ersten Schritt nach Deutschland."},
    "dgm.cta.btn":          {"en": "Free Programme Consultation →", "de": "Kostenlose Programmberatung →"},

    # ── konaklama.html ────────────────────────
    "kon.hero.title":       {"en": "Accommodation, Visa & <em>First Settlement</em>", "de": "Unterkunft, Visum & <em>Erste Eingewöhnung</em>"},
    "kon.hero.subtitle":    {"en": "We are by your side during your move to Germany and your first steps there.", "de": "Wir begleiten Sie bei Ihrem Umzug nach Deutschland und Ihren ersten Schritten dort."},
    "kon.overview.badge":   {"en": "Post-Arrival Services", "de": "Services nach der Ankunft"},
    "kon.overview.title":   {"en": "By Your Side at <em>Every Stage</em>", "de": "In <em>jeder Phase</em> an Ihrer Seite"},
    "kon.acc.title":        {"en": "Accommodation Support", "de": "Unterkunftsunterstützung"},
    "kon.acc.li1":          {"en": "Student dormitories", "de": "Studentenwohnheime"},
    "kon.acc.li2":          {"en": "WG (Shared flat)", "de": "WG (Wohngemeinschaft)"},
    "kon.acc.li3":          {"en": "Private flat rental", "de": "Private Wohnungsvermietung"},
    "kon.acc.li4":          {"en": "Temporary accommodation (Airbnb, hostel etc.)", "de": "Vorübergehende Unterkunft (Airbnb, Hostel usw.)"},
    "kon.visa.title":       {"en": "Visa Consulting", "de": "Visaberatung"},
    "kon.visa.li1":         {"en": "Motivation letter preparation", "de": "Motivationsschreiben-Vorbereitung"},
    "kon.visa.li2":         {"en": "Document checklist review", "de": "Dokumenten-Checkliste"},
    "kon.visa.li3":         {"en": "Blocked account and insurance procedures", "de": "Sperrkonto und Versicherungsverfahren"},
    "kon.visa.li4":         {"en": "Consulate process follow-up", "de": "Konsulatsprozess-Nachverfolgung"},
    "kon.settle.title":     {"en": "First Settlement & Adaptation (First Steps in Germany)", "de": "Erste Eingewöhnung & Anpassung (Erste Schritte in Deutschland)"},
    "kon.settle.li1":       {"en": "Residence registration (Anmeldung)", "de": "Wohnsitzanmeldung (Anmeldung)"},
    "kon.settle.li2":       {"en": "Opening a bank account", "de": "Eröffnung eines Bankkontos"},
    "kon.settle.li3":       {"en": "Health insurance activation", "de": "Krankenversicherungsaktivierung"},
    "kon.settle.li4":       {"en": "Phone line and transport card", "de": "Telefonvertrag und Fahrkarte"},
    "kon.note":             {"en": "Our consulting services cover not only your move to Germany but also ensuring you take your first steps there with confidence.", "de": "Unsere Beratungsleistungen umfassen nicht nur Ihren Umzug nach Deutschland, sondern auch die Sicherstellung, dass Sie Ihre ersten Schritte dort mit Vertrauen gehen."},
    "kon.cta.title":        {"en": "Get Accommodation & Visa Support", "de": "Unterkunfts- & Visaunterstützung erhalten"},
    "kon.cta.desc":         {"en": "Leave your preliminary request to plan where you will stay before going to Germany.", "de": "Hinterlassen Sie Ihre Voranfrage, um zu planen, wo Sie vor Ihrer Abreise nach Deutschland übernachten werden."},
    "kon.cta.btn":          {"en": "Leave Preliminary Request →", "de": "Voranfrage hinterlassen →"},

    # ── index.html service cards ───────────────
    "idx.srv.uni.title":    {"en": "University", "de": "Universität"},
    "idx.srv.uni.desc":     {"en": "Personalised guidance for bachelor, master applications and Studienkolleg processes.", "de": "Individuelle Beratung für Bachelor-, Master-Bewerbungen und Studienkolleg-Verfahren."},
    "idx.srv.uni.li1":      {"en": "Bachelor & Master", "de": "Bachelor & Master"},
    "idx.srv.uni.li2":      {"en": "Studienkolleg", "de": "Studienkolleg"},
    "idx.srv.uni.li3":      {"en": "University and department selection", "de": "Universitäts- und Fachauswahl"},
    "idx.srv.uni.li4":      {"en": "uni-assist and direct applications", "de": "uni-assist und Direktbewerbungen"},
    "idx.srv.uni.btn":      {"en": "Explore University Consulting", "de": "Universitätsberatung erkunden"},
    "idx.srv.dil.title":    {"en": "Language Courses", "de": "Sprachkurse"},
    "idx.srv.dil.desc":     {"en": "Application support for university-affiliated language courses, DSH preparation and private language schools.", "de": "Bewerbungsunterstützung für universitätseigene Sprachkurse, DSH-Vorbereitung und private Sprachschulen."},
    "idx.srv.dil.li1":      {"en": "University-affiliated language courses", "de": "Universitätseigene Sprachkurse"},
    "idx.srv.dil.li2":      {"en": "DSH / studienvorbereitender Deutschkurs", "de": "DSH / Studienvorbereitender Deutschkurs"},
    "idx.srv.dil.li3":      {"en": "Private language schools", "de": "Private Sprachschulen"},
    "idx.srv.dil.li4":      {"en": "Course selection and application", "de": "Kursauswahl und Bewerbung"},
    "idx.srv.dil.btn":      {"en": "Explore Language Courses", "de": "Sprachkurse erkunden"},
    "idx.srv.aus.desc":     {"en": "Comprehensive support for choosing a profession, finding a company, CV, interview and visa processes.", "de": "Umfassende Unterstützung bei der Berufswahl, Unternehmenssuche, Lebenslauf, Vorstellungsgespräch und Visumverfahren."},
    "idx.srv.aus.li1":      {"en": "Suitability assessment", "de": "Eignungsbewertung"},
    "idx.srv.aus.li2":      {"en": "Profession sector selection", "de": "Berufsbranchenwahl"},
    "idx.srv.aus.li3":      {"en": "CV and application preparation", "de": "Lebenslauf- und Bewerbungsvorbereitung"},
    "idx.srv.aus.li4":      {"en": "Company and school research", "de": "Unternehmens- und Schulrecherche"},
    "idx.srv.aus.btn":      {"en": "Explore Ausbildung", "de": "Ausbildung erkunden"},
    "idx.srv.dnk.title":    {"en": "Equivalence", "de": "Anerkennung"},
    "idx.srv.dnk.desc":     {"en": "Recognition of academic and professional qualifications with ZAB, ANABIN and official institutions.", "de": "Anerkennung akademischer und beruflicher Qualifikationen bei ZAB, ANABIN und offiziellen Institutionen."},
    "idx.srv.dnk.li1":      {"en": "High school diploma equivalence", "de": "Schulabschluss-Äquivalenz"},
    "idx.srv.dnk.li2":      {"en": "Academic degree recognition", "de": "Akademische Abschlussanerkennung"},
    "idx.srv.dnk.li3":      {"en": "Professional qualification recognition", "de": "Berufliche Qualifikationsanerkennung"},
    "idx.srv.dnk.btn":      {"en": "Explore Equivalence", "de": "Anerkennung erkunden"},
    "idx.srv.dgm.title":    {"en": "Exchange & Summer", "de": "Austausch & Sommer"},
    "idx.srv.dgm.desc":     {"en": "Erasmus+, internship, summer school and work & travel programme guidance.", "de": "Erasmus+, Praktikum, Sommerschule und Work & Travel-Programmberatung."},
    "idx.srv.dgm.li1":      {"en": "Erasmus+ learning mobility", "de": "Erasmus+ Lernmobilität"},
    "idx.srv.dgm.li2":      {"en": "Erasmus+ internship", "de": "Erasmus+ Praktikum"},
    "idx.srv.dgm.li3":      {"en": "Internship in Germany", "de": "Praktikum in Deutschland"},
    "idx.srv.dgm.li4":      {"en": "Summer school", "de": "Sommerschule"},
    "idx.srv.dgm.btn":      {"en": "Explore Exchange Programmes", "de": "Austauschprogramme erkunden"},
    "idx.srv.kon.title":    {"en": "Accommodation & Visa", "de": "Unterkunft & Visum"},
    "idx.srv.kon.desc":     {"en": "Dormitory, WG and private rental research; visa process and first settlement support.", "de": "Wohnheim-, WG- und Privatmietrecherche; Visumverfahren und Unterstützung bei der ersten Eingewöhnung."},
    "idx.srv.kon.li1":      {"en": "Student dormitories", "de": "Studentenwohnheime"},
    "idx.srv.kon.li2":      {"en": "WG and private rental", "de": "WG und Privatmiete"},
    "idx.srv.kon.li3":      {"en": "Visa consulting", "de": "Visaberatung"},
    "idx.srv.kon.li4":      {"en": "Anmeldung & first steps", "de": "Anmeldung & erste Schritte"},
    "idx.srv.kon.btn":      {"en": "Explore Accommodation", "de": "Unterkunft erkunden"},

    # ── index.html pricing section ─────────────
    "idx.pricing.p1.name":      {"en": "University Application Package", "de": "Universitätsbewerbungspaket"},
    "idx.pricing.p1.li1":       {"en": "Academic eligibility assessment", "de": "Akademische Eignungsbewertung"},
    "idx.pricing.p1.li2":       {"en": "University and programme research", "de": "Universitäts- und Programmrecherche"},
    "idx.pricing.p1.li3":       {"en": "Up to 3 applications", "de": "Bis zu 3 Bewerbungen"},
    "idx.pricing.p1.li4":       {"en": "Document review", "de": "Dokumentenprüfung"},
    "idx.pricing.p1.li5":       {"en": "CV and motivation letter review", "de": "Lebenslauf- und Motivationsschreiben-Überprüfung"},
    "idx.pricing.p1.li6":       {"en": "Direct application support via uni-assist / VPD", "de": "Direkte Bewerbungsunterstützung via uni-assist / VPD"},
    "idx.pricing.p1.btn":       {"en": "Get Information", "de": "Informationen erhalten"},
    "idx.pricing.p2.name":      {"en": "Application + Digital Visa Package", "de": "Bewerbung + Digitales Visapaket"},
    "idx.pricing.p2.li1":       {"en": "University Application Package scope", "de": "Universitätsbewerbungspaket-Umfang"},
    "idx.pricing.p2.li2":       {"en": "Up to 5 applications", "de": "Bis zu 5 Bewerbungen"},
    "idx.pricing.p2.li3":       {"en": "Digital visa document list", "de": "Digitale Visadokumentenliste"},
    "idx.pricing.p2.li4":       {"en": "Document review and organisation", "de": "Dokumentenprüfung und -organisation"},
    "idx.pricing.p2.li5":       {"en": "System upload support", "de": "Systemhochlade-Unterstützung"},
    "idx.pricing.p2.li6":       {"en": "Pre-appointment final check", "de": "Abschlusskontrolle vor dem Termin"},
    "idx.pricing.p2.btn":       {"en": "Get Information", "de": "Informationen erhalten"},
    "idx.pricing.p3.name":      {"en": "Full Process Package", "de": "Vollständiges Prozesspaket"},
    "idx.pricing.p3.li1":       {"en": "Application + digital visa scope", "de": "Bewerbungs- + Digitalvisa-Umfang"},
    "idx.pricing.p3.li2":       {"en": "Up to 7 applications", "de": "Bis zu 7 Bewerbungen"},
    "idx.pricing.p3.li3":       {"en": "Language and exam roadmap", "de": "Sprach- und Prüfungs-Roadmap"},
    "idx.pricing.p3.li4":       {"en": "Accommodation research support", "de": "Unterkunftsrecherche-Unterstützung"},
    "idx.pricing.p3.li5":       {"en": "Preparation for arrival in Germany", "de": "Vorbereitung für die Ankunft in Deutschland"},
    "idx.pricing.p3.li6":       {"en": "First settlement process support", "de": "Unterstützung beim ersten Eingewöhnungsprozess"},
    "idx.pricing.p3.btn":       {"en": "Get Information", "de": "Informationen erhalten"},
    "idx.pricing.note":         {"en": "* The exact scope of service is individually confirmed after the consultant has reviewed the student's file.", "de": "* Der genaue Leistungsumfang wird individuell bestätigt, nachdem der Berater die Akte des Studierenden geprüft hat."},
    "idx.addons.tag":           {"en": "Flexible Solutions", "de": "Flexible Lösungen"},
    "idx.addons.title":         {"en": "Individual and Additional Services", "de": "Einzel- und Zusatzleistungen"},
    "idx.addons.desc":          {"en": "We are by your side only for the steps you need. Flexible options for only the services you need.", "de": "Wir sind nur für die Schritte an Ihrer Seite, die Sie benötigen. Flexible Optionen für nur die Dienste, die Sie benötigen."},
    "idx.addons.s1.title":      {"en": "Single University or Programme Application", "de": "Einzel-Universitäts- oder Programmbewerbung"},
    "idx.addons.s1.li1":        {"en": "Review of application requirements", "de": "Überprüfung der Bewerbungsanforderungen"},
    "idx.addons.s1.li2":        {"en": "Document review", "de": "Dokumentenprüfung"},
    "idx.addons.s1.li3":        {"en": "University portal procedures", "de": "Universitätsportal-Verfahren"},
    "idx.addons.s1.li4":        {"en": "Submission of application", "de": "Einreichung der Bewerbung"},
    "idx.addons.s2.title":      {"en": "Digital Visa Application Support", "de": "Digitale Visumantragsunterstützung"},
    "idx.addons.s2.li1":        {"en": "Personalised document list", "de": "Personalisierte Dokumentenliste"},
    "idx.addons.s2.li2":        {"en": "Form review", "de": "Formularprüfung"},
    "idx.addons.s2.li3":        {"en": "Digital upload support", "de": "Digitale Hochlade-Unterstützung"},
    "idx.addons.s2.li4":        {"en": "Final verification check", "de": "Abschließende Verifizierungsprüfung"},
    "idx.addons.s3.title":      {"en": "Language Course Application Consulting", "de": "Sprachkurs-Bewerbungsberatung"},
    "idx.addons.s4.title":      {"en": "Ausbildung Application Consulting", "de": "Ausbildungsbewerbungsberatung"},
    "idx.addons.other.title":   {"en": "Other Services and Special Areas", "de": "Sonstige Dienstleistungen und spezielle Bereiche"},
    "idx.addons.o1.title":      {"en": "High School and Academic Diploma Procedures", "de": "Schulische und akademische Diplomverfahren"},
    "idx.addons.o1.desc":       {"en": "Diploma and transcript equivalence, ZAB processes", "de": "Diplom- und Transkript-Äquivalenz, ZAB-Verfahren"},
    "idx.addons.o2.title":      {"en": "Professional Equivalence Procedures", "de": "Berufliche Anerkennungsverfahren"},
    "idx.addons.o2.desc":       {"en": "Vocational school, journeyman / master craftsman certificates", "de": "Berufsschule, Gesellenbrief / Meisterbrief"},
    "idx.addons.o3.title":      {"en": "Profession-Specific Equivalence Procedures", "de": "Berufsspezifische Anerkennungsverfahren"},
    "idx.addons.o3.desc":       {"en": "Teaching, health, social services etc.", "de": "Lehramt, Gesundheit, Soziales usw."},
    "idx.addons.o4.title":      {"en": "Erasmus Consulting", "de": "Erasmus-Beratung"},
    "idx.addons.o4.desc":       {"en": "Erasmus study and internship applications", "de": "Erasmus-Studium und Praktikumsbewerbungen"},
    "idx.addons.o5.title":      {"en": "Internship and Summer Work", "de": "Praktikum und Sommerarbeit"},
    "idx.addons.o5.desc":       {"en": "Internship and summer programme support in Germany", "de": "Praktikum und Sommerprogramm-Unterstützung in Deutschland"},
    "idx.addons.o6.title":      {"en": "Accommodation Research Support", "de": "Unterkunftsrecherche-Unterstützung"},
    "idx.addons.o6.desc":       {"en": "Dormitory, WG or private rental research", "de": "Wohnheim-, WG- oder Privatmietrecherche"},
    "idx.addons.o7.title":      {"en": "Arrival in Germany & First Settlement", "de": "Ankunft in Deutschland & Erste Eingewöhnung"},
    "idx.addons.o7.desc":       {"en": "Anmeldung, bank account, insurance activation", "de": "Anmeldung, Bankkonto, Versicherungsaktivierung"},
    "idx.included.title":       {"en": "What's Included in Fees", "de": "Im Preis inbegriffen"},
    "idx.included.desc":        {"en": "Start Akademie consulting services for the listed services", "de": "Start Akademie Beratungsdienstleistungen für die aufgeführten Leistungen"},
    "idx.excluded.title":       {"en": "What's NOT Included in Fees", "de": "NICHT im Preis inbegriffen"},
    "idx.excluded.li1":         {"en": "University and uni-assist application fees", "de": "Universitäts- und uni-assist-Bewerbungsgebühren"},
    "idx.excluded.li2":         {"en": "Translation, notary and apostille costs", "de": "Übersetzungs-, Notar- und Apostillekosten"},
    "idx.excluded.li3":         {"en": "Visa fee", "de": "Visagebühr"},
    "idx.excluded.li4":         {"en": "Amount to be deposited for blocked account", "de": "Einzuzahlender Betrag für das Sperrkonto"},
    "idx.excluded.li5":         {"en": "Health insurance", "de": "Krankenversicherung"},
    "idx.excluded.li6":         {"en": "Language course fees", "de": "Sprachkursgebühren"},
    "idx.excluded.li7":         {"en": "Flight and accommodation expenses", "de": "Flug- und Unterkunftskosten"},
    "idx.excluded.li8":         {"en": "Fees requested by official authorities", "de": "Von Behörden verlangte Gebühren"},
    "idx.excluded.li9":         {"en": "Other third-party expenses", "de": "Sonstige Drittkosten"},
    "idx.disclaimer":           {"en": "Start Akademie does not guarantee university admission, visa outcome, equivalence decision, Ausbildung placement, employer acceptance, internship placement or accommodation. These decisions belong to the relevant institutions and authorities.", "de": "Start Akademie übernimmt keine Garantie für Universitätszulassung, Visumergebnis, Anerkennungsentscheid, Ausbildungsplatzvergabe, Arbeitgeberentscheidung, Praktikumsplatzvergabe oder Unterkunft. Diese Entscheidungen obliegen den zuständigen Institutionen und Behörden."},
}

# ─────────────────────────────────────────────
# HTML PATCHES  {filename: [(search, replacement), ...]}
# ─────────────────────────────────────────────
HTML_PATCHES = {

"uni.html": [
    # hero
    ('class="badge-prep">🎓 Üniversite Danışmanlığı',
     'class="badge-prep" data-i18n="uni.hero.badge">🎓 Üniversite Danışmanlığı'),
    ('<h1>Almanya\'da <em>Üniversite</em> Eğitimi</h1>',
     '<h1 data-i18n="uni.hero.title">Almanya\'da <em>Üniversite</em> Eğitimi</h1>'),
    ('class="hero-sub">Devlet üniversitelerine',
     'class="hero-sub" data-i18n="uni.hero.subtitle">Devlet üniversitelerine'),
    ('href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px;">Ücretsiz Ön Değerlendirme →',
     'href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px;" data-i18n="uni.hero.btn">Ücretsiz Ön Değerlendirme →'),
    # overview
    ('style="background: rgba(43, 112, 250, 0.1); color: var(--blue); border-color: var(--blue);">Profesyonel Destek',
     'style="background: rgba(43, 112, 250, 0.1); color: var(--blue); border-color: var(--blue);" data-i18n="uni.overview.badge">Profesyonel Destek'),
    ('<h2 style="margin-top: 16px;">Lisans, Yüksek Lisans ve <em>Studienkolleg</em> Süreçleri</h2>',
     '<h2 style="margin-top: 16px;" data-i18n="uni.overview.title">Lisans, Yüksek Lisans ve <em>Studienkolleg</em> Süreçleri</h2>'),
    ('class="lead-text" style="margin: 0 auto;">Almanya\'da üniversiteye giden yol',
     'class="lead-text" style="margin: 0 auto;" data-i18n="uni.overview.desc">Almanya\'da üniversiteye giden yol'),
    # card 1
    ('>Hangi Alanlarda Destek Veriyoruz?<',  '>Hangi Alanlarda Destek Veriyoruz?<'.replace('>', ' data-i18n="uni.card1.title">', 1)),
    ('>Lisans başvuruları<', ' data-i18n="uni.card1.li1">Lisans başvuruları<'),
    ('>Yüksek lisans başvuruları<', ' data-i18n="uni.card1.li2">Yüksek lisans başvuruları<'),
    ('>Studienkolleg yönlendirmesi<', ' data-i18n="uni.card1.li3">Studienkolleg yönlendirmesi<'),
    ('>Bölüm ve üniversite seçimi<', ' data-i18n="uni.card1.li4">Bölüm ve üniversite seçimi<'),
    ('>Şartlı kabul ve dil yolu değerlendirmesi<', ' data-i18n="uni.card1.li5">Şartlı kabul ve dil yolu değerlendirmesi<'),
    # card 2
    ('>Başvuru Süreçleri<', ' data-i18n="uni.card2.title">Başvuru Süreçleri<'),
    ('>uni-assist ve VPD işlemleri<', ' data-i18n="uni.card2.li1">uni-assist ve VPD işlemleri<'),
    ('>Doğrudan üniversite başvuruları<', ' data-i18n="uni.card2.li2">Doğrudan üniversite başvuruları<'),
    ('>Belge kontrolü ve dosya düzeni<', ' data-i18n="uni.card2.li3">Belge kontrolü ve dosya düzeni<'),
    ('>CV ve motivasyon yazısı desteği<', ' data-i18n="uni.card2.li4">CV ve motivasyon yazısı desteği<'),
    ('>Eksik belge taleplerinin takibi<', ' data-i18n="uni.card2.li5">Eksik belge taleplerinin takibi<'),
    # card 3
    ('>Kime Uygun?<', ' data-i18n="uni.card3.title">Kime Uygun?<'),
    ('>Lise mezunları<', ' data-i18n="uni.card3.li1">Lise mezunları<'),
    ('>Açık lise mezunları<', ' data-i18n="uni.card3.li2">Açık lise mezunları<'),
    ('>Üniversite öğrencileri<', ' data-i18n="uni.card3.li3">Üniversite öğrencileri<'),
    ('>Ön lisans mezunları<', ' data-i18n="uni.card3.li4">Ön lisans mezunları<'),
    ('>Lisans mezunları<', ' data-i18n="uni.card3.li5">Lisans mezunları<'),
    # badges
    ('>Kişiye Özel Strateji<', ' data-i18n="uni.badge1.title">Kişiye Özel Strateji<'),
    ('>Hedeflerinize uygun planlama<', ' data-i18n="uni.badge1.desc">Hedeflerinize uygun planlama<'),
    ('>Uzman Danışmanlık<', ' data-i18n="uni.badge2.title">Uzman Danışmanlık<'),
    ('>Almanya\'daki eğitim sistemi hakkında güncel bilgi<', ' data-i18n="uni.badge2.desc">Almanya\'daki eğitim sistemi hakkında güncel bilgi<'),
    ('>Güvenilir Destek<', ' data-i18n="uni.badge3.title">Güvenilir Destek<'),
    ('>Başvurudan kabulünüze kadar yanınızdayız<', ' data-i18n="uni.badge3.desc">Başvurudan kabulünüze kadar yanınızdayız<'),
    # faq
    ('<h2>Sık Sorulan <em>Sorular</em></h2>', '<h2 data-i18n="uni.faq.title">Sık Sorulan <em>Sorular</em></h2>'),
],

}

# ─────────────────────────────────────────────
# ENGINE: apply patches + inject to lang.js
# ─────────────────────────────────────────────

def apply_patches(filename, patches):
    path = os.path.join(DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    changed = 0
    for search, replace in patches:
        if search in html:
            html = html.replace(search, replace, 1)
            changed += 1
        else:
            # try flexible: strip leading >
            pass
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  {filename}: {changed}/{len(patches)} patches applied")


def inject_lang_js(translations):
    with open(LANG_JS_PATH, 'r', encoding='utf-8') as f:
        js = f.read()

    # Build insertion strings
    en_lines = ""
    de_lines = ""
    for key, vals in translations.items():
        en_v = vals["en"].replace('"', '\\"')
        de_v = vals["de"].replace('"', '\\"')
        en_lines += f'        "{key}": "{en_v}",\n'
        de_lines += f'        "{key}": "{de_v}",\n'

    # Insert at start of each lang block (after first { of the block)
    en_marker = '"en": {'
    de_marker = '"de": {'

    en_pos = js.find(en_marker)
    if en_pos != -1:
        insert_at = js.find('\n', en_pos) + 1
        js = js[:insert_at] + en_lines + js[insert_at:]

    de_pos = js.find(de_marker)
    if de_pos != -1:
        insert_at = js.find('\n', de_pos) + 1
        js = js[:insert_at] + de_lines + js[insert_at:]

    with open(LANG_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f"  lang.js: {len(translations)} new translation keys added (EN+DE)")


if __name__ == "__main__":
    print("=== i18n Patcher ===")

    for fname, patches in HTML_PATCHES.items():
        apply_patches(fname, patches)

    inject_lang_js(TRANSLATIONS)
    print("\nDone! Now re-run the subpage HTML patching script for dil/ausbildung/denklik/degisim/konaklama.")

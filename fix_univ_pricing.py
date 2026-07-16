import re
import json

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add i18n tags to university titles, descriptions, and acceptance rates
univs = [
    ("Münih Teknik Üniversitesi (TUM)", "Avrupa'nın en iyi teknik üniversitelerinden biri. Mühendislik, inovasyon ve teknolojide dünya çapında bir ekol.", "Kabul: ~%14"),
    ("LMU Münih", "Almanya'nın en büyük ikinci üniversitesi. Tıp, doğa bilimleri ve beşeri bilimlerde dünya lideri.", "Kabul: ~%16"),
    ("Berlin Teknik Üniversitesi", "Girişimcilik ve inovasyonun başkentinde, mühendislik ve sürdürülebilirlik konularında lider bir eğitim kurumu.", "Kabul: ~%18"),
    ("Karlsruhe Teknoloji Enstitüsü (KIT)", "Almanya'nın en büyük araştırma kurumlarından biri. Bilişim ve mühendislik bilimlerinde küresel bir inovasyon merkezi.", "Kabul: ~%16"),
    ("Freie Universität Berlin", "\"Özgür Üniversite\", siyaset bilimi, uluslararası ilişkiler ve sosyal bilimlerde Almanya'nın en saygın kurumlarından biridir.", "Kabul: ~%20"),
    ("Freiburg Üniversitesi", "1457 kuruluş yılıyla eşsiz bir tarihi miras. Çevre bilimleri, tıp ve hukuk alanlarında Avrupa'nın en iddialı üniversitelerinden.", "Kabul: ~%15"),
    ("Tübingen Üniversitesi", "Nobel ödüllü bilim insanlarının yetiştiği, yapay zeka, nörobilim ve teoloji alanlarında Avrupa'nın elit araştırma merkezi.", "Kabul: ~%12"),
    ("Bonn Üniversitesi", "Matematik ve ekonomide dünya çapında otorite. Görkemli ana binasıyla Almanya'nın en prestijli eğitim kurumlarından biri.", "Kabul: ~%18"),
    ("Göttingen Üniversitesi", "Tarih boyunca 40'tan fazla Nobel ödüllü isme ev sahipliği yapmış, fen bilimleri ve fizikte efsanevi bir akademik kurum.", "Kabul: ~%17"),
    ("Stuttgart Üniversitesi", "Almanya'nın sanayi ve teknoloji kalbinde yer alan, otomotiv ve uzay mühendisliği alanlarında öncü teknik üniversite.", "Kabul: ~%16"),
]

for i, (title, desc, acc) in enumerate(univs, 1):
    old_acc = f"<span>{acc}</span>"
    new_acc = f'<span data-i18n="univ{i}.acc">{acc}</span>'
    html = html.replace(old_acc, new_acc)
    
    old_title = f"<h3>{title}</h3>"
    new_title = f'<h3 data-i18n="univ{i}.title">{title}</h3>'
    html = html.replace(old_title, new_title)
    
    # We might have style="font-size: 0.92rem;" in the p tags
    # We use regex to find the description and add data-i18n
    desc_escaped = re.escape(desc)
    html = re.sub(rf'(<p[^>]*?)>({desc_escaped})</p>', rf'\1 data-i18n="univ{i}.desc">\2</p>', html)

html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=36', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update lang.js
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    lang = f.read()

en_pricing = '''        "price.desc": "Comprehensive application and visa guidance packages suited to your needs, from equivalence analysis to visa interview simulation.",
        "price.basic.sub": "Basic Application Package",
        "price.f1": "Academic Eligibility Analysis",
        "price.f2": "Major and University Selection",
        "price.f3": "Application up to 3 Universities",
        "price.f4": "Basic Motivation Letter Support",
        "price.f5": "Visa Interview Simulation",
        "price.f6": "Post-Arrival Support in Germany",
        "price.btn.basic": "Select Basic Package",
        "price.badge": "Most Popular",
        "price.plus.sub": "Comprehensive Application & Admission",
        "price.f7": "Application up to 5 Universities",
        "price.f8": "Detailed Motivation & CV Design",
        "price.f9": "Detailed Visa Document File Preparation",
        "price.f10": "1 Visa Interview Simulation",
        "price.f11": "3 Months Post-Arrival Support in Germany",
        "price.btn.plus": "Select Plus Package",
        "price.premium.sub": "Visa & Arrival Guaranteed VIP",
        "price.f12": "Application up to 8 Universities",
        "price.f13": "Extended CV & Motivation Writing",
        "price.f14": "2 One-on-one Visa Simulations",
        "price.f15": "Detailed Accommodation & Dormitory Guidance",
        "price.f16": "6 Months Post-Arrival Support in Germany",
        "price.btn.premium": "Select Premium Package",'''

de_pricing = '''        "price.desc": "Umfassende Antrags- und Visumberatungspakete nach Ihren Bedürfnissen, von der Äquivalenzanalyse bis zur Visum-Interview-Simulation.",
        "price.basic.sub": "Basis-Bewerbungspaket",
        "price.f1": "Akademische Eignungsanalyse",
        "price.f2": "Studienfach- und Universitätswahl",
        "price.f3": "Bewerbung an bis zu 3 Universitäten",
        "price.f4": "Grundlegende Unterstützung beim Motivationsschreiben",
        "price.f5": "Visum-Interview-Simulation",
        "price.f6": "Betreuung nach der Ankunft in Deutschland",
        "price.btn.basic": "Basis-Paket Auswählen",
        "price.badge": "Am Beliebtesten",
        "price.plus.sub": "Umfassende Bewerbung & Zulassung",
        "price.f7": "Bewerbung an bis zu 5 Universitäten",
        "price.f8": "Detaillierte Motivations- & Lebenslaufgestaltung",
        "price.f9": "Detaillierte Vorbereitung der Visumunterlagen",
        "price.f10": "1 Visum-Interview-Simulation",
        "price.f11": "3 Monate Betreuung nach der Ankunft",
        "price.btn.plus": "Plus-Paket Auswählen",
        "price.premium.sub": "Visum & Ankunft Garantiert VIP",
        "price.f12": "Bewerbung an bis zu 8 Universitäten",
        "price.f13": "Erweitertes Schreiben von Lebenslauf & Motivation",
        "price.f14": "2 Einzel-Visumsimulationen",
        "price.f15": "Detaillierte Unterkunfts- & Wohnheimsvermittlung",
        "price.f16": "6 Monate Betreuung nach der Ankunft",
        "price.btn.premium": "Premium-Paket Auswählen",'''

# Let's replace the single desc string with the whole block in EN and DE
lang = re.sub(r'"price\.desc": "Comprehensive application[^"]*",', en_pricing, lang)
lang = re.sub(r'"price\.desc": "Umfassende Antrags-[^"]*",', de_pricing, lang)

# Now, let's prepare the university translations!
tr_univs = ""
en_univs = ""
de_univs = ""

univ_data_en = [
    ("Technical University of Munich (TUM)", "One of Europe's top technical universities. A global hub for engineering, innovation, and technology.", "Acceptance: ~14%"),
    ("LMU Munich", "Germany's second-largest university. A world leader in medicine, natural sciences, and humanities.", "Acceptance: ~16%"),
    ("Technical University of Berlin", "A leading educational institution in engineering and sustainability, located in the capital of entrepreneurship and innovation.", "Acceptance: ~18%"),
    ("Karlsruhe Institute of Technology (KIT)", "One of Germany's largest research institutions. A global innovation center for computer science and engineering.", "Acceptance: ~16%"),
    ("Freie Universität Berlin", "The 'Free University' is one of Germany's most respected institutions in political science, international relations, and social sciences.", "Acceptance: ~20%"),
    ("University of Freiburg", "A unique historical legacy founded in 1457. One of Europe's most ambitious universities in environmental sciences, medicine, and law.", "Acceptance: ~15%"),
    ("University of Tübingen", "An elite research center in Europe for artificial intelligence, neuroscience, and theology, home to Nobel laureates.", "Acceptance: ~12%"),
    ("University of Bonn", "A global authority in mathematics and economics. One of Germany's most prestigious educational institutions with its magnificent main building.", "Acceptance: ~18%"),
    ("University of Göttingen", "A legendary academic institution in natural sciences and physics, having hosted more than 40 Nobel laureates throughout its history.", "Acceptance: ~17%"),
    ("University of Stuttgart", "A pioneering technical university in automotive and aerospace engineering, located in the industrial and technological heart of Germany.", "Acceptance: ~16%"),
]

univ_data_de = [
    ("Technische Universität München (TUM)", "Eine der besten technischen Universitäten Europas. Ein globales Zentrum für Ingenieurwesen, Innovation und Technologie.", "Zulassung: ~14%"),
    ("LMU München", "Zweitgrößte Universität Deutschlands. Weltweit führend in Medizin, Natur- und Geisteswissenschaften.", "Zulassung: ~16%"),
    ("Technische Universität Berlin", "Führende Bildungseinrichtung für Ingenieurwesen und Nachhaltigkeit in der Hauptstadt des Unternehmertums und der Innovation.", "Zulassung: ~18%"),
    ("Karlsruher Institut für Technologie (KIT)", "Eine der größten Forschungseinrichtungen Deutschlands. Ein globales Innovationszentrum für Informatik und Ingenieurwissenschaften.", "Zulassung: ~16%"),
    ("Freie Universität Berlin", "Die 'Freie Universität' ist eine der angesehensten Institutionen Deutschlands für Politikwissenschaft, internationale Beziehungen und Sozialwissenschaften.", "Zulassung: ~20%"),
    ("Universität Freiburg", "Ein einzigartiges historisches Erbe, gegründet 1457. Eine der ehrgeizigsten Universitäten Europas in Umweltwissenschaften, Medizin und Recht.", "Zulassung: ~15%"),
    ("Universität Tübingen", "Ein elitäres europäisches Forschungszentrum für Künstliche Intelligenz, Neurowissenschaften und Theologie, Heimat von Nobelpreisträgern.", "Zulassung: ~12%"),
    ("Universität Bonn", "Eine weltweite Autorität in Mathematik und Wirtschaft. Eine der renommiertesten Bildungseinrichtungen Deutschlands mit ihrem prächtigen Hauptgebäude.", "Zulassung: ~18%"),
    ("Universität Göttingen", "Eine legendäre akademische Einrichtung für Naturwissenschaften und Physik, die im Laufe ihrer Geschichte über 40 Nobelpreisträger hervorgebracht hat.", "Zulassung: ~17%"),
    ("Universität Stuttgart", "Eine wegweisende technische Universität in den Bereichen Automobil- und Luft- und Raumfahrttechnik, gelegen im industriellen und technologischen Herzen Deutschlands.", "Zulassung: ~16%"),
]

for i in range(1, 11):
    tr_univs += f'''        "univ{i}.title": "{univs[i-1][0]}",
        "univ{i}.desc": "{univs[i-1][1]}",
        "univ{i}.acc": "{univs[i-1][2]}",\n'''
    en_univs += f'''        "univ{i}.title": "{univ_data_en[i-1][0]}",
        "univ{i}.desc": "{univ_data_en[i-1][1]}",
        "univ{i}.acc": "{univ_data_en[i-1][2]}",\n'''
    de_univs += f'''        "univ{i}.title": "{univ_data_de[i-1][0]}",
        "univ{i}.desc": "{univ_data_de[i-1][1]}",
        "univ{i}.acc": "{univ_data_de[i-1][2]}",\n'''

# Append these to the respective sections in lang.js
lang = lang.replace('"extra.title": "Ek Hizmetler', tr_univs + '        "extra.title": "Ek Hizmetler')
lang = lang.replace('"extra.title": "Additional Services', en_univs + '        "extra.title": "Additional Services')
lang = lang.replace('"extra.title": "Zusätzliche Dienste', de_univs + '        "extra.title": "Zusätzliche Dienste')

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(lang)


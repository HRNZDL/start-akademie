import io

lang_path = 'assets/lang.js'

with io.open(lang_path, 'r', encoding='utf-8') as f:
    lang_content = f.read()

en_keys = """
        "price.badge": "Most Popular",
        "price.basic.sub": "Basic Application Package",
        "price.plus.sub": "Comprehensive Application & Admission",
        "price.premium.sub": "Visa & Arrival Guaranteed VIP",
        "price.btn.basic": "Select Basic",
        "price.btn.plus": "Select Plus",
        "price.btn.premium": "Select Premium",
        "price.f1": "Academic Eligibility Analysis",
        "price.f2": "Department and University Selection",
        "price.f3": "Application to up to 3 Universities",
        "price.f4": "Basic Motivation Letter Support",
        "price.f5": "Visa Interview Simulation",
        "price.f6": "Post-Arrival Support in Germany",
        "price.f7": "Application to up to 5 Universities",
        "price.f8": "Detailed Motivation & CV Design",
        "price.f9": "Detailed Visa Document Preparation",
        "price.f10": "1 Visa Interview Simulation",
        "price.f11": "3 Months Post-Arrival Support",
        "price.f12": "Application to up to 8 Universities",
        "price.f13": "Extended CV & Motivation Writing",
        "price.f14": "2 1-on-1 Visa Simulations",
        "price.f15": "Detailed Accommodation & Dorm Guidance",
        "price.f16": "6 Months Post-Arrival Support",
        "extra.title": "Additional Services & Modules",
        "extra.desc": "Single or add-on package options tailored to your specific needs.",
        "extra.s1": "Visa Guide Package",
        "extra.s1_desc": "For those who only need visa file preparation and simulation.",
        "extra.s2": "Single Application Package",
        "extra.s2_desc": "Targeted application and tracking for a single university.",
        "extra.s3": "Arrival in Germany & First Steps",
        "extra.s3_desc": "Residence registration, bank account, and health insurance activation.",
        "extra.s4": "German Preparation & Language Planning",
        "extra.s4_desc": "Language school registration, dorm planning, and conditional acceptance process.",
"""

de_keys = """
        "price.badge": "Am Beliebtesten",
        "price.basic.sub": "Basis-Bewerbungspaket",
        "price.plus.sub": "Umfassende Bewerbung & Zulassung",
        "price.premium.sub": "Visum & Ankunft Garantiert VIP",
        "price.btn.basic": "Basic Auswählen",
        "price.btn.plus": "Plus Auswählen",
        "price.btn.premium": "Premium Auswählen",
        "price.f1": "Analyse der akademischen Eignung",
        "price.f2": "Fach- und Universitätswahl",
        "price.f3": "Bewerbung an bis zu 3 Universitäten",
        "price.f4": "Grundlegende Unterstützung beim Motivationsschreiben",
        "price.f5": "Visum-Interview-Simulation",
        "price.f6": "Unterstützung nach der Ankunft in Deutschland",
        "price.f7": "Bewerbung an bis zu 5 Universitäten",
        "price.f8": "Detailliertes Motivations- & Lebenslauf-Design",
        "price.f9": "Detaillierte Vorbereitung der Visumunterlagen",
        "price.f10": "1 Visum-Interview-Simulation",
        "price.f11": "3 Monate Unterstützung nach der Ankunft",
        "price.f12": "Bewerbung an bis zu 8 Universitäten",
        "price.f13": "Erweitertes Schreiben von Lebenslauf & Motivation",
        "price.f14": "2 1-zu-1 Visum-Simulationen",
        "price.f15": "Detaillierte Unterkunfts- & Wohnheimberatung",
        "price.f16": "6 Monate Unterstützung nach der Ankunft",
        "extra.title": "Zusätzliche Dienstleistungen",
        "extra.desc": "Einzel- oder Zusatzpaketoptionen zugeschnitten auf Ihre spezifischen Bedürfnisse.",
        "extra.s1": "Visum-Guide-Paket",
        "extra.s1_desc": "Für diejenigen, die nur die Erstellung und Simulation der Visumunterlagen benötigen.",
        "extra.s2": "Einzelbewerbungspaket",
        "extra.s2_desc": "Gezielte Bewerbung und Verfolgung für eine einzelne Universität.",
        "extra.s3": "Ankunft in Deutschland & Erste Schritte",
        "extra.s3_desc": "Wohnsitzanmeldung, Bankkonto und Aktivierung der Krankenversicherung.",
        "extra.s4": "Deutsch-Vorbereitung & Sprachplanung",
        "extra.s4_desc": "Sprachschulanmeldung, Wohnheimplanung und Prozess der bedingten Zulassung.",
"""

if "price.btn.basic" not in lang_content.split('"en": {')[1].split('},')[0]:
    lang_content = lang_content.replace(
        '"price.title": "Official Consulting Packages",', 
        f'"price.title": "Official Consulting Packages",{en_keys}'
    )

if "price.btn.basic" not in lang_content.split('"de": {')[1].split('},')[0]:
    lang_content = lang_content.replace(
        '"price.title": "Offizielle Beratungspakete",', 
        f'"price.title": "Offizielle Beratungspakete",{de_keys}'
    )

with io.open(lang_path, 'w', encoding='utf-8') as f:
    f.write(lang_content)

print("EN and DE translation keys successfully injected.")

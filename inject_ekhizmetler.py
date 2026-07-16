import io

index_path = 'index.html'
lang_path = 'assets/lang.js'

with io.open(index_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# HTML to insert
ek_hizmetler_html = """
            <!-- EK HİZMETLER MODÜLÜ -->
            <div style="margin-top: 64px;">
                <div style="text-align: center; margin-bottom: 32px;">
                    <h3 style="font-size: 1.8rem; font-family: var(--font-serif);" data-i18n="extra.title">Ek Hizmetler & Modüller</h3>
                    <p style="color: var(--text-muted);" data-i18n="extra.desc">Özel ihtiyaçlarınıza yönelik tekli veya ek paket seçenekleri.</p>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px;">
                    <div class="glass-card" style="padding: 24px; text-align: center;">
                        <h4 style="margin-bottom: 12px; color: var(--gold);" data-i18n="extra.s1">Vize Rehberim Paketi</h4>
                        <div style="font-size: 1.5rem; font-weight: 600; margin-bottom: 12px;">1.200 €</div>
                        <p style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="extra.s1_desc">Sadece vize dosyası hazırlığı ve simülasyon isteyenler için.</p>
                    </div>
                    <div class="glass-card" style="padding: 24px; text-align: center;">
                        <h4 style="margin-bottom: 12px; color: var(--gold);" data-i18n="extra.s2">Tek Başvuru Paketi</h4>
                        <div style="font-size: 1.5rem; font-weight: 600; margin-bottom: 12px;">950 €</div>
                        <p style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="extra.s2_desc">Tek bir üniversiteye nokta atışı başvuru ve takip.</p>
                    </div>
                    <div class="glass-card" style="padding: 24px; text-align: center;">
                        <h4 style="margin-bottom: 12px; color: var(--gold);" data-i18n="extra.s3">Almanya'ya Varış & İlk Adımlar</h4>
                        <div style="font-size: 1.5rem; font-weight: 600; margin-bottom: 12px;">450 €</div>
                        <p style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="extra.s3_desc">İkamet kaydı, banka hesabı ve sağlık sigortası aktivasyonu.</p>
                    </div>
                    <div class="glass-card" style="padding: 24px; text-align: center;">
                        <h4 style="margin-bottom: 12px; color: var(--gold);" data-i18n="extra.s4">Almanca Hazırlık & Dil Planlama</h4>
                        <div style="font-size: 1.5rem; font-weight: 600; margin-bottom: 12px;">550 €</div>
                        <p style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="extra.s4_desc">Dil okulu kaydı, yurt planlaması ve şartlı kabul süreci.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ══════════════════════════════════════════
         INTERACTIVE DENKLİK VE UYGUNLUK TESTİ"""

search_str = """        </div>
    </section>

    <!-- ══════════════════════════════════════════
         INTERACTIVE DENKLİK VE UYGUNLUK TESTİ"""

if search_str in html_content:
    new_html = html_content.replace(search_str, ek_hizmetler_html)
    with io.open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("HTML updated.")
else:
    print("Search string not found in index.html.")


with io.open(lang_path, 'r', encoding='utf-8') as f:
    lang_content = f.read()

# TR injections
tr_inject = """        "price.desc": "Denklik analizinden vize randevu simülasyonuna kadar ihtiyacınıza uygun kapsamlı başvuru ve vize rehberliği paketlerimiz.",
        "extra.title": "Ek Hizmetler & Modüller",
        "extra.desc": "Özel ihtiyaçlarınıza yönelik tekli veya ek paket seçenekleri.",
        "extra.s1": "Vize Rehberim Paketi",
        "extra.s1_desc": "Sadece vize dosyası hazırlığı ve simülasyon isteyenler için.",
        "extra.s2": "Tek Başvuru Paketi",
        "extra.s2_desc": "Tek bir üniversiteye nokta atışı başvuru ve takip.",
        "extra.s3": "Almanya'ya Varış & İlk Adımlar",
        "extra.s3_desc": "İkamet kaydı, banka hesabı ve sağlık sigortası aktivasyonu.",
        "extra.s4": "Almanca Hazırlık & Dil Planlama",
        "extra.s4_desc": "Dil okulu kaydı, yurt planlaması ve şartlı kabul süreci.","""

lang_content = lang_content.replace('"price.desc": "Denklik analizinden vize randevu simülasyonuna kadar ihtiyacınıza uygun kapsamlı başvuru ve vize rehberliği paketlerimiz.",', tr_inject)

# EN injections
en_inject = """        "price.desc": "Comprehensive application and visa guidance packages tailored to your needs, from equivalence analysis to visa appointment simulation.",
        "extra.title": "Additional Services & Modules",
        "extra.desc": "Single or add-on package options tailored to your specific needs.",
        "extra.s1": "Visa Guide Package",
        "extra.s1_desc": "For those who only need visa file preparation and simulation.",
        "extra.s2": "Single Application Package",
        "extra.s2_desc": "Targeted application and tracking for a single university.",
        "extra.s3": "Arrival in Germany & First Steps",
        "extra.s3_desc": "Residence registration, bank account, and health insurance activation.",
        "extra.s4": "German Preparation & Language Planning",
        "extra.s4_desc": "Language school registration, dorm planning, and conditional acceptance process.","""

lang_content = lang_content.replace('"price.desc": "Comprehensive application and visa guidance packages tailored to your needs, from equivalence analysis to visa appointment simulation.",', en_inject)

# DE injections
de_inject = """        "price.desc": "Umfassende Bewerbungs- und Visumberatungspakete nach Ihren Bedürfnissen, von der Anerkennungsanalyse bis zur Visum-Simulation.",
        "extra.title": "Zusätzliche Dienstleistungen",
        "extra.desc": "Einzel- oder Zusatzpaketoptionen zugeschnitten auf Ihre spezifischen Bedürfnisse.",
        "extra.s1": "Visum-Guide-Paket",
        "extra.s1_desc": "Für diejenigen, die nur die Erstellung und Simulation der Visumunterlagen benötigen.",
        "extra.s2": "Einzelbewerbungspaket",
        "extra.s2_desc": "Gezielte Bewerbung und Verfolgung für eine einzelne Universität.",
        "extra.s3": "Ankunft in Deutschland & Erste Schritte",
        "extra.s3_desc": "Wohnsitzanmeldung, Bankkonto und Aktivierung der Krankenversicherung.",
        "extra.s4": "Deutsch-Vorbereitung & Sprachplanung",
        "extra.s4_desc": "Sprachschulanmeldung, Wohnheimplanung und Prozess der bedingten Zulassung.","""

lang_content = lang_content.replace('"price.desc": "Umfassende Bewerbungs- und Visumberatungspakete nach Ihren Bedürfnissen, von der Anerkennungsanalyse bis zur Visum-Simulation.",', de_inject)

with io.open(lang_path, 'w', encoding='utf-8') as f:
    f.write(lang_content)
print("Lang updated.")

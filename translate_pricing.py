import io
import re

lang_path = 'assets/lang.js'
index_path = 'index.html'

# 1. Update lang.js
with io.open(lang_path, 'r', encoding='utf-8') as f:
    lang_content = f.read()

tr_keys = """        "price.badge": "En Çok Tercih Edilen",
        "price.basic.sub": "Temel Başvuru Paketi",
        "price.plus.sub": "Kapsamlı Başvuru & Kabul",
        "price.premium.sub": "Vize & Varış Garantili VIP",
        "price.btn.basic": "Basic Paket Seç",
        "price.btn.plus": "Plus Paket Seç",
        "price.btn.premium": "Premium Paket Seç",
        "price.f1": "Akademik Uygunluk Analizi",
        "price.f2": "Bölüm ve Üniversite Seçimi",
        "price.f3": "3 Üniversiteye Kadar Başvuru",
        "price.f4": "Temel Motivasyon Mektubu Desteği",
        "price.f5": "Vize Görüşmesi Simülasyonu",
        "price.f6": "Almanya Sonrası Destek",
        "price.f7": "5 Üniversiteye Kadar Başvuru",
        "price.f8": "Detaylı Motivasyon & CV Tasarımı",
        "price.f9": "Detaylı Vize Evrak Dosyası Hazırlığı",
        "price.f10": "1 Adet Vize Randevu Simülasyonu",
        "price.f11": "Almanya Sonrası 3 Ay Destek",
        "price.f12": "8 Üniversiteye Kadar Başvuru",
        "price.f13": "Genişletilmiş CV & Motivasyon Yazımı",
        "price.f14": "2 Adet Birebir Vize Simülasyonu",
        "price.f15": "Detaylı Konaklama & Yurt Yönlendirmesi",
        "price.f16": "Almanya Sonrası 6 Ay Destek","""

en_keys = """        "price.badge": "Most Popular",
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
        "price.f16": "6 Months Post-Arrival Support","""

de_keys = """        "price.badge": "Am Beliebtesten",
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
        "price.f16": "6 Monate Unterstützung nach der Ankunft","""

lang_content = lang_content.replace('"price.desc": "Denklik analizinden vize randevu simülasyonuna kadar ihtiyacınıza uygun kapsamlı başvuru ve vize rehberliği paketlerimiz.",',
                                     f'"price.desc": "Denklik analizinden vize randevu simülasyonuna kadar ihtiyacınıza uygun kapsamlı başvuru ve vize rehberliği paketlerimiz.",\n{tr_keys}')
lang_content = lang_content.replace('"price.desc": "Comprehensive application and visa guidance packages tailored to your needs, from equivalence analysis to visa appointment simulation.",',
                                     f'"price.desc": "Comprehensive application and visa guidance packages tailored to your needs, from equivalence analysis to visa appointment simulation.",\n{en_keys}')
lang_content = lang_content.replace('"price.desc": "Umfassende Bewerbungs- und Visumberatungspakete nach Ihren Bedürfnissen, von der Anerkennungsanalyse bis zur Visum-Simulation.",',
                                     f'"price.desc": "Umfassende Bewerbungs- und Visumberatungspakete nach Ihren Bedürfnissen, von der Anerkennungsanalyse bis zur Visum-Simulation.",\n{de_keys}')

with io.open(lang_path, 'w', encoding='utf-8') as f:
    f.write(lang_content)


# 2. Update index.html
with io.open(index_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_replacements = {
    'Temel Başvuru Paketi': '<span data-i18n="price.basic.sub">Temel Başvuru Paketi</span>',
    'Kapsamlı Başvuru & Kabul': '<span data-i18n="price.plus.sub">Kapsamlı Başvuru & Kabul</span>',
    'Vize & Varış Garantili VIP': '<span data-i18n="price.premium.sub">Vize & Varış Garantili VIP</span>',
    'En Çok Tercih Edilen': '<span data-i18n="price.badge">En Çok Tercih Edilen</span>',
    'Akademik Uygunluk Analizi': '<span data-i18n="price.f1">Akademik Uygunluk Analizi</span>',
    'Bölüm ve Üniversite Seçimi': '<span data-i18n="price.f2">Bölüm ve Üniversite Seçimi</span>',
    '3 Üniversiteye Kadar Başvuru': '<span data-i18n="price.f3">3 Üniversiteye Kadar Başvuru</span>',
    'Temel Motivasyon Mektubu Desteği': '<span data-i18n="price.f4">Temel Motivasyon Mektubu Desteği</span>',
    'Vize Görüşmesi Simülasyonu': '<span data-i18n="price.f5">Vize Görüşmesi Simülasyonu</span>',
    'Almanya Sonrası Destek': '<span data-i18n="price.f6">Almanya Sonrası Destek</span>',
    '5 Üniversiteye Kadar Başvuru': '<span data-i18n="price.f7">5 Üniversiteye Kadar Başvuru</span>',
    'Detaylı Motivasyon & CV Tasarımı': '<span data-i18n="price.f8">Detaylı Motivasyon & CV Tasarımı</span>',
    'Detaylı Vize Evrak Dosyası Hazırlığı': '<span data-i18n="price.f9">Detaylı Vize Evrak Dosyası Hazırlığı</span>',
    '1 Adet Vize Randevu Simülasyonu': '<span data-i18n="price.f10">1 Adet Vize Randevu Simülasyonu</span>',
    'Almanya Sonrası 3 Ay Destek': '<span data-i18n="price.f11">Almanya Sonrası 3 Ay Destek</span>',
    '8 Üniversiteye Kadar Başvuru': '<span data-i18n="price.f12">8 Üniversiteye Kadar Başvuru</span>',
    'Genişletilmiş CV & Motivasyon Yazımı': '<span data-i18n="price.f13">Genişletilmiş CV & Motivasyon Yazımı</span>',
    '2 Adet Birebir Vize Simülasyonu': '<span data-i18n="price.f14">2 Adet Birebir Vize Simülasyonu</span>',
    'Detaylı Konaklama & Yurt Yönlendirmesi': '<span data-i18n="price.f15">Detaylı Konaklama & Yurt Yönlendirmesi</span>',
    'Almanya Sonrası 6 Ay Destek': '<span data-i18n="price.f16">Almanya Sonrası 6 Ay Destek</span>',
    '>Basic Paket Seç<': ' data-i18n="price.btn.basic">Basic Paket Seç<',
    '>Plus Paket Seç<': ' data-i18n="price.btn.plus">Plus Paket Seç<',
    '>Premium Paket Seç<': ' data-i18n="price.btn.premium">Premium Paket Seç<'
}

# Apply replacements to html
for old_text, new_text in html_replacements.items():
    # Only replace if not already wrapped in data-i18n
    if f'data-i18n' not in old_text and f'data-i18n' not in html_content.split(old_text)[0][-15:]:
        # Avoid double replacing if I run the script twice
        html_content = html_content.replace(old_text, new_text)

with io.open(index_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Translation strings integrated into lang.js and index.html")

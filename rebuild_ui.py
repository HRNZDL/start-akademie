import io
import re

index_path = 'index.html'

with io.open(index_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# ----------------------------------------
# 1. WIZARD REPLACEMENT
# ----------------------------------------

wizard_old_str = """    <section class="section-padding" id="wizard">
        <div class="container">
            <div class="glass-card wizard-layout">
                <div style="text-align: center; margin-bottom: 40px;">
                    <span class="section-tag">Hızlı Denklik Testi</span>
                    <h2>Almanya Üniversite Uygunluk Sihirbazı</h2>
                    <p style="margin-top: 12px; font-size: 0.95rem;">Lise mezuniyet bilginize göre doğrudan Almanya devlet üniversitesine kabul alıp alamayacağınızı 4 adımda hızlıca kontrol edin.</p>
                </div>

                <div class="wizard-progress">
                    <div class="wizard-progress-bar" id="wizard-progress"></div>
                </div>

                <!-- Step 1 -->
                <div class="wizard-step active" id="step-1">
                    <h4 style="font-size: 1.2rem; text-align: center;">1. Mezun olduğunuz / olacağınız lise türü hangisidir?</h4>
                    <div class="wizard-buttons">
                        <button class="wizard-btn-option" onclick="nextWizardStep(2, 'anadolu')">Anadolu veya Fen Lisesi</button>
                        <button class="wizard-btn-option" onclick="nextWizardStep(2, 'meslek')">Meslek veya İmam Hatip Lisesi</button>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="wizard-step" id="step-2">
                    <h4 style="font-size: 1.2rem; text-align: center;">2. Uluslararası bir diplomanız var mı? (IB, Abitur, AP vb.)</h4>
                    <div class="wizard-buttons">
                        <button class="wizard-btn-option" onclick="nextWizardStep(3, 'yes')">Evet (IB / Abitur / AP mevcut)</button>
                        <button class="wizard-btn-option" onclick="nextWizardStep(3, 'no')">Hayır (Sadece YKS / Lise Diploması)</button>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="wizard-step" id="step-3">
                    <h4 style="font-size: 1.2rem; text-align: center;">3. Güncel Almanca dil seviyeniz nedir?</h4>
                    <div class="wizard-buttons">
                        <button class="wizard-btn-option" onclick="nextWizardStep(4, 'b1')">B1 ve Üzeri</button>
                        <button class="wizard-btn-option" onclick="nextWizardStep(4, 'zero')">Başlangıç Seviyesi / Hiç Yok</button>
                    </div>
                </div>

                <!-- Step 4 -->
                <div class="wizard-step" id="step-4">
                    <h4 style="font-size: 1.2rem; text-align: center;">4. YKS sınavına girdiniz mi ve bir üniversiteye yerleştiniz mi?</h4>
                    <div class="wizard-buttons">
                        <button class="wizard-btn-option" onclick="showWizardResult('yes')">Evet, 4 yıllık bölüme yerleştim</button>
                        <button class="wizard-btn-option" onclick="showWizardResult('no')">Hayır, henüz girmedim/yerleşmedim</button>
                    </div>
                </div>

                <!-- Result -->
                <div class="wizard-step" id="step-result">
                    <div class="wizard-result-box">
                        <div id="result-title" style="font-family: var(--font-serif); font-style: italic; font-size: 2.2rem; color: var(--gold); margin-bottom: 16px;">Değerlendiriliyor...</div>
                        <p id="result-desc" style="font-size: 1rem; color: var(--text-muted); line-height: 1.8; max-width: 600px; margin: 0 auto 32px;"></p>
                        <a href="#contact" class="btn btn-primary" data-i18n="wizard.btn">Birebir Analiz Randevusu Alın</a>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

wizard_new_str = """    <section class="section-padding" id="wizard">
        <div class="container">
            <div class="glass-card wizard-layout">
                <div style="text-align: center; margin-bottom: 40px;">
                    <span class="section-tag" data-i18n="wizard.tag">Hızlı Denklik Testi</span>
                    <h2 data-i18n="wizard.title">Almanya Üniversite Uygunluk Sihirbazı</h2>
                    <p style="margin-top: 12px; font-size: 0.95rem;" data-i18n="wizard.desc">Lise mezuniyet bilginize göre doğrudan Almanya devlet üniversitesine kabul alıp alamayacağınızı 4 adımda hızlıca kontrol edin.</p>
                </div>

                <div class="wizard-progress">
                    <div class="wizard-progress-bar" id="wizard-progress"></div>
                </div>

                <!-- Step 1 -->
                <div class="wizard-step active" id="step-1">
                    <h4 style="font-size: 1.2rem; text-align: center;" data-i18n="wizard.step1.q">1. Mezun olduğunuz / olacağınız lise türü hangisidir?</h4>
                    <div class="wizard-buttons">
                        <button class="wizard-btn-option" onclick="nextWizardStep(2, 'anadolu')" data-i18n="wizard.step1.o1">Anadolu veya Fen Lisesi</button>
                        <button class="wizard-btn-option" onclick="nextWizardStep(2, 'meslek')" data-i18n="wizard.step1.o2">Meslek veya İmam Hatip Lisesi</button>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="wizard-step" id="step-2">
                    <h4 style="font-size: 1.2rem; text-align: center;" data-i18n="wizard.step2.q">2. Uluslararası bir diplomanız var mı? (IB, Abitur, AP vb.)</h4>
                    <div class="wizard-buttons">
                        <button class="wizard-btn-option" onclick="nextWizardStep(3, 'yes')" data-i18n="wizard.step2.o1">Evet (IB / Abitur / AP mevcut)</button>
                        <button class="wizard-btn-option" onclick="nextWizardStep(3, 'no')" data-i18n="wizard.step2.o2">Hayır (Sadece YKS / Lise Diploması)</button>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="wizard-step" id="step-3">
                    <h4 style="font-size: 1.2rem; text-align: center;" data-i18n="wizard.step3.q">3. Güncel Almanca dil seviyeniz nedir?</h4>
                    <div class="wizard-buttons">
                        <button class="wizard-btn-option" onclick="nextWizardStep(4, 'b1')" data-i18n="wizard.step3.o1">B1 ve Üzeri</button>
                        <button class="wizard-btn-option" onclick="nextWizardStep(4, 'zero')" data-i18n="wizard.step3.o2">Başlangıç Seviyesi / Hiç Yok</button>
                    </div>
                </div>

                <!-- Step 4 -->
                <div class="wizard-step" id="step-4">
                    <h4 style="font-size: 1.2rem; text-align: center;" data-i18n="wizard.step4.q">4. YKS sınavına girdiniz mi ve bir üniversiteye yerleştiniz mi?</h4>
                    <div class="wizard-buttons">
                        <button class="wizard-btn-option" onclick="showWizardResult('yes')" data-i18n="wizard.step4.o1">Evet, 4 yıllık bölüme yerleştim</button>
                        <button class="wizard-btn-option" onclick="showWizardResult('no')" data-i18n="wizard.step4.o2">Hayır, henüz girmedim/yerleşmedim</button>
                    </div>
                </div>

                <!-- Result -->
                <div class="wizard-step" id="step-result">
                    <div class="wizard-result-box">
                        <div id="result-title" style="font-family: var(--font-serif); font-style: italic; font-size: 2.2rem; color: var(--gold); margin-bottom: 16px;">Değerlendiriliyor...</div>
                        <p id="result-desc" style="font-size: 1rem; color: var(--text-muted); line-height: 1.8; max-width: 600px; margin: 0 auto 32px;"></p>
                        <a href="#contact" class="btn btn-primary" data-i18n="wizard.btn">Birebir Analiz Randevusu Alın</a>
                    </div>
                </div>
            </div>
        </div>
    </section>"""


# ----------------------------------------
# 2. CAMP REPLACEMENT
# ----------------------------------------

# The camp block starts at id="camp" and ends right before the FAQ section
camp_regex = re.compile(r'<section class="section-padding" style="background: rgba\(255, 255, 255, 0\.01\);" id="camp">.*?(?=<!-- ══════════════════════════════════════════\s*FAQ SIKÇA SORULAN SORULAR)', re.DOTALL)

camp_new_str = """<section class="section-padding" style="background: rgba(255, 255, 255, 0.01);" id="camp">
        <div class="container">
            <div style="text-align: center; max-width: 800px; margin: 0 auto 64px;">
                <span class="section-tag" data-i18n="camp.tag">Abitur / Oberstufe Boost</span>
                <h2 data-i18n="camp.title">Yaz Kampları & Yoğunlaştırılmış Kurslar 2026</h2>
                <p style="margin-top: 16px;" data-i18n="camp.desc">Lise eğitimine veya Abitur'a yönelik özel hazırlanın - ister Rüsselsheim'da yüz yüze yoğun, ister online esnek birebir derslerle.</p>
            </div>

            <!-- In-Person Camp -->
            <div style="margin-bottom: 64px;">
                <div class="glass-card" style="border: 1px solid rgba(212, 175, 100, 0.3);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 24px; margin-bottom: 24px;">
                        <div>
                            <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--gold); letter-spacing: 0.1em; display: block; margin-bottom: 8px;" data-i18n="camp.inperson.tag">YÜZ YÜZE YOĞUNLAŞTIRILMIŞ KAMP</span>
                            <h3 style="font-size: 2rem; margin: 0;" data-i18n="camp.inperson.title">12. Sınıfa Güçlü Başlangıç</h3>
                            <p style="color: var(--text-muted); margin-top: 12px; max-width: 600px;" data-i18n="camp.inperson.desc">12. sınıfa geçiş hayati bir adımdır. Yoğunlaştırılmış kampımızla öğrencileri lise (Oberstufe) gereksinimlerine özel olarak hazırlıyoruz.</p>
                        </div>
                        <div style="background: rgba(212, 175, 100, 0.1); padding: 16px 24px; border-radius: 8px; text-align: center; min-width: 200px;">
                            <div style="font-size: 0.8rem; color: var(--gold); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;" data-i18n="camp.inperson.dates">2026 KAMP TARİHLERİ</div>
                            <div style="font-weight: 600; margin-bottom: 4px;" data-i18n="camp.inperson.d1">Cumartesi, 25.07.2026</div>
                            <div style="font-weight: 600; margin-bottom: 4px;" data-i18n="camp.inperson.d2">Cumartesi, 01.08.2026</div>
                            <div style="font-weight: 600; margin-bottom: 4px;" data-i18n="camp.inperson.d3">Cumartesi, 15.08.2026</div>
                            <div style="font-weight: 600;" data-i18n="camp.inperson.d4">Cumartesi, 22.08.2026</div>
                        </div>
                    </div>
                    
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px;">
                        <div>
                            <ul style="list-style: none; padding: 0; margin: 0;">
                                <li class="check" data-i18n="camp.inperson.f1">Matematik (Lise İleri Düzey)</li>
                                <li class="check" data-i18n="camp.inperson.f2">Almanca: Analiz & Yazma Eğitimi</li>
                                <li class="check" data-i18n="camp.inperson.f3">İngilizce: Makale & Metin Analizi</li>
                                <li class="check" data-i18n="camp.inperson.f4">Sınav Eğitimi & Öğrenme Stratejileri</li>
                            </ul>
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 12px; justify-content: center;">
                            <div style="display: flex; align-items: center; gap: 12px;">
                                <i data-lucide="clock" style="color: var(--gold); width: 20px;"></i>
                                <span data-i18n="camp.inperson.info1">09:00 - 16:30 arası</span>
                            </div>
                            <div style="display: flex; align-items: center; gap: 12px;">
                                <i data-lucide="users" style="color: var(--gold); width: 20px;"></i>
                                <span data-i18n="camp.inperson.info2">5 - 8 Kişilik Gruplar</span>
                            </div>
                            <div style="display: flex; align-items: center; gap: 12px;">
                                <i data-lucide="map-pin" style="color: var(--gold); width: 20px;"></i>
                                <span data-i18n="camp.inperson.info3">Start Akademie - Rüsselsheim</span>
                            </div>
                        </div>
                        <div style="display: flex; align-items: center; justify-content: flex-end;">
                            <a href="#contact" class="btn btn-primary" data-i18n="camp.inperson.btn">Yerini Ayırt</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Online Camp -->
            <div>
                <div style="text-align: center; margin-bottom: 40px;">
                    <h3 style="font-size: 1.8rem; font-family: var(--font-serif);" data-i18n="camp.online.title">Online İngilizce Yaz Kursları (1:1)</h3>
                    <p style="color: var(--text-muted); font-family: var(--font-mono); font-size: 0.9rem;" data-i18n="camp.online.desc">4 Hafta (06.07. - 31.07.2026) | Pazartesi - Cuma, Her Gün 90 dk | Toplam 20 Ders</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
                    <!-- Class 11 -->
                    <div class="glass-card" style="padding: 32px;">
                        <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--gold); letter-spacing: 0.1em; display: block; margin-bottom: 8px;" data-i18n="camp.class11.tag">11. SINIF</span>
                        <h4 style="font-size: 1.3rem; margin-bottom: 16px;" data-i18n="camp.class11.title">Lise Hazırlık (Oberstufe)</h4>
                        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; font-size: 0.95rem; color: var(--text-muted);">
                            <li data-i18n="camp.class11.p1"><strong>Gramer & Yazım:</strong> Zamanlar, Edilgen Çatı, Deneme Yazımı.</li>
                            <li data-i18n="camp.class11.p2"><strong>Metin Analizi & Edebiyat:</strong> Kısa hikaye yorumlama.</li>
                            <li data-i18n="camp.class11.p3"><strong>Kültür & Medya:</strong> Birleşik Krallık/ABD siyasetini anlama.</li>
                            <li data-i18n="camp.class11.p4"><strong>Argümantasyon:</strong> Fikirleri temellendirme.</li>
                        </ul>
                    </div>
                    <!-- Class 12 -->
                    <div class="glass-card" style="padding: 32px; border-color: rgba(212, 175, 100, 0.15);">
                        <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--gold); letter-spacing: 0.1em; display: block; margin-bottom: 8px;" data-i18n="camp.class12.tag">12. SINIF</span>
                        <h4 style="font-size: 1.3rem; margin-bottom: 16px;" data-i18n="camp.class12.title">Kalifikasyon Aşaması</h4>
                        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; font-size: 0.95rem; color: var(--text-muted);">
                            <li data-i18n="camp.class12.p1"><strong>Metin Analizi:</strong> Karmaşık metinler, Shakespeare.</li>
                            <li data-i18n="camp.class12.p2"><strong>Akademik Yazım:</strong> Yorumlama, Tartışma.</li>
                            <li data-i18n="camp.class12.p3"><strong>Medya & Politika:</strong> Küresel sorunları değerlendirme.</li>
                            <li data-i18n="camp.class12.p4"><strong>Mediasyon:</strong> İçerikleri akıcı aktarma.</li>
                        </ul>
                    </div>
                    <!-- Class 13 -->
                    <div class="glass-card" style="padding: 32px;">
                        <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--gold); letter-spacing: 0.1em; display: block; margin-bottom: 8px;" data-i18n="camp.class13.tag">13. SINIF</span>
                        <h4 style="font-size: 1.3rem; margin-bottom: 16px;" data-i18n="camp.class13.title">Abitur Final Boost</h4>
                        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; font-size: 0.95rem; color: var(--text-muted);">
                            <li data-i18n="camp.class13.p1"><strong>Söylem Analizi:</strong> Retorik analiz.</li>
                            <li data-i18n="camp.class13.p2"><strong>Abitur Writing:</strong> Yapı & Kesinlik.</li>
                            <li data-i18n="camp.class13.p3"><strong>Toplum:</strong> Demokrasiyi eleştirel analiz etme.</li>
                            <li data-i18n="camp.class13.p4"><strong>Argümantasyon:</strong> Karşı argümanları entegre etme.</li>
                        </ul>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 40px;">
                    <a href="#contact" class="btn btn-outline" data-i18n="camp.online.btn">Yaz Kursuna Kaydol</a>
                </div>
            </div>
        </div>
    </section>

    """

# Replace in content
if 'id="wizard"' in html_content:
    # Basic string replace for wizard
    # Need to be careful with formatting, let's just do a clean replace if exact string matches
    # or regex if not matching due to indents
    # I'll use a regex that matches the whole section
    wizard_regex = re.compile(r'<section class="section-padding" id="wizard">.*?(?=</section>)</section>', re.DOTALL)
    html_content = wizard_regex.sub(wizard_new_str.replace('\\', '\\\\'), html_content)
    print("Wizard section replaced successfully.")
else:
    print("Wizard section not found.")

if 'id="camp"' in html_content:
    html_content = camp_regex.sub(camp_new_str.replace('\\', '\\\\'), html_content)
    print("Camp section replaced successfully.")
else:
    print("Camp section not found.")

# Update the script tag to bust cache again (v=4)
html_content = html_content.replace('assets/lang.js?v=3', 'assets/lang.js?v=4')
html_content = html_content.replace('assets/lang.js?v=2', 'assets/lang.js?v=4')
html_content = html_content.replace('assets/lang.js"', 'assets/lang.js?v=4"')


with io.open(index_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML updated.")

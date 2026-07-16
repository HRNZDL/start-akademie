import sys
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix StartBot CSS for light mode
css_old = """.chat-msg.bot {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            color: var(--text);
            align-self: flex-start;
        }"""
css_new = """.chat-msg.bot {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #ffffff !important;
            align-self: flex-start;
        }
        .startbot-window {
            z-index: 999999;
        }
        .chat-msg.bot strong {
            color: var(--gold-light);
        }
        """
html = html.replace(css_old, css_new)

# 2. Add Detailed Nachhilfe Section
nachhilfe_html = """
    <!-- ══════════════════════════════════════════
         NACHHILFE & DEVLET DESTEĞİ DETAYLARI
         ══════════════════════════════════════════ -->
    <section class="section-padding" id="nachhilfe-details" style="background: var(--bg-deep);">
        <div class="container">
            <div style="text-align: center; max-width: 800px; margin: 0 auto 64px;">
                <span class="section-tag" data-i18n="nachhilfe.tag">Start Akademie Almanya</span>
                <h2 data-i18n="nachhilfe.title">Almanya'da Okul Desteği (Nachhilfe)</h2>
                <p style="margin-top: 16px; font-size: 1.05rem;" data-i18n="nachhilfe.desc">Start Akademie, ilkokuldan lise son sınıfa kadar tüm okul türlerine ve ders seviyelerine uygun bireysel destek sağlar. VNN üyesidir ve Kreis Groß-Gerau tarafından resmi olarak tanınmış bir BuT (Bildung und Teilhabe) Ders Desteği Sağlayıcısıdır.</p>
            </div>

            <div class="bento-grid">
                <!-- Eğitim Modellerimiz -->
                <div class="glass-card" style="grid-column: span 2;">
                    <h3 style="font-family: var(--font-serif); font-style: italic; font-size: 1.8rem; margin-bottom: 24px; color: var(--gold-light);">Çocuğunuzu Destekleme Yollarımız</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; color: var(--text-muted);">
                        <div><strong style="color: var(--text);">Einzelunterricht:</strong> Birebir Özel Ders</div>
                        <div><strong style="color: var(--text);">Kleingruppen:</strong> Odaklanmış Küçük Gruplar</div>
                        <div><strong style="color: var(--text);">Tandemunterricht:</strong> İki Öğrenci, Tek Hedef</div>
                        <div><strong style="color: var(--text);">Hausaufgabenbetreuung:</strong> Ev Ödevi Etütü</div>
                        <div><strong style="color: var(--text);">Klausur-Vorbereitung:</strong> Sınav Hazırlığı</div>
                        <div><strong style="color: var(--text);">Regelmäßige Rückmeldung:</strong> Düzenli Veli Geri Bildirimi</div>
                    </div>
                </div>

                <!-- Hausaufgaben-Flat -->
                <div class="glass-card" style="border-color: var(--gold); box-shadow: 0 10px 30px var(--gold-glow);">
                    <h3 style="font-family: var(--font-serif); font-style: italic; font-size: 1.8rem; margin-bottom: 16px;">Hausaufgaben-Flat</h3>
                    <div style="font-size: 2.2rem; color: var(--gold); font-family: var(--font-serif); font-style: italic; margin-bottom: 16px;">150 € <span style="font-size: 1rem; font-family: var(--font-sans); font-style: normal;">/ Ay</span></div>
                    <ul class="card-points" style="margin: 0;">
                        <li>3. - 8. Sınıf Arası</li>
                        <li>Haftada 4 Kez Etüt</li>
                        <li>Ödev Kontrolü & Destek</li>
                    </ul>
                </div>
            </div>

            <!-- BuT Desteği -->
            <div class="glass-card" style="margin-top: 32px; background: rgba(212, 175, 100, 0.03);">
                <div style="display: flex; gap: 32px; align-items: center; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 300px;">
                        <h3 style="font-family: var(--font-serif); font-style: italic; font-size: 2.2rem; color: var(--gold-light); margin-bottom: 16px;">Ücretsiz Nachhilfe & Devlet Desteği (BuT)</h3>
                        <p style="color: var(--text-muted); line-height: 1.8;">Almanya'da devlet, sosyal yardım alan ailelerin çocuklarının ders desteği (Nachhilfe) masraflarını <strong>%100 karşılamaktadır.</strong> Eğer <em>Bürgergeld, Wohngeld, Kinderzuschlag, Sozialhilfe veya Asylbewerberleistungen</em> alıyorsanız, başvuru formunuzu biz dolduruyoruz.</p>
                    </div>
                    <div style="flex: 1; min-width: 300px;">
                        <ol style="color: var(--text-muted); line-height: 1.8; padding-left: 20px;">
                            <li>Belge talebi (Bizden)</li>
                            <li>Formun doldurulması</li>
                            <li>Okul onayı alınması</li>
                            <li>Resmi makama gönderim</li>
                            <li>Onay belgesi teslimi</li>
                            <li>Ücretsiz kayıt</li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Insert nachhilfe_html right after the pillars section
html = html.replace('</section>\n\n    <!-- ══════════════════════════════════════════\n         UNIVERSITIES', '</section>\n' + nachhilfe_html + '\n    <!-- ══════════════════════════════════════════\n         UNIVERSITIES')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Nachhilfe section and CSS fixes applied.")

# -*- coding: utf-8 -*-

with open('konaklama.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update hero
hero_start = html.find('<h1>')
hero_end = html.find('<div class="badge-prep" style="background: rgba(255,165,0,0.12);')

if hero_start != -1 and hero_end != -1:
    new_hero = '<h1>Konaklama, Vize ve <em>İlk Yerleşim</em></h1>\n            <p class="hero-sub">Almanya\'ya gidiş sürecinizde ve oradaki ilk adımlarınızda yanınızdayız.</p>\n            '
    html = html[:hero_start] + new_hero + html[hero_end:]

# Update content
start_marker = '<!-- Konaklama türleri -->'
end_marker = '<!-- CTA -->'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

new_content = '''<!-- Overview -->
    <section class="content-section">
        <div class="container">
            <div style="text-align: center; margin-bottom: 56px;">
                <span class="badge-prep" style="background: rgba(43, 112, 250, 0.1); color: var(--blue); border-color: var(--blue);">Varış Sonrası Hizmetler</span>
                <h2 style="margin-top: 16px;">Sürecin Her Aşamasında <em>Yanınızdayız</em></h2>
            </div>

            <div class="feat-grid" style="grid-template-columns: 1fr; max-width: 800px; margin: 0 auto; gap: 32px;">
                
                <!-- Konaklama -->
                <div class="feat-card glass-card" style="padding: 40px 32px;">
                    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 32px;">
                        <div class="icon-wrap" style="width: 56px; height: 56px; margin: 0; background: var(--blue);"><i data-lucide="home" style="width: 28px; height: 28px;"></i></div>
                        <h3 style="font-size: 1.5rem; margin: 0; color: var(--text);">Konaklama Desteği</h3>
                    </div>
                    
                    <ul class="step-list">
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="building-2" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Öğrenci yurtları</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="users" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">WG (Paylaşımlı ev)</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="key" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Özel daire kiralama</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: none; gap: 16px; align-items: center;">
                            <i data-lucide="hotel" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Geçici konaklama (Airbnb, Hostel vb.)</span>
                        </li>
                    </ul>
                </div>

                <!-- Vize -->
                <div class="feat-card glass-card" style="padding: 40px 32px;">
                    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 32px;">
                        <div class="icon-wrap" style="width: 56px; height: 56px; margin: 0; background: var(--blue);"><i data-lucide="passport" style="width: 28px; height: 28px;"></i></div>
                        <h3 style="font-size: 1.5rem; margin: 0; color: var(--text);">Vize Danışmanlığı</h3>
                    </div>
                    
                    <ul class="step-list">
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="file-text" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Motivasyon mektubu hazırlığı</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="check-circle" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Gerekli evrakların kontrolü</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="shield-check" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Bloke hesap ve sigorta işlemleri</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: none; gap: 16px; align-items: center;">
                            <i data-lucide="landmark" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Konsolosluk süreci takibi</span>
                        </li>
                    </ul>
                </div>

                <!-- İlk Yerleşim -->
                <div class="feat-card glass-card" style="padding: 40px 32px;">
                    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 32px;">
                        <div class="icon-wrap" style="width: 56px; height: 56px; margin: 0; background: var(--blue);"><i data-lucide="map-pin" style="width: 28px; height: 28px;"></i></div>
                        <h3 style="font-size: 1.5rem; margin: 0; color: var(--text);">İlk Yerleşim ve Uyum (Almanya'daki İlk Adımlar)</h3>
                    </div>
                    
                    <ul class="step-list">
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="map" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">İkametgah kaydı (Anmeldung)</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="credit-card" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Banka hesabı açma</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="heart-pulse" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Sağlık sigortası aktivasyonu</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: none; gap: 16px; align-items: center;">
                            <i data-lucide="smartphone" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Telefon hattı ve ulaşım kartı</span>
                        </li>
                    </ul>
                </div>

            </div>
            
            <div style="max-width: 800px; margin: 40px auto 0; padding: 24px 32px; background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border); border-radius: 16px; display: flex; align-items: center; gap: 24px;">
                <i data-lucide="shield" style="color: var(--gold); width: 40px; height: 40px; flex-shrink: 0;"></i>
                <p style="margin: 0; font-size: 1.05rem; color: var(--text); line-height: 1.6;">
                    Danışmanlık hizmetlerimiz sadece Almanya'ya gidiş sürecini değil, oradaki ilk adımlarınızı da güvenle atmanızı kapsar.
                </p>
            </div>
        </div>
    </section>

    '''

html = html[:start_idx] + new_content + html[end_idx:]

with open('konaklama.html', 'w', encoding='utf-8') as f:
    f.write(html)

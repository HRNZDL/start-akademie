# -*- coding: utf-8 -*-

with open('denklik.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- Genel -->'
end_marker = '<!-- CTA -->'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

new_content = '''<!-- Overview -->
    <section class="content-section">
        <div class="container">
            <div style="text-align: center; margin-bottom: 56px;">
                <span class="badge-prep" style="background: rgba(43, 112, 250, 0.1); color: var(--blue); border-color: var(--blue);">Profesyonel Destek</span>
                <h2 style="margin-top: 16px;">Diploma ve Mesleki Tanınma Süreçlerinde <em>Doğru Yol Haritası</em></h2>
            </div>

            <div class="feat-grid" style="grid-template-columns: 1fr; max-width: 800px; margin: 0 auto; gap: 32px;">
                
                <!-- 01 -->
                <div class="feat-card glass-card" style="padding: 32px; display: flex; flex-direction: column; gap: 24px;">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div class="step-num" style="background: var(--blue); color: #fff; width: 56px; height: 56px; font-size: 1.4rem;">01</div>
                        <div class="icon-wrap" style="width: 48px; height: 48px; margin: 0; background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%); color: var(--navy);"><i data-lucide="graduation-cap" style="width: 24px; height: 24px;"></i></div>
                        <h3 style="font-size: 1.4rem; margin: 0; color: var(--text);">OKUL VE AKADEMİK DİPLOMALAR</h3>
                    </div>
                    <ul class="step-list" style="padding-left: 76px;">
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Lise diploması</span></li>
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Açık lise işlemleri</span></li>
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Ön lisans değerlendirmesi</span></li>
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">ZAB süreçleri</span></li>
                    </ul>
                </div>

                <!-- 02 -->
                <div class="feat-card glass-card" style="padding: 32px; display: flex; flex-direction: column; gap: 24px;">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div class="step-num" style="background: var(--blue); color: #fff; width: 56px; height: 56px; font-size: 1.4rem;">02</div>
                        <div class="icon-wrap" style="width: 48px; height: 48px; margin: 0; background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%); color: var(--navy);"><i data-lucide="briefcase" style="width: 24px; height: 24px;"></i></div>
                        <h3 style="font-size: 1.4rem; margin: 0; color: var(--text);">MESLEKİ DENKLİK</h3>
                    </div>
                    <ul class="step-list" style="padding-left: 76px;">
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Meslek lisesi diplomaları</span></li>
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Meslek diplomaları</span></li>
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Kalfalık ve ustalık belgeleri</span></li>
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">İlgili kurum başvuruları</span></li>
                    </ul>
                </div>

                <!-- 03 -->
                <div class="feat-card glass-card" style="padding: 32px; display: flex; flex-direction: column; gap: 24px;">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div class="step-num" style="background: var(--blue); color: #fff; width: 56px; height: 56px; font-size: 1.4rem;">03</div>
                        <div class="icon-wrap" style="width: 48px; height: 48px; margin: 0; background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%); color: var(--navy);"><i data-lucide="users" style="width: 24px; height: 24px;"></i></div>
                        <h3 style="font-size: 1.4rem; margin: 0; color: var(--text);">MESLEĞE ÖZEL BAŞVURULAR</h3>
                    </div>
                    <ul class="step-list" style="padding-left: 76px;">
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Öğretmenlik</span></li>
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Erzieher / Pädagogische Fachkraft</span></li>
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Sosyal hizmet ve sosyal pedagoji</span></li>
                        <li style="padding: 8px 0; border: none; gap: 12px; align-items: center;"><div style="width:6px;height:6px;border-radius:50%;background:var(--gold);"></div><span style="color: var(--text-muted); font-size: 1.05rem;">Sağlık meslekleri</span></li>
                    </ul>
                </div>
            </div>
            
            <div style="max-width: 800px; margin: 40px auto 0; padding: 24px 32px; background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border); border-radius: 16px; display: flex; align-items: center; gap: 24px;">
                <i data-lucide="info" style="color: var(--gold); width: 40px; height: 40px; flex-shrink: 0;"></i>
                <p style="margin: 0; font-size: 1.05rem; color: var(--text); line-height: 1.6;">
                    Denklik süreçleri, mesleğe ve eyalete göre değişebilir. Başvuru yapılacak doğru kurumun belirlenmesi, belgelerin hazırlanması ve sürecin takip edilmesi bu alandaki en önemli adımlardır.
                </p>
            </div>
        </div>
    </section>

    '''

html = html[:start_idx] + new_content + html[end_idx:]

with open('denklik.html', 'w', encoding='utf-8') as f:
    f.write(html)

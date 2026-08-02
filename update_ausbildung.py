# -*- coding: utf-8 -*-

with open('ausbildung.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- Nedir -->'
end_marker = '<!-- Ön talep -->'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

new_content = '''<!-- Overview -->
    <section class="content-section">
        <div class="container">
            <div style="text-align: center; margin-bottom: 56px;">
                <span class="badge-prep" style="background: rgba(43, 112, 250, 0.1); color: var(--blue); border-color: var(--blue);">Ausbildung</span>
                <h2 style="margin-top: 16px;">Almanya'daki Eğitim ve Mesleki Yolunuz İçin <em>Önemli Bir Seçenek</em></h2>
            </div>

            <div class="feat-grid" style="grid-template-columns: 1fr; max-width: 800px; margin: 0 auto; gap: 32px;">
                <div class="feat-card glass-card" style="padding: 40px 32px;">
                    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 32px;">
                        <div class="icon-wrap" style="width: 56px; height: 56px; margin: 0; background: var(--blue);"><i data-lucide="briefcase" style="width: 28px; height: 28px;"></i></div>
                        <h3 style="font-size: 1.5rem; margin: 0; color: var(--text);">Ausbildung Hizmetlerimiz</h3>
                    </div>
                    
                    <ul class="step-list">
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="search" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Uygun meslek alanının belirlenmesi</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="clipboard-list" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Başvuru şartlarının değerlendirilmesi</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="file-text" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Almanca CV ve başvuru dosyası</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="building" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">İşletme ve okul başvuruları</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 16px; align-items: center;">
                            <i data-lucide="users" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Mülakat hazırlığı</span>
                        </li>
                        <li style="padding: 16px 0; border-bottom: none; gap: 16px; align-items: center;">
                            <i data-lucide="plane" style="color: var(--gold); width: 24px; height: 24px; flex-shrink: 0;"></i>
                            <span style="color: var(--text); font-size: 1.05rem;">Ausbildung vizesi sürecine hazırlık</span>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div style="max-width: 800px; margin: 40px auto 0; padding: 24px 32px; background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border); border-radius: 16px; display: flex; align-items: center; gap: 24px;">
                <i data-lucide="target" style="color: var(--gold); width: 40px; height: 40px; flex-shrink: 0;"></i>
                <p style="margin: 0; font-size: 1.05rem; color: var(--text); line-height: 1.6;">
                    Dil seviyesi, eğitim geçmişi ve kariyer hedefleri birlikte değerlendirilerek hangi yolun size daha uygun olduğu belirlenir.
                </p>
            </div>
        </div>
    </section>

    '''

html = html[:start_idx] + new_content + html[end_idx:]

with open('ausbildung.html', 'w', encoding='utf-8') as f:
    f.write(html)

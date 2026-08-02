# -*- coding: utf-8 -*-

with open('degisim.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- Programlar -->'
end_marker = '<!-- Ön talep CTA -->'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

new_content = '''<!-- Programlar -->
    <section class="content-section">
        <div class="container">
            <div style="text-align: center; margin-bottom: 56px;">
                <span class="badge-prep" style="background: rgba(43, 112, 250, 0.1); color: var(--blue); border-color: var(--blue);">Kısa Dönem Deneyimler</span>
                <h2 style="margin-top: 16px;">Kısa Süreli Programlarla <em>Almanya'yı Keşfedin</em></h2>
            </div>

            <div class="feat-grid">
                <div class="feat-card glass-card">
                    <div class="icon-wrap" style="background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%); color: var(--navy);"><i data-lucide="book-open"></i></div>
                    <h3>Erasmus Öğrenim</h3>
                    <p>Almanya'daki üniversitelerde bir veya iki dönem eğitim desteği.</p>
                </div>
                <div class="feat-card glass-card">
                    <div class="icon-wrap" style="background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%); color: var(--navy);"><i data-lucide="briefcase"></i></div>
                    <h3>Erasmus Stajı</h3>
                    <p>Akademik eğitiminizi pratik deneyimle destekleyen staj süreçleri.</p>
                </div>
                <div class="feat-card glass-card">
                    <div class="icon-wrap" style="background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%); color: var(--navy);"><i data-lucide="building"></i></div>
                    <h3>Almanya'da Staj</h3>
                    <p>Bölümünüzle bağlantılı staj başvuruları için danışmanlık ve dosya desteği.</p>
                </div>
                <div class="feat-card glass-card">
                    <div class="icon-wrap" style="background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%); color: var(--navy);"><i data-lucide="sun"></i></div>
                    <h3>Yaz Dönemi Çalışma</h3>
                    <p>Üniversite öğrencileri için kısa dönemli yaz programları ve çalışma seçenekleri.</p>
                </div>
            </div>
            
            <div style="max-width: 800px; margin: 40px auto 0; padding: 24px 32px; background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border); border-radius: 16px; display: flex; align-items: center; gap: 24px;">
                <i data-lucide="info" style="color: var(--gold); width: 40px; height: 40px; flex-shrink: 0;"></i>
                <p style="margin: 0; font-size: 1.05rem; color: var(--text); line-height: 1.6;">
                    Bu alanlardaki hizmet kapsamı programa göre değişebilir. Güncel koşullar, başvuru takvimi ve uygunluk şartları bireysel olarak değerlendirilir.
                </p>
            </div>
        </div>
    </section>

    '''

html = html[:start_idx] + new_content + html[end_idx:]

with open('degisim.html', 'w', encoding='utf-8') as f:
    f.write(html)

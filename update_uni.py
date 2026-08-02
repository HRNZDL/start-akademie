# -*- coding: utf-8 -*-
import re

with open('uni.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace everything between "<!-- Overview -->" and "<!-- FAQ -->" with the new brochure content
start_marker = '<!-- Overview -->'
end_marker = '<!-- FAQ -->'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

new_content = '''<!-- Overview -->
    <section class="content-section">
        <div class="container">
            <div style="text-align: center; margin-bottom: 56px;">
                <span class="badge-prep" style="background: rgba(43, 112, 250, 0.1); color: var(--blue); border-color: var(--blue);">Profesyonel Destek</span>
                <h2 style="margin-top: 16px;">Lisans, Yüksek Lisans ve <em>Studienkolleg</em> Süreçleri</h2>
                <p class="lead-text" style="margin: 0 auto;">Almanya'da üniversiteye giden yol her öğrenci için farklıdır. Eğitim geçmişiniz ve hedefleriniz doğrultusunda en uygun başvuru stratejisi belirlenir.</p>
            </div>

            <div class="feat-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px;">
                <!-- 1. Hangi Alanlarda Destek Veriyoruz? -->
                <div class="feat-card glass-card" style="padding: 40px 32px;">
                    <div class="step-num" style="background: var(--blue); color: #fff; margin-bottom: 24px; width: 48px; height: 48px; font-size: 1.2rem;">1</div>
                    <h3 style="font-size: 1.3rem; margin-bottom: 24px; color: var(--text);">Hangi Alanlarda Destek Veriyoruz?</h3>
                    <ul class="step-list">
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="graduation-cap" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Lisans başvuruları</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="book-open" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Yüksek lisans başvuruları</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="building" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Studienkolleg yönlendirmesi</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="search" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Bölüm ve üniversite seçimi</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: none; gap: 12px;">
                            <i data-lucide="message-square" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Şartlı kabul ve dil yolu değerlendirmesi</span>
                        </li>
                    </ul>
                </div>

                <!-- 2. Başvuru Süreçleri -->
                <div class="feat-card glass-card" style="padding: 40px 32px;">
                    <div class="step-num" style="background: var(--blue); color: #fff; margin-bottom: 24px; width: 48px; height: 48px; font-size: 1.2rem;">2</div>
                    <h3 style="font-size: 1.3rem; margin-bottom: 24px; color: var(--text);">Başvuru Süreçleri</h3>
                    <ul class="step-list">
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="monitor" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">uni-assist ve VPD işlemleri</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="landmark" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Doğrudan üniversite başvuruları</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="folder-check" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Belge kontrolü ve dosya düzeni</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="file-text" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">CV ve motivasyon yazısı desteği</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: none; gap: 12px;">
                            <i data-lucide="check-circle-2" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Eksik belge taleplerinin takibi</span>
                        </li>
                    </ul>
                </div>

                <!-- 3. Kime Uygun? -->
                <div class="feat-card glass-card" style="padding: 40px 32px;">
                    <div class="step-num" style="background: var(--blue); color: #fff; margin-bottom: 24px; width: 48px; height: 48px; font-size: 1.2rem;">3</div>
                    <h3 style="font-size: 1.3rem; margin-bottom: 24px; color: var(--text);">Kime Uygun?</h3>
                    <ul class="step-list">
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="user" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Lise mezunları</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="book" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Açık lise mezunları</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="users" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Üniversite öğrencileri</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); gap: 12px;">
                            <i data-lucide="award" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Ön lisans mezunları</span>
                        </li>
                        <li style="padding: 12px 0; border-bottom: none; gap: 12px;">
                            <i data-lucide="graduation-cap" style="color: var(--gold); flex-shrink: 0;"></i>
                            <span style="color: var(--text-muted); font-size: 0.95rem;">Lisans mezunları</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Badges Section -->
    <section class="content-section alt" style="padding-top: 20px;">
        <div class="container">
            <div class="feat-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px;">
                <div style="display: flex; align-items: center; gap: 16px; padding: 24px; background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 12px;">
                    <i data-lucide="award" style="color: var(--gold); width: 32px; height: 32px; flex-shrink: 0;"></i>
                    <div>
                        <h4 style="margin: 0 0 4px 0; font-size: 1.05rem;">Kişiye Özel Strateji</h4>
                        <p style="margin: 0; font-size: 0.85rem; color: var(--text-muted);">Hedeflerinize uygun planlama</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 16px; padding: 24px; background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 12px;">
                    <i data-lucide="target" style="color: var(--gold); width: 32px; height: 32px; flex-shrink: 0;"></i>
                    <div>
                        <h4 style="margin: 0 0 4px 0; font-size: 1.05rem;">Uzman Danışmanlık</h4>
                        <p style="margin: 0; font-size: 0.85rem; color: var(--text-muted);">Almanya'daki eğitim sistemi hakkında güncel bilgi</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 16px; padding: 24px; background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 12px;">
                    <i data-lucide="shield-check" style="color: var(--gold); width: 32px; height: 32px; flex-shrink: 0;"></i>
                    <div>
                        <h4 style="margin: 0 0 4px 0; font-size: 1.05rem;">Güvenilir Destek</h4>
                        <p style="margin: 0; font-size: 0.85rem; color: var(--text-muted);">Başvurudan kabulünüze kadar yanınızdayız</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    '''

html = html[:start_idx] + new_content + html[end_idx:]

with open('uni.html', 'w', encoding='utf-8') as f:
    f.write(html)

# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace pricing section
start_marker = '    <!-- ══════════════════════════════════════════\n         ÜNİVERSİTE DANIŞMANLIĞI PAKETLERİ'
end_marker = '    <!-- ══════════════════════════════════════════\n         TEKİL VE İLAVE HİZMETLER'

start_idx = html.find('<!-- ══════════════════════════════════════════\n         ÜNİVERSİTE DANIŞMANLIĞI PAKETLERİ')
end_idx = html.find('<!-- ══════════════════════════════════════════\n         TEKİL VE İLAVE HİZMETLER')

if start_idx == -1:
    print("Marker not found - trying alternative search")
    start_idx = html.find('id="pricing"')
    # go back to find the section tag
    start_idx = html.rfind('<section', 0, start_idx)
    end_idx = html.find('<section', start_idx + 10)
    print(f"Found at {start_idx} to {end_idx}")
else:
    # go back to find the comment start
    start_idx = html.rfind('<section', 0, start_idx)
    print(f"Found at {start_idx} to {end_idx}")

new_pricing = '''
    <!-- PRICING SECTION -->
    <section class="section-padding" id="pricing" style="background: var(--surface-hover);">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 64px;">
                <span class="section-tag" data-i18n="price.tag">Paket ve Hizmetler</span>
                <h2 data-i18n="price.title">Üniversite Danışmanlığı Paketleri</h2>
                <p style="margin-top: 16px; font-size: 1.05rem;" data-i18n="price.desc">İhtiyacınıza uygun başvuru ve rehberlik paketleri ile sürecinizi şeffaf bir şekilde yönetiyoruz.</p>
            </div>

            <!-- 3 Main Packages -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 64px;">
                
                <!-- Package 1 -->
                <div class="glass-card" style="padding: 40px 32px; display: flex; flex-direction: column; gap: 16px; border: 1px solid var(--glass-border);">
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                        <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(212,175,55,0.12); display: flex; align-items: center; justify-content: center;">
                            <i data-lucide="graduation-cap" style="width: 22px; height: 22px; color: var(--gold);"></i>
                        </div>
                        <div>
                            <div style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.08em;">Paket 1</div>
                            <h3 style="font-size: 1.05rem; margin: 0;">Üniversite Başvuru Paketi</h3>
                        </div>
                    </div>
                    <div style="font-size: 2.8rem; font-weight: 800; color: var(--gold); line-height: 1; margin: 8px 0;">1.490 <span style="font-size: 1.4rem;">€</span></div>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; flex: 1;">
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Akademik uygunluk değerlendirmesi</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Üniversite ve program araştırması</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> En fazla 3 başvuru</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Belge kontrolü</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> CV ve motivasyon yazısı incelemesi</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> uni-assist / VPD'den doğrudan başvuru desteği</li>
                    </ul>
                    <a href="iletisim.html" class="btn btn-primary" style="margin-top: 16px; text-align: center;">Bilgi Al</a>
                </div>

                <!-- Package 2 -->
                <div class="glass-card" style="padding: 40px 32px; display: flex; flex-direction: column; gap: 16px; border: 2px solid var(--blue); position: relative; overflow: hidden;">
                    <div style="position: absolute; top: 16px; right: 16px; background: var(--blue); color: #fff; font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; padding: 4px 10px; border-radius: 999px;">Popüler</div>
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                        <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(0,80,158,0.12); display: flex; align-items: center; justify-content: center;">
                            <i data-lucide="file-check-2" style="width: 22px; height: 22px; color: var(--blue-light);"></i>
                        </div>
                        <div>
                            <div style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.08em;">Paket 2</div>
                            <h3 style="font-size: 1.05rem; margin: 0;">Başvuru + Dijital Vize Paketi</h3>
                        </div>
                    </div>
                    <div style="font-size: 2.8rem; font-weight: 800; color: var(--blue-light); line-height: 1; margin: 8px 0;">2.290 <span style="font-size: 1.4rem;">€</span></div>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; flex: 1;">
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--blue-light); flex-shrink: 0; margin-top: 2px;"></i> Üniversite Başvuru Paketi kapsamı</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--blue-light); flex-shrink: 0; margin-top: 2px;"></i> En fazla 5 başvuru</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--blue-light); flex-shrink: 0; margin-top: 2px;"></i> Dijital vize evrak listesi</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--blue-light); flex-shrink: 0; margin-top: 2px;"></i> Belge kontrolü ve düzeni</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--blue-light); flex-shrink: 0; margin-top: 2px;"></i> Sisteme yükleme desteği</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--blue-light); flex-shrink: 0; margin-top: 2px;"></i> Randevu öncesi son kontrol</li>
                    </ul>
                    <a href="iletisim.html" class="btn btn-primary" style="margin-top: 16px; text-align: center; background: var(--blue);">Bilgi Al</a>
                </div>

                <!-- Package 3 -->
                <div class="glass-card" style="padding: 40px 32px; display: flex; flex-direction: column; gap: 16px; border: 1px solid var(--glass-border);">
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                        <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(212,175,55,0.12); display: flex; align-items: center; justify-content: center;">
                            <i data-lucide="star" style="width: 22px; height: 22px; color: var(--gold);"></i>
                        </div>
                        <div>
                            <div style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.08em;">Paket 3</div>
                            <h3 style="font-size: 1.05rem; margin: 0;">Tam Süreç Paketi</h3>
                        </div>
                    </div>
                    <div style="font-size: 2.8rem; font-weight: 800; color: var(--gold); line-height: 1; margin: 8px 0;">3.290 <span style="font-size: 1.4rem;">€</span></div>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; flex: 1;">
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Başvuru + dijital vize kapsamı</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> En fazla 7 başvuru</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Dil ve sınav yol haritası</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Konaklama araştırma desteği</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Almanya'ya geliş hazırlığı</li>
                        <li style="display: flex; gap: 10px; align-items: flex-start; font-size: 0.9rem; color: var(--text-muted);"><i data-lucide="check" style="width: 16px; height: 16px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> İlk yerleşim sürecine destek</li>
                    </ul>
                    <a href="iletisim.html" class="btn btn-primary" style="margin-top: 16px; text-align: center;">Bilgi Al</a>
                </div>
            </div>

            <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-top: -32px; margin-bottom: 64px;">* Kesin hizmet kapsamı, öğrencinin dosyasına göre talep belirtildikten sonra özel olarak netleştirilir.</p>

        </div>
    </section>

    <!-- ══════════════════════════════════════════
         TEKİL VE İLAVE HİZMETLER
         ══════════════════════════════════════════ -->
    <section class="section-padding" id="addons">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 48px;">
                <span class="section-tag">Esnek Çözümler</span>
                <h2>Tekil ve İlave Hizmetler</h2>
                <p style="margin-top: 16px;">Sadece ihtiyacınız olan adımlarda yanınızdayız. Yalnızca ihtiyaç duyduğunuz hizmetler için esnek seçenekler.</p>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto;">
                
                <div class="glass-card" style="padding: 28px; display: flex; flex-direction: column; gap: 12px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 40px; height: 40px; border-radius: 10px; background: rgba(0,80,158,0.1); display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="graduation-cap" style="width: 18px; height: 18px; color: var(--blue-light);"></i></div>
                        <div>
                            <div style="font-size: 0.7rem; color: var(--gold); font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em;">1</div>
                            <h4 style="margin: 0; font-size: 0.95rem;">Tek Üniversite veya Program Başvurusu</h4>
                        </div>
                    </div>
                    <div style="font-size: 1.6rem; font-weight: 800; color: var(--text);">450 €</div>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px;">
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Başvuru şartlarının kontrolü</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Belgelerin incelenmesi</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Üniversite portalı işlemleri</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Başvurunun gönderilmesi</li>
                    </ul>
                </div>

                <div class="glass-card" style="padding: 28px; display: flex; flex-direction: column; gap: 12px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 40px; height: 40px; border-radius: 10px; background: rgba(0,80,158,0.1); display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="file-check-2" style="width: 18px; height: 18px; color: var(--blue-light);"></i></div>
                        <div>
                            <div style="font-size: 0.7rem; color: var(--gold); font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em;">2</div>
                            <h4 style="margin: 0; font-size: 0.95rem;">Dijital Vize Başvuru Desteği</h4>
                        </div>
                    </div>
                    <div style="font-size: 1.6rem; font-weight: 800; color: var(--text);">590 €</div>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px;">
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Kişiye özel evrak listesi</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Form incelemesi</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Dijital yükleme desteği</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Son doğrulama kontrolü</li>
                    </ul>
                </div>

                <div class="glass-card" style="padding: 28px; display: flex; flex-direction: column; gap: 12px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 40px; height: 40px; border-radius: 10px; background: rgba(0,80,158,0.1); display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="languages" style="width: 18px; height: 18px; color: var(--blue-light);"></i></div>
                        <div>
                            <div style="font-size: 0.7rem; color: var(--gold); font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em;">3</div>
                            <h4 style="margin: 0; font-size: 0.95rem;">Dil Kursu Başvuru Danışmanlığı</h4>
                        </div>
                    </div>
                    <div style="font-size: 1.6rem; font-weight: 800; color: var(--text);">350 € <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 400;">'dan itibaren</span></div>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px;">
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Seviye ve hedef değerlendirmesi</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Uygun kurs araştırması</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Başvuru desteği</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Kayıt sürecinin takibi</li>
                    </ul>
                </div>

                <div class="glass-card" style="padding: 28px; display: flex; flex-direction: column; gap: 12px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 40px; height: 40px; border-radius: 10px; background: rgba(0,80,158,0.1); display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="briefcase" style="width: 18px; height: 18px; color: var(--blue-light);"></i></div>
                        <div>
                            <div style="font-size: 0.7rem; color: var(--gold); font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em;">4</div>
                            <h4 style="margin: 0; font-size: 0.95rem;">Ausbildung Başvuru Danışmanlığı</h4>
                        </div>
                    </div>
                    <div style="font-size: 1.6rem; font-weight: 800; color: var(--text);">990 € <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 400;">'dan itibaren</span></div>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px;">
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Uygunluk analizi</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> CV ve başvuru dosyası</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> İşletme ve okul araştırması</li>
                        <li style="font-size: 0.82rem; color: var(--text-muted); display: flex; gap: 6px; align-items: flex-start;"><i data-lucide="check" style="width: 14px; height: 14px; color: var(--gold); flex-shrink: 0; margin-top: 2px;"></i> Mülakat hazırlığı</li>
                    </ul>
                </div>

            </div>

            <!-- Other services -->
            <div style="margin-top: 56px;">
                <h3 style="text-align: center; margin-bottom: 32px; font-size: 1.5rem;">Diğer Hizmetler ve Özel Alanlar</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; max-width: 1200px; margin: 0 auto;">
                    
                    <div class="glass-card" style="padding: 24px;">
                        <h5 style="margin: 0 0 4px; font-size: 0.9rem;">Lise ve Akademik Diploma İşlemleri</h5>
                        <div style="font-size: 1.4rem; font-weight: 800; color: var(--gold); margin: 6px 0;">290 € <span style="font-size: 0.65rem; color: var(--text-muted); font-weight: 400;">'dan itibaren</span></div>
                        <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0;">Diploma ve transkript denklik, ZAB süreçleri</p>
                    </div>
                    
                    <div class="glass-card" style="padding: 24px;">
                        <h5 style="margin: 0 0 4px; font-size: 0.9rem;">Mesleki Denklik İşlemleri</h5>
                        <div style="font-size: 1.4rem; font-weight: 800; color: var(--gold); margin: 6px 0;">490 € <span style="font-size: 0.65rem; color: var(--text-muted); font-weight: 400;">'dan itibaren</span></div>
                        <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0;">Meslek lisesi, kalfalık / ustalık belgeleri</p>
                    </div>
                    
                    <div class="glass-card" style="padding: 24px;">
                        <h5 style="margin: 0 0 4px; font-size: 0.9rem;">Mesleğe Özel Denklik İşlemleri</h5>
                        <div style="font-size: 1.4rem; font-weight: 800; color: var(--gold); margin: 6px 0;">490 € <span style="font-size: 0.65rem; color: var(--text-muted); font-weight: 400;">'dan itibaren</span></div>
                        <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0;">Öğretmenlik, sağlık, sosyal hizmet vb.</p>
                    </div>
                    
                    <div class="glass-card" style="padding: 24px;">
                        <h5 style="margin: 0 0 4px; font-size: 0.9rem;">Erasmus Danışmanlığı</h5>
                        <div style="font-size: 1.4rem; font-weight: 800; color: var(--gold); margin: 6px 0;">250 € <span style="font-size: 0.65rem; color: var(--text-muted); font-weight: 400;">'dan itibaren</span></div>
                        <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0;">Erasmus öğrenim ve staj başvuruları</p>
                    </div>
                    
                    <div class="glass-card" style="padding: 24px;">
                        <h5 style="margin: 0 0 4px; font-size: 0.9rem;">Staj ve Yaz Dönemi Çalışma</h5>
                        <div style="font-size: 1.4rem; font-weight: 800; color: var(--gold); margin: 6px 0;">250 € <span style="font-size: 0.65rem; color: var(--text-muted); font-weight: 400;">'dan itibaren</span></div>
                        <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0;">Almanya'da staj ve yaz programı desteği</p>
                    </div>
                    
                    <div class="glass-card" style="padding: 24px;">
                        <h5 style="margin: 0 0 4px; font-size: 0.9rem;">Konaklama Araştırma Desteği</h5>
                        <div style="font-size: 1.4rem; font-weight: 800; color: var(--gold); margin: 6px 0;">290 € <span style="font-size: 0.65rem; color: var(--text-muted); font-weight: 400;">'dan itibaren</span></div>
                        <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0;">Yurt, WG veya özel kira araştırması</p>
                    </div>
                    
                    <div class="glass-card" style="padding: 24px;">
                        <h5 style="margin: 0 0 4px; font-size: 0.9rem;">Almanya'ya Varış ve İlk Yerleşim</h5>
                        <div style="font-size: 1.4rem; font-weight: 800; color: var(--gold); margin: 6px 0;">290 € <span style="font-size: 0.65rem; color: var(--text-muted); font-weight: 400;">'dan itibaren</span></div>
                        <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0;">Anmeldung, banka hesabı, sigorta aktivasyonu</p>
                    </div>

                </div>
            </div>

            <!-- What's included / not included -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; max-width: 900px; margin: 56px auto 0;">
                <div class="glass-card" style="padding: 32px;">
                    <h4 style="margin: 0 0 16px; display: flex; align-items: center; gap: 10px;"><i data-lucide="check-circle" style="width: 22px; height: 22px; color: #4caf50;"></i> Ücretlere Dahil Olanlar</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; font-size: 0.88rem; color: var(--text-muted);">
                        <li>Belirtilen hizmetler için Start Akademie danışmanlık hizmetleri</li>
                    </ul>
                </div>
                <div class="glass-card" style="padding: 32px;">
                    <h4 style="margin: 0 0 16px; display: flex; align-items: center; gap: 10px;"><i data-lucide="x-circle" style="width: 22px; height: 22px; color: #f44336;"></i> Ücretlere Dahil Olmayanlar</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; font-size: 0.88rem; color: var(--text-muted);">
                        <li style="display: flex; gap: 8px;"><i data-lucide="minus" style="width: 14px; height: 14px; color: var(--text-muted); flex-shrink: 0; margin-top: 2px;"></i> Üniversite ve uni-assist başvuru ücretleri</li>
                        <li style="display: flex; gap: 8px;"><i data-lucide="minus" style="width: 14px; height: 14px; color: var(--text-muted); flex-shrink: 0; margin-top: 2px;"></i> Tercüme, noter ve apostil masrafları</li>
                        <li style="display: flex; gap: 8px;"><i data-lucide="minus" style="width: 14px; height: 14px; color: var(--text-muted); flex-shrink: 0; margin-top: 2px;"></i> Vize harcı</li>
                        <li style="display: flex; gap: 8px;"><i data-lucide="minus" style="width: 14px; height: 14px; color: var(--text-muted); flex-shrink: 0; margin-top: 2px;"></i> Bloke hesap için yatırılacak tutar</li>
                        <li style="display: flex; gap: 8px;"><i data-lucide="minus" style="width: 14px; height: 14px; color: var(--text-muted); flex-shrink: 0; margin-top: 2px;"></i> Sağlık sigortası</li>
                        <li style="display: flex; gap: 8px;"><i data-lucide="minus" style="width: 14px; height: 14px; color: var(--text-muted); flex-shrink: 0; margin-top: 2px;"></i> Dil kursu ücretleri</li>
                        <li style="display: flex; gap: 8px;"><i data-lucide="minus" style="width: 14px; height: 14px; color: var(--text-muted); flex-shrink: 0; margin-top: 2px;"></i> Uçuş ve konaklama giderleri</li>
                        <li style="display: flex; gap: 8px;"><i data-lucide="minus" style="width: 14px; height: 14px; color: var(--text-muted); flex-shrink: 0; margin-top: 2px;"></i> Resmi makamların talep ettiği ücretler</li>
                        <li style="display: flex; gap: 8px;"><i data-lucide="minus" style="width: 14px; height: 14px; color: var(--text-muted); flex-shrink: 0; margin-top: 2px;"></i> Diğer üçüncü taraf giderleri</li>
                    </ul>
                </div>
            </div>
            <p style="text-align: center; font-size: 0.82rem; color: var(--text-muted); margin-top: 20px; max-width: 700px; margin-left: auto; margin-right: auto;">Start Akademie; üniversite kabulü, vize sonucu, denklik kararı, Ausbildung yeri, işveren kabulü, staj yeri veya konaklama sonucu konusunda garanti vermez. Bu kararlar ilgili kurumlara ve makamlarına aittir.</p>

        </div>
    </section>

'''

html = html[:start_idx] + new_pricing + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")

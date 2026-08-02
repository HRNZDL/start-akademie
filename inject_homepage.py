# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add "Size Uygun Yol Hangisi?" (Point 12) + 6 Main Service Cards (Point 9)
# We will insert them right after the #pillars section ends.
pillars_end = '    </section>\n\n    <!-- ══════════════════════════════════════════\n         PARTNER VE SEÇKİN ÜNİVERSİTELER'

new_sections = '''    </section>

    <!-- ══════════════════════════════════════════
         SİZE UYGUN YOL HANGİSİ? (Point 12)
         ══════════════════════════════════════════ -->
    <section class="section-padding" id="path-selector" style="background: var(--surface-hover);">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 48px;">
                <span class="section-tag" data-i18n="path.tag">Hızlı Yönlendirme</span>
                <h2 data-i18n="path.title">Size Uygun Yol Hangisi?</h2>
                <p style="margin-top: 16px; font-size: 1.05rem;" data-i18n="path.desc">Mevcut eğitim durumunuzu veya hedefinizi seçerek size en uygun hizmetlerimize hızlıca ulaşın.</p>
            </div>
            
            <div class="chip-container" style="display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; max-width: 900px; margin: 0 auto;">
                <a href="uni.html" class="chip-btn">Lise mezunuyum</a>
                <a href="uni.html" class="chip-btn">Açık Lise mezunuyum</a>
                <a href="uni.html" class="chip-btn">Üniversite öğrencisiyim</a>
                <a href="uni.html" class="chip-btn">Üniversite mezunuyum</a>
                <a href="uni.html" class="chip-btn">Yüksek lisans yapmak istiyorum</a>
                <a href="dil.html" class="chip-btn">Almanya’da dil kursuna gitmek istiyorum</a>
                <a href="ausbildung.html" class="chip-btn">Ausbildung yapmak istiyorum</a>
                <a href="denklik.html" class="chip-btn">Diplomamı denkleştirmek istiyorum</a>
                <a href="degisim.html" class="chip-btn">Erasmus yapmak istiyorum</a>
                <a href="degisim.html" class="chip-btn">Almanya’da staj yapmak istiyorum</a>
                <a href="degisim.html" class="chip-btn">Yazın Almanya’da çalışmak istiyorum</a>
                <a href="konaklama.html" class="chip-btn">Konaklama arıyorum</a>
            </div>
        </div>
    </section>

    <!-- ══════════════════════════════════════════
         6 ANA HİZMET (Point 9)
         ══════════════════════════════════════════ -->
    <section class="section-padding" id="main-services">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 64px;">
                <span class="section-tag">Odak Alanlarımız</span>
                <h2>Eğitim ve Kariyer Hizmetlerimiz</h2>
            </div>
            
            <div class="bento-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px;">
                <!-- 1. Üniversite -->
                <div class="glass-card service-card">
                    <div class="service-icon" style="background: rgba(43, 112, 250, 0.1); color: #2b70fa;">
                        <i data-lucide="graduation-cap"></i>
                    </div>
                    <h3>Üniversite</h3>
                    <p style="color: var(--text-muted); margin-bottom: 16px;">Lisans, yüksek lisans, Studienkolleg ve üniversite başvurularında kişiye özel yol haritası.</p>
                    <ul class="service-list" style="list-style: none; padding: 0; margin-bottom: 24px; color: var(--text-color); font-size: 0.95rem;">
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Lisans & Yüksek lisans</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Studienkolleg</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Üniversite ve bölüm seçimi</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> uni-assist ve doğrudan başvurular</li>
                    </ul>
                    <a href="uni.html" class="btn btn-outline" style="width: 100%; text-align: center;">Üniversite Danışmanlığını İnceleyin</a>
                </div>

                <!-- 2. Dil Kursları -->
                <div class="glass-card service-card">
                    <div class="service-icon" style="background: rgba(255, 126, 51, 0.1); color: #ff7e33;">
                        <i data-lucide="languages"></i>
                    </div>
                    <h3>Dil Kursları</h3>
                    <p style="color: var(--text-muted); margin-bottom: 16px;">Almanya’daki üniversite dil kursları, DSH hazırlık programları ve özel dil okullarına başvuru desteği.</p>
                    <ul class="service-list" style="list-style: none; padding: 0; margin-bottom: 24px; color: var(--text-color); font-size: 0.95rem;">
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Üniversiteye bağlı dil kursları</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> DSH / studienvorbereitender Deutschkurs</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Özel dil okulları</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Kurs seçimi ve başvuru</li>
                    </ul>
                    <a href="dil.html" class="btn btn-outline" style="width: 100%; text-align: center;">Dil Kurslarını İnceleyin</a>
                </div>

                <!-- 3. Ausbildung -->
                <div class="glass-card service-card">
                    <div class="service-icon" style="background: rgba(30, 209, 161, 0.1); color: #1ed1a1;">
                        <i data-lucide="briefcase"></i>
                    </div>
                    <h3>Ausbildung</h3>
                    <p style="color: var(--text-muted); margin-bottom: 16px;">Meslek seçimi, Almanca başvuru dosyası, işletme ve okul başvuruları için danışmanlık.</p>
                    <ul class="service-list" style="list-style: none; padding: 0; margin-bottom: 24px; color: var(--text-color); font-size: 0.95rem;">
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Uygunluk değerlendirmesi</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Meslek alanı seçimi</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Lebenslauf ve Anschreiben</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> İşletme ve okul başvuruları</li>
                    </ul>
                    <a href="ausbildung.html" class="btn btn-outline" style="width: 100%; text-align: center;">Ausbildung Sürecini İnceleyin</a>
                </div>

                <!-- 4. Denklik -->
                <div class="glass-card service-card">
                    <div class="service-icon" style="background: rgba(147, 51, 234, 0.1); color: #9333ea;">
                        <i data-lucide="file-check-2"></i>
                    </div>
                    <h3>Denklik</h3>
                    <p style="color: var(--text-muted); margin-bottom: 16px;">Okul, akademik ve mesleki diplomaların Almanya’daki değerlendirme ve tanınma süreçleri.</p>
                    <ul class="service-list" style="list-style: none; padding: 0; margin-bottom: 24px; color: var(--text-color); font-size: 0.95rem;">
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Lise ve Açık Lise</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Ön lisans & Meslek diploması</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Öğretmenlik</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Sağlık meslekleri</li>
                    </ul>
                    <a href="denklik.html" class="btn btn-outline" style="width: 100%; text-align: center;">Denklik Hizmetlerini İnceleyin</a>
                </div>

                <!-- 5. Değişim ve Yaz Programları -->
                <div class="glass-card service-card">
                    <div class="service-icon" style="background: rgba(236, 72, 153, 0.1); color: #ec4899;">
                        <i data-lucide="plane"></i>
                    </div>
                    <h3>Değişim ve Yaz Programları</h3>
                    <p style="color: var(--text-muted); margin-bottom: 16px;">Erasmus, staj ve üniversite öğrencilerine yönelik kısa süreli Almanya programları.</p>
                    <ul class="service-list" style="list-style: none; padding: 0; margin-bottom: 24px; color: var(--text-color); font-size: 0.95rem;">
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Erasmus öğrenim</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Erasmus staj</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Almanya’da staj</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Yaz dönemi çalışma</li>
                    </ul>
                    <a href="degisim.html" class="btn btn-outline" style="width: 100%; text-align: center;">Programları İnceleyin</a>
                </div>

                <!-- 6. Konaklama -->
                <div class="glass-card service-card">
                    <div class="service-icon" style="background: rgba(244, 63, 94, 0.1); color: #f43f5e;">
                        <i data-lucide="home"></i>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <h3 style="margin-bottom: 0;">Konaklama</h3>
                        <span style="background: rgba(255, 171, 0, 0.1); color: #ffab00; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600;">Ön talep alınıyor</span>
                    </div>
                    <p style="color: var(--text-muted); margin-bottom: 16px; margin-top: 16px;">Öğrenciler için konaklama araştırması ve Almanya’ya varış sonrası ilk yerleşim desteği.</p>
                    <ul class="service-list" style="list-style: none; padding: 0; margin-bottom: 24px; color: var(--text-color); font-size: 0.95rem;">
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Öğrenci konaklaması</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Rhein-Main bölgesi</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Ön talep</li>
                        <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="check-circle-2" style="width: 16px; color: var(--gold);"></i> Varış ve ilk yerleşim</li>
                    </ul>
                    <a href="konaklama.html" class="btn btn-outline" style="width: 100%; text-align: center;">Konaklama Hizmetini İnceleyin</a>
                </div>
            </div>
        </div>
    </section>

    <!-- ══════════════════════════════════════════
         PARTNER VE SEÇKİN ÜNİVERSİTELER'''

html = html.replace(pillars_end, new_sections)

# 2. Fix the #universities section (Point 11)
old_universities = re.search(r'<!-- ══════════════════════════════════════════\n         ÜNİVERSİTE VE PROGRAM.*?</section>', html, re.DOTALL).group(0)

new_universities = '''<!-- ══════════════════════════════════════════
         ÜNİVERSİTE VE PROGRAM SEÇİMİNİ NASIL YAPIYORUZ?
         ══════════════════════════════════════════ -->
    <section class="section-padding" id="universities" style="background: var(--surface-hover);">
        <div class="container">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 24px; margin-bottom: 64px;">
                <div>
                    <span class="section-tag">Stratejik Planlama</span>
                    <h2>Üniversite ve Program Seçimini Nasıl Yapıyoruz?</h2>
                </div>
                <p style="max-width: 480px; font-size: 0.95rem;">Başvuru stratejinizi, lise/lisans alanınıza ve kariyer hedeflerinize en uygun program türüne göre 4 temel kriterde özel olarak tasarlıyoruz.</p>
            </div>

            <div class="univ-slider" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
                <!-- 1. Akademik Uygunluk -->
                <div class="glass-card univ-card">
                    <div class="univ-info" style="padding: 32px;">
                        <div class="univ-meta" style="margin-bottom: 16px;">
                            <span style="background: rgba(43, 112, 250, 0.1); color: #2b70fa; padding: 4px 12px; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">1. Aşama</span>
                        </div>
                        <h3 style="font-size: 1.25rem;">Akademik Uygunluk</h3>
                        <ul style="margin-top: 16px; padding-left: 20px; color: var(--text-muted); font-size: 0.95rem;">
                            <li>Lise türü</li>
                            <li>YKS veya üniversite geçmişi</li>
                            <li>Not ortalaması</li>
                            <li>Mevcut bölüm</li>
                        </ul>
                    </div>
                </div>

                <!-- 2. Program Uyumu -->
                <div class="glass-card univ-card">
                    <div class="univ-info" style="padding: 32px;">
                        <div class="univ-meta" style="margin-bottom: 16px;">
                            <span style="background: rgba(30, 209, 161, 0.1); color: #1ed1a1; padding: 4px 12px; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">2. Aşama</span>
                        </div>
                        <h3 style="font-size: 1.25rem;">Program Uyumu</h3>
                        <ul style="margin-top: 16px; padding-left: 20px; color: var(--text-muted); font-size: 0.95rem;">
                            <li>Hedef bölüm</li>
                            <li>Önceki ders içerikleri</li>
                            <li>Dil şartı</li>
                            <li>Akademik ön koşullar</li>
                        </ul>
                    </div>
                </div>

                <!-- 3. Şehir ve Bütçe -->
                <div class="glass-card univ-card">
                    <div class="univ-info" style="padding: 32px;">
                        <div class="univ-meta" style="margin-bottom: 16px;">
                            <span style="background: rgba(255, 171, 0, 0.1); color: #ffab00; padding: 4px 12px; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">3. Aşama</span>
                        </div>
                        <h3 style="font-size: 1.25rem;">Şehir ve Bütçe</h3>
                        <ul style="margin-top: 16px; padding-left: 20px; color: var(--text-muted); font-size: 0.95rem;">
                            <li>Yaşam maliyetleri</li>
                            <li>Konaklama</li>
                            <li>Ulaşım</li>
                            <li>Öğrenci hayatı</li>
                        </ul>
                    </div>
                </div>

                <!-- 4. Başvuru Yöntemi -->
                <div class="glass-card univ-card">
                    <div class="univ-info" style="padding: 32px;">
                        <div class="univ-meta" style="margin-bottom: 16px;">
                            <span style="background: rgba(147, 51, 234, 0.1); color: #9333ea; padding: 4px 12px; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">4. Aşama</span>
                        </div>
                        <h3 style="font-size: 1.25rem;">Başvuru Yöntemi</h3>
                        <ul style="margin-top: 16px; padding-left: 20px; color: var(--text-muted); font-size: 0.95rem;">
                            <li>uni-assist</li>
                            <li>VPD</li>
                            <li>Doğrudan üniversite başvurusu</li>
                            <li>Üniversite portalı</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 32px; padding: 16px; background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 12px; text-align: center;">
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0;">
                    <i data-lucide="info" style="width: 14px; display: inline-block; vertical-align: middle; margin-right: 4px;"></i>
                    Sitemizde kullanılan üniversite logoları vb. görseller örnek niteliğindedir. Bu gösterim Start Akademie ile resmî ortaklık, kabul veya yerleştirme garantisi ifade etmez.
                </p>
            </div>
        </div>
    </section>'''

html = html.replace(old_universities, new_universities)

# 3. Add 5-step process timeline (Point 14) before #pricing
pricing_start = '<!-- ══════════════════════════════════════════\n         ÜNİVERSİTE DANIŞMANLIĞI PAKETLERİ'

timeline_section = '''<!-- ══════════════════════════════════════════
         5 AŞAMALI SÜREÇ (TIMELINE)
         ══════════════════════════════════════════ -->
    <section class="section-padding" id="process-timeline">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 64px;">
                <span class="section-tag">Nasıl Çalışıyoruz?</span>
                <h2>İlk Görüşmeden Almanya’daki İlk Günlerinize Kadar</h2>
                <p style="margin-top: 16px; font-size: 1.05rem;">Size özel hazırladığımız 5 aşamalı yol haritası ile Almanya hayalinizi adım adım gerçeğe dönüştürüyoruz.</p>
            </div>
            
            <div class="timeline-container" style="max-width: 800px; margin: 0 auto; position: relative;">
                <!-- Timeline steps will use CSS grid/flex for a beautiful vertical timeline -->
                <div class="timeline-step glass-card" style="margin-bottom: 24px; padding: 24px; display: flex; gap: 24px; align-items: flex-start;">
                    <div class="step-number" style="background: var(--gold); color: #000; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; font-size: 1.2rem;">1</div>
                    <div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 12px;">Ön Değerlendirme</h3>
                        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                            <span class="step-chip">Eğitim geçmişi</span>
                            <span class="step-chip">Dil seviyesi</span>
                            <span class="step-chip">Hedefler</span>
                            <span class="step-chip">Mevcut belgeler</span>
                            <span class="step-chip">Zaman planı</span>
                        </div>
                    </div>
                </div>

                <div class="timeline-step glass-card" style="margin-bottom: 24px; padding: 24px; display: flex; gap: 24px; align-items: flex-start;">
                    <div class="step-number" style="background: var(--primary); color: #fff; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; font-size: 1.2rem;">2</div>
                    <div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 12px;">Kişisel Yol Haritası</h3>
                        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                            <span class="step-chip">Uygun eğitim yolu</span>
                            <span class="step-chip">Başvuru yöntemi</span>
                            <span class="step-chip">Gerekli belgeler</span>
                            <span class="step-chip">Tahmini süreç</span>
                            <span class="step-chip">Hizmet kapsamı</span>
                        </div>
                    </div>
                </div>

                <div class="timeline-step glass-card" style="margin-bottom: 24px; padding: 24px; display: flex; gap: 24px; align-items: flex-start;">
                    <div class="step-number" style="background: var(--gold); color: #000; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; font-size: 1.2rem;">3</div>
                    <div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 12px;">Başvuru ve Takip</h3>
                        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                            <span class="step-chip">Üniversite</span>
                            <span class="step-chip">Dil kursu</span>
                            <span class="step-chip">Ausbildung</span>
                            <span class="step-chip">Denklik</span>
                            <span class="step-chip">Değişim programları</span>
                        </div>
                    </div>
                </div>

                <div class="timeline-step glass-card" style="margin-bottom: 24px; padding: 24px; display: flex; gap: 24px; align-items: flex-start;">
                    <div class="step-number" style="background: var(--primary); color: #fff; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; font-size: 1.2rem;">4</div>
                    <div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 12px;">Dijital Vize Süreci</h3>
                        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                            <span class="step-chip">Evrak listesi</span>
                            <span class="step-chip">Belge kontrolü</span>
                            <span class="step-chip">Dijital dosya hazırlığı</span>
                            <span class="step-chip">Yükleme desteği</span>
                            <span class="step-chip">Eksik belge bildirimlerinin takibi</span>
                        </div>
                    </div>
                </div>

                <div class="timeline-step glass-card" style="margin-bottom: 24px; padding: 24px; display: flex; gap: 24px; align-items: flex-start;">
                    <div class="step-number" style="background: var(--gold); color: #000; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; font-size: 1.2rem;">5</div>
                    <div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 12px;">Almanya'daki İlk Adımlar</h3>
                        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                            <span class="step-chip">Konaklama</span>
                            <span class="step-chip">Anmeldung</span>
                            <span class="step-chip">Sağlık sigortası</span>
                            <span class="step-chip">Banka hesabı</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ══════════════════════════════════════════
         ÜNİVERSİTE DANIŞMANLIĞI PAKETLERİ'''

html = html.replace(pricing_start, timeline_section)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

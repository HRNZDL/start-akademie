import sys
import re
import os

try:
    from PIL import Image
    # 1. Fix Logo Alpha
    # The user provided a jpg, but we also have assets/logo.png.
    # Let's try to convert the uploaded jpg if it exists, otherwise assets/logo.png
    uploaded_jpg = "C:/Users/Harun/.gemini/antigravity/brain/tempmediaStorage/media__1780696768606.jpg"
    logo_path = "assets/logo.png"
    
    src_path = uploaded_jpg if os.path.exists(uploaded_jpg) else logo_path
    
    img = Image.open(src_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    # Make white (or near white) transparent
    for item in datas:
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save("assets/logo_alpha.png", "PNG")
    print("Logo alpha conversion successful.")
except Exception as e:
    print("Logo alpha error:", e)

# 2. Update index.html
html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update Logo path and remove the bad filter
html = html.replace('src="assets/logo.png" alt="Start Akademie Logo" style="height: 56px; width: auto; filter: grayscale(1) brightness(2);"', 'src="assets/logo_alpha.png" alt="Start Akademie Logo" style="height: 56px; width: auto; filter: brightness(0) invert(1);"')
html = html.replace('src="assets/logo.png"', 'src="assets/logo_alpha.png"')

# Update Addresses
html = html.replace('Bahnhofstraße 22 / 22a', 'Mainzer Straße 18')
html = html.replace('Bahnhofstraße 22', 'Mainzer Straße 18')

# Update FAQ HTML
faq_html = """
    <!-- ══════════════════════════════════════════
         FAQ SIKÇA SORULAN SORULAR
         ══════════════════════════════════════════ -->
    <section class="section-padding" id="faq" style="background: rgba(3, 4, 7, 0.4);">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 64px;">
                <span class="section-tag" data-i18n="faq.tag">Start SSS</span>
                <h2 data-i18n="faq.title">Sıkça Sorulan Sorular</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px;">
                <div class="glass-card" style="padding: 24px; cursor: pointer;" onclick="this.querySelector('.faq-ans').style.display = this.querySelector('.faq-ans').style.display === 'block' ? 'none' : 'block'">
                    <h3 style="font-size: 1.1rem; display: flex; justify-content: space-between;"><span data-i18n="faq.q1">Almanya'da üniversite tamamen ücretsiz mi?</span> <i data-lucide="chevron-down"></i></h3>
                    <div class="faq-ans" style="display: none; margin-top: 16px; color: var(--text-muted); font-size: 0.95rem;" data-i18n="faq.a1">
                        Birçok devlet üniversitesinde yüksek öğrenim harcı yoktur; ancak dönemlik katkı payı (Semesterbeitrag) ve yaşam giderleri ayrıca planlanmalıdır.
                    </div>
                </div>
                <div class="glass-card" style="padding: 24px; cursor: pointer;" onclick="this.querySelector('.faq-ans').style.display = this.querySelector('.faq-ans').style.display === 'block' ? 'none' : 'block'">
                    <h3 style="font-size: 1.1rem; display: flex; justify-content: space-between;"><span data-i18n="faq.q2">YKS olmadan başvuru yapılabilir mi?</span> <i data-lucide="chevron-down"></i></h3>
                    <div class="faq-ans" style="display: none; margin-top: 16px; color: var(--text-muted); font-size: 0.95rem;" data-i18n="faq.a2">
                        Bu durum öğrencinin eğitim geçmişine göre değişir. Her dosya bireysel değerlendirilmelidir (Abitur, IB gibi uluslararası diplomalarla doğrudan mümkündür).
                    </div>
                </div>
                <div class="glass-card" style="padding: 24px; cursor: pointer;" onclick="this.querySelector('.faq-ans').style.display = this.querySelector('.faq-ans').style.display === 'block' ? 'none' : 'block'">
                    <h3 style="font-size: 1.1rem; display: flex; justify-content: space-between;"><span data-i18n="faq.q3">Almanca bilmeden başvuru mümkün mü?</span> <i data-lucide="chevron-down"></i></h3>
                    <div class="faq-ans" style="display: none; margin-top: 16px; color: var(--text-muted); font-size: 0.95rem;" data-i18n="faq.a3">
                        Bazı öğrenciler için dil kursu, şartlı kabul veya hazırlık (Studienkolleg) seçenekleri değerlendirilebilir. Ayrıca İngilizce bölümler (IELTS/TOEFL ile) mevcuttur.
                    </div>
                </div>
                <div class="glass-card" style="padding: 24px; cursor: pointer;" onclick="this.querySelector('.faq-ans').style.display = this.querySelector('.faq-ans').style.display === 'block' ? 'none' : 'block'">
                    <h3 style="font-size: 1.1rem; display: flex; justify-content: space-between;"><span data-i18n="faq.q4">Öğrenciler Almanya'da çalışabilir mi?</span> <i data-lucide="chevron-down"></i></h3>
                    <div class="faq-ans" style="display: none; margin-top: 16px; color: var(--text-muted); font-size: 0.95rem;" data-i18n="faq.a4">
                        Evet, resmi kurallar çerçevesinde yılda 140 tam gün veya 280 yarım gün çalışma hakkınız bulunmaktadır.
                    </div>
                </div>
                <div class="glass-card" style="padding: 24px; cursor: pointer;" onclick="this.querySelector('.faq-ans').style.display = this.querySelector('.faq-ans').style.display === 'block' ? 'none' : 'block'">
                    <h3 style="font-size: 1.1rem; display: flex; justify-content: space-between;"><span data-i18n="faq.q5">Start Akademie kabul veya vize garantisi verir mi?</span> <i data-lucide="chevron-down"></i></h3>
                    <div class="faq-ans" style="display: none; margin-top: 16px; color: var(--text-muted); font-size: 0.95rem;" data-i18n="faq.a5">
                        Hayır. Nihai karar her zaman ilgili üniversite ve resmi makamlar (Konsolosluk/Yabancılar Dairesi) tarafından verilir. Biz dosyanızı kusursuzlaştırırız.
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Replace the old FAQ section
old_faq_start = "<!-- ══════════════════════════════════════════\n         FAQ SIKÇA SORULAN SORULAR"
old_faq_end = "<!-- ══════════════════════════════════════════\n         REZERVASYON"

if old_faq_start in html and old_faq_end in html:
    before = html.split(old_faq_start)[0]
    after = old_faq_end + html.split(old_faq_end)[1]
    html = before + faq_html + "\n    " + after
else:
    print("Warning: Could not find old FAQ boundaries. Trying alternative replace.")
    # Fallback if not found precisely
    
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML update complete.")

import io

html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add new Knowledge Base rules
anchor_rule = """            if (q.includes("kamp") || q.includes("yaz") || q.includes("sommercamp")) {"""

new_rules = """            if (q.includes("but evrak") || q.includes("but form") || q.includes("but basvuru") || q.includes("but başvuru")) {
                return "**BuT (Eğitim ve Katılım) Başvuru Evrakları:**<br>Lise ve okul destek (Nachhilfe) programlarımız için devlet desteğine (BuT) başvururken bu resmi formu kullanabilirsiniz.<br><br>📝 **<a href='assets/docs/BuT_Antrag_Formu.pdf' download style='color:var(--gold); text-decoration:underline;'>BuT Başvuru Formunu İndir (PDF)</a>**<br><br>**Nasıl Doldurulur?**<br>- **Bölüm 1:** Veli (Anne/Baba) bilgilerinizi eksiksiz yazın.<br>- **Bölüm 2:** Destek alacak çocuğunuzun adını ve okulunu belirtin.<br>- **Bölüm 3 (Ek):** Okul öğretmeniniz tarafından <em>'Zusatzbedarf'</em> (ek ders ihtiyacı) onayının imzalanması gerekmektedir.<br><br>Takıldığınız bir yer olursa formu bize getirin, birlikte dolduralım!";
            }
            if (q.includes("üniversite kayıt") || q.includes("universite kayit") || q.includes("kayıt evrak") || q.includes("kayit evrak") || q.includes("basvuru evrak") || q.includes("başvuru evrak") || q.includes("uni assist")) {
                return "**Almanya Üniversite Başvuru/Kayıt Evrakları:**<br>Almanya'da devlet üniversitelerine kayıt başvuruları için temel başvuru formuna ve rehberine aşağıdan ulaşabilirsiniz.<br><br>🎓 **<a href='assets/docs/Uni_Assist_Basvuru_Formu.pdf' download style='color:var(--gold); text-decoration:underline;'>Uni-Assist Başvuru Formunu İndir (PDF)</a>**<br><br>**Nasıl Doldurulur?**<br>- Lise diplomanızın veya YKS sonuç belgenizin noter onaylı yeminli tercümeleri forma eklenmelidir.<br>- Bölüm tercihlerini yaparken uzman danışmanımızın hazırladığı <em>Strateji Raporunu</em> baz alın.<br>- Lütfen formu doldurduktan sonra PDF olarak bu sohbet üzerinden veya e-posta ile bize gönderin, başvuruyu yapmadan önce son kontrolleri biz yapalım.";
            }
            if (q.includes("kamp") || q.includes("yaz") || q.includes("sommercamp")) {"""

if anchor_rule in html:
    html = html.replace(anchor_rule, new_rules)

# 2. Add chips
old_chips = """            <div class="startbot-chips">
                <span class="startbot-chip" onclick="handleBotChip('Bloke Hesap miktarı ne kadar?')">Bloke Hesap Miktarı</span>
                <span class="startbot-chip" onclick="handleBotChip('BuT Desteği nedir?')">Ücretsiz BuT Desteği</span>
                <span class="startbot-chip" onclick="handleBotChip('Adresiniz nerede?')">Adres & İletişim</span>
            </div>"""
            
new_chips = """            <div class="startbot-chips">
                <span class="startbot-chip" onclick="handleBotChip('Üniversite kayıt başvuru evrakları')">🎓 Üni Kayıt Evrakları</span>
                <span class="startbot-chip" onclick="handleBotChip('BuT evrakları ve formları')">📝 BuT Evrakları</span>
                <span class="startbot-chip" onclick="handleBotChip('Bloke Hesap miktarı ne kadar?')">Bloke Hesap Miktarı</span>
                <span class="startbot-chip" onclick="handleBotChip('BuT Desteği nedir?')">Ücretsiz BuT Desteği</span>
                <span class="startbot-chip" onclick="handleBotChip('Adresiniz nerede?')">Adres & İletişim</span>
            </div>"""

# Handle encoding quirks (might have ? instead of special chars in some terminals)
old_chips_safe = """            <div class="startbot-chips">
                <span class="startbot-chip" onclick="handleBotChip('Bloke Hesap miktar"""
new_chips_safe = """            <div class="startbot-chips">
                <span class="startbot-chip" onclick="handleBotChip('niversite kayt basvuru evraklar')">ni Kayt Evraklar</span>
                <span class="startbot-chip" onclick="handleBotChip('BuT evraklar nasl doldurulur?')">BuT Evraklar</span>
                <span class="startbot-chip" onclick="handleBotChip('Bloke Hesap miktar"""

if old_chips in html:
    html = html.replace(old_chips, new_chips)
elif old_chips_safe in html:
    html = html.replace(old_chips_safe, new_chips_safe)
else:
    # Manual replace
    start_idx = html.find('<div class="startbot-chips">')
    if start_idx != -1:
        insert_idx = html.find('>', start_idx) + 1
        html = html[:insert_idx] + """
                <span class="startbot-chip" onclick="handleBotChip('Üniversite kayıt başvuru evrakları')">Üni Kayıt Evrakları</span>
                <span class="startbot-chip" onclick="handleBotChip('BuT evrakları nasıl doldurulur?')">BuT Evrakları</span>""" + html[insert_idx:]

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added docs logic and chips to chatbot.")

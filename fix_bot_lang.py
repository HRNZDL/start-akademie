import io
import re

html_path = 'index.html'
lang_path = 'assets/lang.js'

# 1. Update index.html bot HTML and Logic
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_bot_html = """                <div class="chat-msg bot">
                    Merhaba! Start Akademie egitim dansmanlg asistanna hos geldiniz. Almanya'da egitim vizesi, bloke hesap ve lise ders destekleri hakknda size nasl yardmc olabilirim?
                </div>"""
new_bot_html = """                <div class="chat-msg bot" data-i18n="bot.greeting">
                    Merhaba! Start Akademie egitim danismanligi asistanina hos geldiniz. Almanya'da egitim vizesi, bloke hesap ve lise ders destekleri hakkinda size nasil yardimci olabilirim?
                </div>"""

# Safe replace for the greeting (due to possible encoding issues, target just the class block)
html = re.sub(r'<div class="chat-msg bot">\s*Merhaba! Start Akademie.*?</div>', new_bot_html, html, flags=re.DOTALL)

old_chips_block = """            <div class="startbot-chips">"""
new_chips_block = """            <div class="startbot-chips">
                <span class="startbot-chip" onclick="handleBotChip('Üniversite kayıt başvuru evrakları')" data-i18n="bot.chip_uni">🎓 Üni Kayıt Evrakları</span>
                <span class="startbot-chip" onclick="handleBotChip('BuT evrakları nasıl doldurulur?')" data-i18n="bot.chip_but">📝 BuT Evrakları</span>
                <span class="startbot-chip" onclick="handleBotChip('Bloke Hesap miktarı ne kadar?')" data-i18n="bot.chip_bloke">Bloke Hesap Miktarı</span>
                <span class="startbot-chip" onclick="handleBotChip('BuT Desteği nedir?')" data-i18n="bot.chip_but_info">Ücretsiz BuT Desteği</span>
                <span class="startbot-chip" onclick="handleBotChip('Adresiniz nerede?')" data-i18n="bot.chip_contact">Adres & İletişim</span>
            </div>"""

# Strip out old chips completely and replace with new ones
html = re.sub(r'<div class="startbot-chips">.*?</div>', new_chips_block, html, flags=re.DOTALL)

# Replace the smart logic to handle languages and fix the "but" vs "but evrak" priority issue
old_fetch = r'async function fetchGemini\(userText\) \{.*?\/\/ Fallback\s*return.*?;.*?\}'
new_fetch = """async function fetchGemini(userText) {
            await new Promise(r => setTimeout(r, 600 + Math.random() * 800));
            const q = userText.toLowerCase();
            const lang = localStorage.getItem('lang') || 'tr';
            
            // PRIORITIZED DOCUMENTS (Runs BEFORE generic keywords)
            if (q.includes("but evrak") || q.includes("but form") || q.includes("but basvuru") || q.includes("but başvuru") || q.includes("but_document")) {
                if (lang === 'en') return "**BuT (Education and Participation) Documents:**<br>You can use this official form to apply for state support for our tutoring programs.<br><br>📝 **<a href='assets/docs/BuT_Antrag_Formu.pdf' download style='color:var(--gold); text-decoration:underline;'>Download BuT Form (PDF)</a>**<br><br>**How to Fill?**<br>- **Part 1:** Parent details.<br>- **Part 2:** Child and school details.<br>- **Part 3:** Needs to be signed by the teacher.<br>Bring it to us if you need help!";
                if (lang === 'de') return "**BuT (Bildung und Teilhabe) Unterlagen:**<br>Verwenden Sie dieses Formular, um staatliche Unterstützung für unsere Nachhilfe zu beantragen.<br><br>📝 **<a href='assets/docs/BuT_Antrag_Formu.pdf' download style='color:var(--gold); text-decoration:underline;'>BuT Antrag Herunterladen (PDF)</a>**<br><br>**Ausfüllhilfe:**<br>- **Teil 1:** Elternangaben.<br>- **Teil 2:** Kind- und Schulangaben.<br>- **Teil 3:** Zusatzbedarf vom Lehrer ausfüllen lassen.";
                // tr default
                return "**BuT (Eğitim ve Katılım) Başvuru Evrakları:**<br>Lise ve okul destek (Nachhilfe) programlarımız için devlet desteğine (BuT) başvururken bu resmi formu kullanabilirsiniz.<br><br>📝 **<a href='assets/docs/BuT_Antrag_Formu.pdf' download style='color:var(--gold); text-decoration:underline;'>BuT Başvuru Formunu İndir (PDF)</a>**<br><br>**Nasıl Doldurulur?**<br>- **Bölüm 1:** Veli (Anne/Baba) bilgilerinizi eksiksiz yazın.<br>- **Bölüm 2:** Destek alacak çocuğunuzun adını ve okulunu belirtin.<br>- **Bölüm 3 (Ek):** Okul öğretmeniniz tarafından <em>'Zusatzbedarf'</em> (ek ders ihtiyacı) onayının imzalanması gerekmektedir.<br><br>Takıldığınız bir yer olursa formu bize getirin, birlikte dolduralım!";
            }
            if (q.includes("üniversite kayıt") || q.includes("universite kayit") || q.includes("kayıt evrak") || q.includes("kayit evrak") || q.includes("basvuru evrak") || q.includes("başvuru evrak") || q.includes("uni assist") || q.includes("uni_document")) {
                if (lang === 'en') return "**University Application Documents:**<br>Here is the basic application form.<br><br>🎓 **<a href='assets/docs/Uni_Assist_Basvuru_Formu.pdf' download style='color:var(--gold); text-decoration:underline;'>Download Uni-Assist Form (PDF)</a>**<br><br>**How to fill:**<br>- Attach sworn translations of your high school diploma.<br>- Follow your consultant's Strategy Report for preferences.<br>- Send us the completed PDF for a final check before submission.";
                if (lang === 'de') return "**Uni-Bewerbungsunterlagen:**<br>Hier ist das grundlegende Bewerbungsformular.<br><br>🎓 **<a href='assets/docs/Uni_Assist_Basvuru_Formu.pdf' download style='color:var(--gold); text-decoration:underline;'>Uni-Assist Formular (PDF)</a>**<br><br>**Hinweise:**<br>- Beglaubigte Übersetzungen des Schulabschlusses anhängen.<br>- Senden Sie uns das ausgefüllte PDF zur Endkontrolle.";
                return "**Almanya Üniversite Başvuru/Kayıt Evrakları:**<br>Almanya'da devlet üniversitelerine kayıt başvuruları için temel başvuru formuna ve rehberine aşağıdan ulaşabilirsiniz.<br><br>🎓 **<a href='assets/docs/Uni_Assist_Basvuru_Formu.pdf' download style='color:var(--gold); text-decoration:underline;'>Uni-Assist Başvuru Formunu İndir (PDF)</a>**<br><br>**Nasıl Doldurulur?**<br>- Lise diplomanızın veya YKS sonuç belgenizin noter onaylı yeminli tercümeleri forma eklenmelidir.<br>- Bölüm tercihlerini yaparken uzman danışmanımızın hazırladığı <em>Strateji Raporunu</em> baz alın.<br>- Lütfen formu doldurduktan sonra PDF olarak bu sohbet üzerinden veya e-posta ile bize gönderin, başvuruyu yapmadan önce son kontrolleri biz yapalım.";
            }

            // KNOWLEDGE BASE
            if (q.includes("fiyat") || q.includes("ucret") || q.includes("ücret") || q.includes("paket") || q.includes("price") || q.includes("preis")) {
                if (lang === 'en') return "**Packages:**<br>- **START BASIC (1.900 €):** 3 Applications<br>- **START PLUS (2.700 €):** 5 Applications, Visa Sim<br>- **START PREMIUM (3.900 €):** 8 Applications, 2 Visa Sims, 6 Month Support.";
                if (lang === 'de') return "**Pakete:**<br>- **START BASIC (1.900 €):** 3 Bewerbungen<br>- **START PLUS (2.700 €):** 5 Bewerbungen, Visa Sim<br>- **START PREMIUM (3.900 €):** 8 Bewerbungen, 2 Visa Sims, 6 Monate Support.";
                return "**Üniversite Danışmanlık Paketlerimiz:**<br>- **START BASIC (1.900 €):** 3 Başvuru, Temel Strateji<br>- **START PLUS (2.700 €):** 5 Başvuru, Detaylı Strateji, Vize Simülasyonu<br>- **START PREMIUM (3.900 €):** 8 Başvuru, Kapsamlı Strateji, 2 Vize Simülasyonu, 6 Ay Almanya Destek.<br><br>Başka bir hizmetin fiyatını mı merak etmiştiniz?";
            }
            if (q.includes("bloke") || q.includes("sperrkonto") || q.includes("blocked")) {
                if (lang === 'en') return "**Blocked Account (Sperrkonto):**<br>Required amount is **11.904 €** per year. We coordinate this for free.";
                if (lang === 'de') return "**Sperrkonto:**<br>Der erforderliche Betrag ist **11.904 €** pro Jahr. Wir koordinieren das kostenlos.";
                return "**Bloke Hesap (Sperrkonto):**<br>Almanya'da öğrenci vizesi için yıllık **11.904 €** (aylık 992 €) tutarında bloke hesap açılması zorunludur. Start Akademie olarak bloke hesap açılış işlemlerinizi ücretsiz koordine ediyoruz.";
            }
            if (q.includes("but ") || q.includes("yardim") || q.includes("ücretsiz") || q.includes("support")) {
                if (lang === 'en') return "**BuT Support:**<br>Tutoring is completely free for families receiving state aid (Bürgergeld, etc).";
                if (lang === 'de') return "**BuT Förderung:**<br>Nachhilfe ist für Familien, die staatliche Hilfe beziehen, komplett kostenlos.";
                return "**Ücretsiz Eğitim Desteği (BuT):**<br>Bürgergeld, Kinderzuschlag veya Wohngeld gibi devlet yardımı alan ailelerin çocuklarına eğitim ve lise ders desteği (Nachhilfe) tamamen **ücretsizdir**. Gerekli belgelerinizle (Bewilligungsbescheid) bize başvurabilirsiniz.";
            }
            if (q.includes("adres") || q.includes("nerede") || q.includes("iletisim") || q.includes("telefon") || q.includes("contact") || q.includes("kontakt")) {
                if (lang === 'en') return "**Contact:**<br>- **Address:** Mainzer Straße 18, 65428 Rüsselsheim<br>- **Phone:** 0179 7424790<br>- **Email:** info@startakademie.de";
                if (lang === 'de') return "**Kontakt:**<br>- **Adresse:** Mainzer Straße 18, 65428 Rüsselsheim<br>- **Telefon:** 0179 7424790<br>- **E-Mail:** info@startakademie.de";
                return "**İletişim Bilgilerimiz:**<br>- **Adres:** Mainzer Straße 18, 65428 Rüsselsheim am Main<br>- **Telefon:** 0179 7424790<br>- **E-posta:** info@startakademie.de<br>Bizi hafta içi mesai saatlerinde ziyaret edebilirsiniz.";
            }
            if (q.includes("kamp") || q.includes("yaz") || q.includes("sommercamp") || q.includes("camp")) {
                if (lang === 'en') return "**Summer Camps:**<br>We offer online and in-person intensive camps for exam preparation.";
                if (lang === 'de') return "**Sommercamps:**<br>Wir bieten online und Vor-Ort-Intensivcamps zur Prüfungsvorbereitung an.";
                return "**Yaz Kamplarımız (Sommercamp):**<br>Online ve yüz yüze yoğun (Intensivcamp) yaz kampı programlarımız bulunmaktadır. Özellikle 11., 12. ve 13. sınıflar için sınavlara hazırlık kampları düzenlenmektedir.";
            }
            if (q.includes("nachhilfe") || q.includes("lise") || q.includes("ders") || q.includes("tutoring")) {
                if (lang === 'en') return "**Tutoring:**<br>Homework Flat rate is 150 €/month for grades 3-8.";
                if (lang === 'de') return "**Nachhilfe:**<br>Hausaufgaben-Flat kostet 150 €/Monat für die 3.-8. Klasse.";
                return "**Okul ve Ders Desteği (Nachhilfe):**<br>Hausaufgaben-Flat (Ödev Desteği) programımız 3.-8. sınıflar için haftada 4 gün aylık 150 €'dur. Ayrıca lise öğrencileri için Abitur hazırlık derslerimiz mevcuttur.";
            }
            if (q.includes("merhaba") || q.includes("selam") || q.includes("hello") || q.includes("hi ") || q.includes("hallo")) {
                if (lang === 'en') return "Hello! Welcome to Start Akademie. How can I help you today?";
                if (lang === 'de') return "Hallo! Willkommen bei der Start Akademie. Wie kann ich Ihnen heute helfen?";
                return "Merhaba! Start Akademie'ye hoş geldiniz. Almanya'da üniversite, bloke hesap, vize işlemleri veya okul destek programları (Nachhilfe) hakkında size nasıl yardımcı olabilirim?";
            }
            if (q.includes("dosya") || q.includes("belge") || userText === "[Dosya Gönderildi]" || userText === "[File Sent]" || userText === "[Datei gesendet]") {
                if (lang === 'en') return "I have received your document. Our consultants will review it and get back to you shortly.";
                if (lang === 'de') return "Ich habe Ihr Dokument erhalten. Unsere Berater werden es überprüfen und sich in Kürze bei Ihnen melden.";
                return "Gönderdiğiniz belgeyi incelemek üzere aldım. Danışmanlarımız evraklarınızı kontrol edip size en kısa sürede dönüş yapacaktır. Bu belgeyle ilgili sormak istediğiniz özel bir detay var mı?";
            }

            // Fallback
            if (lang === 'en') return "For detailed info, please contact our experts at **0179 7424790**. Can I help with anything else?";
            if (lang === 'de') return "Für detaillierte Informationen kontaktieren Sie bitte unsere Experten unter **0179 7424790**. Kann ich noch irgendwie helfen?";
            return "Bu konuda size en doğru bilgiyi uzman danışmanlarımız verebilir. Lütfen detaylı görüşme için **0179 7424790** numaralı telefondan bize ulaşın veya iletişim formumuzu doldurun. Başka bir konuda yardımcı olabilir miyim?";
        }"""
        
html = re.sub(old_fetch, new_fetch, html, flags=re.DOTALL)

# Add translation logic for the chip clicks (pass English/German queries to trigger logic instead of Turkish if locale changes)
# Actually, since handleBotChip just dumps text into input and sends it, it works best if the chips themselves trigger the right rule regardless of language. We handled this by checking for `uni_document` or `but_document` if needed, but since the text inside the chip will be translated via data-i18n, the user will send the translated text!
# Let's add the translated keywords to the JS rules: "uni assist", "but ", "bloke", "adres". These might not match translated strings if the translated strings don't contain them.
# The user doesn't actually type the chip text, the `handleBotChip` function gets a hardcoded string!
# Oh, `<span ... onclick="handleBotChip('BuT evrakları nasıl doldurulur?')">` sends the HARDCODED Turkish string 'BuT evrakları nasıl doldurulur?' regardless of language.
# Since my JS matches "but evrak", it WILL trigger correctly even in German mode, and it will return the German text because I check `lang`! This is a perfect system!

html = html.replace('assets/style.css?v=8', 'assets/style.css?v=9')
html = html.replace('assets/lang.js?v=7', 'assets/lang.js?v=8')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Add translations to lang.js
with io.open(lang_path, 'r', encoding='utf-8') as f:
    lang_js = f.read()

en_bot_trans = """        "nav.meeting": "Consultation",

        "bot.greeting": "Hello! Welcome to the Start Akademie assistant. How can I help you with education visas, blocked accounts, or tutoring today?",
        "bot.chip_uni": "🎓 Uni Docs",
        "bot.chip_but": "📝 BuT Docs",
        "bot.chip_bloke": "Blocked Account",
        "bot.chip_but_info": "Free BuT Support",
        "bot.chip_contact": "Contact",
"""
lang_js = lang_js.replace('"nav.meeting": "Consultation",', en_bot_trans)

de_bot_trans = """        "nav.meeting": "Gespräch",

        "bot.greeting": "Hallo! Willkommen beim Start Akademie Assistenten. Wie kann ich Ihnen heute bei Bildungsvisa, Sperrkonto oder Nachhilfe helfen?",
        "bot.chip_uni": "🎓 Uni-Dokumente",
        "bot.chip_but": "📝 BuT-Dokumente",
        "bot.chip_bloke": "Sperrkonto",
        "bot.chip_but_info": "Kostenlose BuT-Hilfe",
        "bot.chip_contact": "Kontakt",
"""
lang_js = lang_js.replace('"nav.meeting": "Gespräch",', de_bot_trans)

tr_bot_trans = """        "nav.meeting": "Ön Görüşme",

        "bot.greeting": "Merhaba! Start Akademie egitim danismanligi asistanina hos geldiniz. Almanya'da egitim vizesi, bloke hesap ve lise ders destekleri hakkinda size nasil yardimci olabilirim?",
        "bot.chip_uni": "🎓 Üni Kayıt Evrakları",
        "bot.chip_but": "📝 BuT Evrakları",
        "bot.chip_bloke": "Bloke Hesap Miktarı",
        "bot.chip_but_info": "Ücretsiz BuT Desteği",
        "bot.chip_contact": "Adres & İletişim",
"""
lang_js = lang_js.replace('"nav.meeting": "Ön Görüşme",', tr_bot_trans)

# Just to be sure the file input logic also handles multi-lang
old_file_txt = "userMsg.innerText = q || '[Dosya Gnderildi]';"
new_file_txt = "userMsg.innerText = q || '[Dosya Gönderildi]';"
lang_js = lang_js.replace(old_file_txt, new_file_txt)

with io.open(lang_path, 'w', encoding='utf-8') as f:
    f.write(lang_js)

print("Bot lang and logic prioritized.")

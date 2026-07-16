import io
import re

html_path = 'index.html'
css_path = 'assets/style.css'

# 1. UPDATE JS LOGIC IN INDEX.HTML
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the fetchGemini function with a Smart Offline Bot logic
fetch_gemini_start = "async function fetchGemini(userText) {"
fetch_gemini_end = "async function sendBotMsg() {"

if fetch_gemini_start in html and fetch_gemini_end in html:
    part1 = html.split(fetch_gemini_start)[0]
    part2 = html.split(fetch_gemini_end)[1]
    
    smart_bot_logic = """async function fetchGemini(userText) {
            // Simulated network delay for realism
            await new Promise(r => setTimeout(r, 600 + Math.random() * 800));
            
            const q = userText.toLowerCase();
            
            // Knowledge Base Rules
            if (q.includes("fiyat") || q.includes("ucret") || q.includes("ücret") || q.includes("paket")) {
                return "**Üniversite Danışmanlık Paketlerimiz:**<br>- **START BASIC (1.900 €):** 3 Başvuru, Temel Strateji<br>- **START PLUS (2.700 €):** 5 Başvuru, Detaylı Strateji, Vize Simülasyonu<br>- **START PREMIUM (3.900 €):** 8 Başvuru, Kapsamlı Strateji, 2 Vize Simülasyonu, 6 Ay Almanya Destek.<br><br>Başka bir hizmetin fiyatını mı merak etmiştiniz?";
            }
            if (q.includes("bloke") || q.includes("sperrkonto")) {
                return "**Bloke Hesap (Sperrkonto):**<br>Almanya'da öğrenci vizesi için yıllık **11.904 €** (aylık 992 €) tutarında bloke hesap açılması zorunludur. Start Akademie olarak bloke hesap açılış işlemlerinizi ücretsiz koordine ediyoruz.";
            }
            if (q.includes("but ") || q.includes("yardim") || q.includes("ücretsiz")) {
                return "**Ücretsiz Eğitim Desteği (BuT):**<br>Bürgergeld, Kinderzuschlag veya Wohngeld gibi devlet yardımı alan ailelerin çocuklarına eğitim ve lise ders desteği (Nachhilfe) tamamen **ücretsizdir**. Gerekli belgelerinizle (Bewilligungsbescheid) bize başvurabilirsiniz.";
            }
            if (q.includes("adres") || q.includes("nerede") || q.includes("iletisim") || q.includes("iletişim") || q.includes("telefon")) {
                return "**İletişim Bilgilerimiz:**<br>- **Adres:** Mainzer Straße 18, 65428 Rüsselsheim am Main<br>- **Telefon:** 0179 7424790<br>- **E-posta:** info@startakademie.de<br>Bizi hafta içi mesai saatlerinde ziyaret edebilirsiniz.";
            }
            if (q.includes("kamp") || q.includes("yaz") || q.includes("sommercamp")) {
                return "**Yaz Kamplarımız (Sommercamp):**<br>Online ve yüz yüze yoğun (Intensivcamp) yaz kampı programlarımız bulunmaktadır. Özellikle 11., 12. ve 13. sınıflar için sınavlara hazırlık kampları düzenlenmektedir.";
            }
            if (q.includes("nachhilfe") || q.includes("lise") || q.includes("ders")) {
                return "**Okul ve Ders Desteği (Nachhilfe):**<br>Hausaufgaben-Flat (Ödev Desteği) programımız 3.-8. sınıflar için haftada 4 gün aylık 150 €'dur. Ayrıca lise öğrencileri için Abitur hazırlık derslerimiz mevcuttur.";
            }
            if (q.includes("merhaba") || q.includes("selam")) {
                return "Merhaba! Start Akademie'ye hoş geldiniz. Almanya'da üniversite, bloke hesap, vize işlemleri veya okul destek programları (Nachhilfe) hakkında size nasıl yardımcı olabilirim?";
            }
            if (q.includes("dosya") || q.includes("belge") || userText === "[Dosya Gönderildi]") {
                return "Gönderdiğiniz belgeyi incelemek üzere aldım. Danışmanlarımız evraklarınızı kontrol edip size en kısa sürede dönüş yapacaktır. Bu belgeyle ilgili sormak istediğiniz özel bir detay var mı?";
            }

            // Fallback
            return "Bu konuda size en doğru bilgiyi uzman danışmanlarımız verebilir. Lütfen detaylı görüşme için **0179 7424790** numaralı telefondan bize ulaşın veya iletişim formumuzu doldurun. Başka bir konuda yardımcı olabilir miyim?";
        }

        async function sendBotMsg() {"""
    
    html = part1 + smart_bot_logic + part2

# Add Auto-Greeting logic
auto_greeting_js = """        let hasGreeted = false;
        function toggleStartbot() {
            if (startbotWin) {
                startbotWin.classList.toggle('active');
                hasGreeted = true; // User manually opened it
            }
        }
        
        // Auto-greet after 6 seconds if not already opened
        setTimeout(() => {
            if (!hasGreeted && startbotWin && !startbotWin.classList.contains('active')) {
                toggleStartbot();
                // Play a subtle notification sound if possible or just open
            }
        }, 6000);"""

if "function toggleStartbot() {\n            if (startbotWin) startbotWin.classList.toggle('active');\n        }" in html:
    html = html.replace("function toggleStartbot() {\n            if (startbotWin) startbotWin.classList.toggle('active');\n        }", auto_greeting_js)


with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. UPDATE CSS UI IN STYLE.CSS
with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .startbot-window logic to support Light & Dark Mode Glassmorphism
old_window = """        .startbot-window {
            position: absolute;
            bottom: 80px;
            right: 0;
            width: 360px;
            height: 480px;
            background: rgba(7, 8, 13, 0.95);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6);
            display: none;
            flex-direction: column;
            overflow: hidden;
            backdrop-filter: blur(20px);
        }"""
        
new_window = """        /* --- PREMIUM CHATBOT UI --- */
        .startbot-window {
            position: absolute;
            bottom: 80px;
            right: 0;
            width: 360px;
            height: 480px;
            /* Premium Dark Mode Glass */
            background: rgba(18, 18, 22, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;
            display: none;
            flex-direction: column;
            overflow: hidden;
            backdrop-filter: blur(30px) saturate(150%);
            -webkit-backdrop-filter: blur(30px) saturate(150%);
            z-index: 999999;
            transform: translateY(20px);
            opacity: 0;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        .startbot-window.active {
            display: flex;
            transform: translateY(0);
            opacity: 1;
            animation: botSlideIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        @keyframes botSlideIn {
            0% { transform: translateY(20px) scale(0.95); opacity: 0; }
            100% { transform: translateY(0) scale(1); opacity: 1; }
        }

        /* Light Mode Overrides for Startbot */
        :root[data-theme="light"] .startbot-window {
            background: rgba(255, 255, 255, 0.75);
            border: 1px solid rgba(0, 0, 0, 0.1);
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.15), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
        }
        :root[data-theme="light"] .startbot-header {
            background: rgba(0, 0, 0, 0.03);
            border-bottom: 1px solid rgba(0, 0, 0, 0.06);
        }
        :root[data-theme="light"] .startbot-header button {
            color: #666;
        }
        :root[data-theme="light"] .chat-msg.bot {
            background: #ffffff;
            border: 1px solid rgba(0, 0, 0, 0.08);
            color: #1a1a1c !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        :root[data-theme="light"] .chat-msg.bot strong {
            color: var(--gold);
        }
        :root[data-theme="light"] .startbot-chips {
            border-top: 1px solid rgba(0, 0, 0, 0.06);
        }
        :root[data-theme="light"] .startbot-chip {
            background: #ffffff;
            border: 1px solid rgba(0,0,0,0.1);
            color: #333;
        }
        :root[data-theme="light"] .startbot-chip:hover {
            background: var(--gold);
            color: #fff;
            border-color: var(--gold);
        }
        :root[data-theme="light"] .startbot-input {
            border-top: 1px solid rgba(0, 0, 0, 0.06);
        }
        :root[data-theme="light"] .startbot-input input {
            background: #ffffff;
            border: 1px solid rgba(0, 0, 0, 0.1);
            color: #1a1a1c;
        }
        :root[data-theme="light"] .startbot-input input:focus {
            border-color: var(--gold);
            box-shadow: 0 0 0 2px rgba(212, 175, 100, 0.2);
        }"""
        
css = css.replace(old_window, new_window)

# Fix dark mode input focus border
old_input = """        .startbot-input input {
            flex-grow: 1;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 6px;
            padding: 10px 14px;
            color: var(--text);
            font-family: var(--font-display);
            font-size: 0.88rem;
            outline: none;
        }"""
new_input = """        .startbot-input input {
            flex-grow: 1;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 6px;
            padding: 10px 14px;
            color: var(--text);
            font-family: var(--font-display);
            font-size: 0.88rem;
            outline: none;
            transition: all 0.3s;
        }
        .startbot-input input:focus {
            border-color: var(--gold);
            box-shadow: 0 0 0 2px rgba(212, 175, 100, 0.2);
        }"""
css = css.replace(old_input, new_input)

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Cache bust
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/style.css?v=5', 'assets/style.css?v=6')
with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Chatbot logic and UI completely upgraded.")

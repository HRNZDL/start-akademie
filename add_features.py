import sys
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add SEO JSON-LD before </head>
seo_json = """
    <!-- JSON-LD SEO / AEO / GEO -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "EducationalOrganization",
      "name": "Start Akademie UG",
      "description": "Frankfurt yakınlarında yerleşik elite ders desteği (Nachhilfe), dil okulu ve Almanya Devlet Üniversiteleri Kabul Danışmanlık Portalı.",
      "url": "https://www.startakademie.de",
      "logo": "https://www.startakademie.de/assets/logo.png",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Bahnhofstraße 22",
        "addressLocality": "Rüsselsheim am Main",
        "postalCode": "65428",
        "addressCountry": "DE"
      },
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+49-179-7424790",
        "contactType": "customer service",
        "email": "info@startakademie.de"
      },
      "founder": {
        "@type": "Person",
        "name": "Mevlüt Uysal"
      }
    }
    </script>
</head>"""
html = html.replace('</head>', seo_json)

# 2. Add FAQ Section right before the contact section
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
                    <h3 style="font-size: 1.1rem; display: flex; justify-content: space-between;"><span data-i18n="faq.q1">BuT (Bildung und Teilhabe) desteği kimleri kapsar?</span> <i data-lucide="chevron-down"></i></h3>
                    <div class="faq-ans" style="display: none; margin-top: 16px; color: var(--text-muted); font-size: 0.95rem;" data-i18n="faq.a1">
                        Bürgergeld, Wohngeld, Kinderzuschlag, Sozialhilfe veya Asylbewerberleistungen alan ailelerin çocukları için Nachhilfe ücretleri devlet tarafından %100 karşılanmaktadır.
                    </div>
                </div>
                <div class="glass-card" style="padding: 24px; cursor: pointer;" onclick="this.querySelector('.faq-ans').style.display = this.querySelector('.faq-ans').style.display === 'block' ? 'none' : 'block'">
                    <h3 style="font-size: 1.1rem; display: flex; justify-content: space-between;"><span data-i18n="faq.q2">Bloke hesap (Sperrkonto) ne kadardır?</span> <i data-lucide="chevron-down"></i></h3>
                    <div class="faq-ans" style="display: none; margin-top: 16px; color: var(--text-muted); font-size: 0.95rem;" data-i18n="faq.a2">
                        2026 yılı için Almanya öğrenci vizesi bloke hesap tutarı yıllık 11.904 € (aylık 992 €) olarak belirlenmiştir. Bu süreçte tüm kurulum desteğini sağlıyoruz.
                    </div>
                </div>
                <div class="glass-card" style="padding: 24px; cursor: pointer;" onclick="this.querySelector('.faq-ans').style.display = this.querySelector('.faq-ans').style.display === 'block' ? 'none' : 'block'">
                    <h3 style="font-size: 1.1rem; display: flex; justify-content: space-between;"><span data-i18n="faq.q3">Lise diplomam (YKS) olmadan Almanya'da üniversite okuyabilir miyim?</span> <i data-lucide="chevron-down"></i></h3>
                    <div class="faq-ans" style="display: none; margin-top: 16px; color: var(--text-muted); font-size: 0.95rem;" data-i18n="faq.a3">
                        Genel kural olarak Türkiye'de YKS ile 4 yıllık bir bölüme yerleşmiş olmanız gerekir. Ancak IB, Abitur gibi uluslararası diplomalarla veya Studienkolleg (Hazırlık Yılı) ile doğrudan başvuru yapılabilmektedir.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ══════════════════════════════════════════
         REZERVASYON VE İLETİŞİM FORMU
"""
html = html.replace('<!-- ══════════════════════════════════════════\n         REZERVASYON VE İLETİŞİM FORMU', faq_html)

# 3. Replace Chatbot HTML
chatbot_old = """            <div class="startbot-input">
                <input type="text" placeholder="Sorunuzu buraya yazın..." id="startbot-text">
                <button onclick="sendBotMsg()"><i data-lucide="send"></i></button>
            </div>"""
chatbot_new = """            <div class="startbot-input" style="display: flex; align-items: center; gap: 8px; position: relative;">
                <label for="startbot-file" style="cursor: pointer; color: var(--text-muted); padding: 8px;" title="Belge Yükle">
                    <i data-lucide="paperclip"></i>
                </label>
                <input type="file" id="startbot-file" style="display: none;" accept="image/*,application/pdf">
                <div id="file-indicator" style="display:none; position:absolute; top:-25px; left:10px; background:var(--gold); color:black; font-size:0.7rem; padding:2px 6px; border-radius:4px; font-weight:600;">Dosya Eklendi ✓</div>
                
                <input type="text" placeholder="Sorunuzu buraya yazın..." id="startbot-text" style="flex-grow:1; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px; color:#fff;" onkeypress="if(event.key === 'Enter') sendBotMsg()">
                <button onclick="sendBotMsg()" style="background:var(--gold); color:black; border:none; border-radius:6px; padding:10px; cursor:pointer;"><i data-lucide="send"></i></button>
            </div>"""
html = html.replace(chatbot_old, chatbot_new)

# 4. Replace Chatbot JS
js_old_regex = r"function handleBotChip\(query\) \{.*?(?=// Custom time picker selection)"
js_new = """function handleBotChip(query) {
            document.getElementById('startbot-text').value = query;
            sendBotMsg();
        }

        let selectedFileBase64 = null;
        let selectedFileMime = null;
        const fileInput = document.getElementById('startbot-file');
        const fileIndicator = document.getElementById('file-indicator');

        if(fileInput) {
            fileInput.addEventListener('change', function(e) {
                const file = e.target.files[0];
                if (!file) {
                    selectedFileBase64 = null;
                    selectedFileMime = null;
                    fileIndicator.style.display = 'none';
                    return;
                }
                const reader = new FileReader();
                reader.onload = function(event) {
                    selectedFileBase64 = event.target.result.split(',')[1];
                    selectedFileMime = file.type;
                    fileIndicator.style.display = 'block';
                };
                reader.readAsDataURL(file);
            });
        }

        async function fetchGemini(userText) {
            const API_KEY = 'AIzaSyAWbzSlT9FwebC88-0_5XFaQaJOhmHQSwk'; // Inserted via Script
            const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}`;
            
            const systemPrompt = `Sen Start Akademie adlı eğitim kurumunun akıllı asistanı StartAgent'sın.
Kurum adresi: Bahnhofstraße 22 / 22a, 65428 Rüsselsheim am Main. Telefon: 0179 7424790. E-posta: info@startakademie.de
Genel Müdür: Mevlüt Uysal.
Hizmetlerimiz:
1) Almanya'da Okul Desteği (Nachhilfe): İlkokuldan lise sona kadar tüm dersler. Devlet BuT (Bildung und Teilhabe) onayıyla vatandaşlık yardımı alan ailelerin çocukları için ücretsiz.
2) Almanya Üniversite Danışmanlığı: YKS puanı ile veya Abitur/IB ile devlet üniversitelerine başvuru. Vize sıfır red politikası.
3) Çevrimiçi Dil Kursları: A1-C1 Almanca ve İngilizce.
4) Yaz Kampı 2026: 06.07.2026 - 31.07.2026 arası Abitur lise İngilizce.

Lütfen kısa, nazik, net ve profesyonel Türkçe cevaplar ver. Kullanıcının dilini algılarsan o dilde cevap verebilirsin. Eğer resim veya PDF yüklenirse onu incele ve yorumla.`;

            let contents;
            if (selectedFileBase64) {
                contents = [{
                    "role": "user",
                    "parts": [
                        {"text": systemPrompt + "\\n\\nKullanıcı sorusu: " + userText},
                        {
                            "inlineData": {
                                "mimeType": selectedFileMime,
                                "data": selectedFileBase64
                            }
                        }
                    ]
                }];
                // Reset file after sending
                selectedFileBase64 = null;
                selectedFileMime = null;
                fileIndicator.style.display = 'none';
                fileInput.value = '';
            } else {
                contents = [{
                    "role": "user",
                    "parts": [{"text": systemPrompt + "\\n\\nKullanıcı sorusu: " + userText}]
                }];
            }

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ contents: contents })
                });
                
                const data = await response.json();
                if (data.candidates && data.candidates[0].content.parts[0].text) {
                    return data.candidates[0].content.parts[0].text;
                }
                return "Üzgünüm, şu an bağlantı kuramıyorum. Lütfen 0179 7424790 numaralı telefondan bize ulaşın.";
            } catch (err) {
                console.error(err);
                return "Bir bağlantı hatası oluştu. Eğitim uzmanlarımız size 0179 7424790 numarası üzerinden yardımcı olabilir.";
            }
        }

        async function sendBotMsg() {
            const txt = document.getElementById('startbot-text');
            const q = txt.value.trim();
            if (!q && !selectedFileBase64) return;

            txt.value = '';
            const chatMessages = document.getElementById('startbot-messages');
            
            // Add user message
            const userMsg = document.createElement('div');
            userMsg.className = 'chat-msg user';
            userMsg.innerText = q || '[Dosya Gönderildi]';
            chatMessages.appendChild(userMsg);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            // Add typing indicator
            const typingMsg = document.createElement('div');
            typingMsg.className = 'chat-msg bot';
            typingMsg.innerHTML = '<span class="pulse-dot" style="display:inline-block;"></span> StartAgent yazıyor...';
            chatMessages.appendChild(typingMsg);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            // Fetch AI Response
            const answer = await fetchGemini(q);
            
            // Replace typing with actual answer
            typingMsg.innerHTML = '';
            // Process basic markdown bold to HTML
            typingMsg.innerHTML = answer.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>').replace(/\\n/g, '<br>');
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        """

html = re.sub(js_old_regex, js_new, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML modifications completed.")

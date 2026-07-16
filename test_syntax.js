
        // Init Lucide Icons
        lucide.createIcons();

        // ══════════════════════════════════════════
        // HEADER: scroll shrink + gold border
        // ══════════════════════════════════════════
        const mainHeader = document.getElementById('main-header');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 60) {
                mainHeader.classList.add('scrolled');
            } else {
                mainHeader.classList.remove('scrolled');
            }

            // Active nav tracking
            const sections = document.querySelectorAll('section[id]');
            let current = '';
            sections.forEach(s => {
                if (window.scrollY >= s.offsetTop - 140) current = s.id;
            });
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + current) link.classList.add('active');
            });
        }, { passive: true });

        // ══════════════════════════════════════════
        // SCROLL REVEAL — fade-up all sections
        // ══════════════════════════════════════════
        const revealItems = document.querySelectorAll(
            '.section-padding .glass-card, .section-padding .section-tag, .bento-card, .univ-card, .price-card, .camp-timeline > *, .booking-layout > *'
        );
        revealItems.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
        });

        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry, i) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, 80 * (i % 4));
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });
        revealItems.forEach(el => revealObserver.observe(el));

        // Mobile toggle
        const mobToggle = document.getElementById('mobile-toggle');
        const mobDrawer = document.getElementById('mobile-menu-drawer');
        if (mobToggle && mobDrawer) {
            mobToggle.addEventListener('click', () => {
                mobDrawer.classList.toggle('open');
                const icon = mobToggle.querySelector('i');
                if (icon) {
                    if (mobDrawer.classList.contains('open')) {
                        icon.setAttribute('data-lucide', 'x');
                    } else {
                        icon.setAttribute('data-lucide', 'menu');
                    }
                    lucide.createIcons();
                }
            });
        }

        // Native smooth scrolling is handled by CSS (scroll-behavior: smooth)

        // ══════════════════════════════════════════
        // INTERACTIVE CALCULATOR
        // ══════════════════════════════════════════
        const sliderMonths = document.getElementById('slider-months');
        const sliderExtra = document.getElementById('slider-extra');
        
        const labelMonths = document.getElementById('label-months');
        const labelExtra = document.getElementById('label-extra');

        const calcTotal = document.getElementById('calc-total');
        const valMonthly = document.getElementById('val-monthly');
        const valTotalSperr = document.getElementById('val-total-sperr');
        const valFees = document.getElementById('val-fees');

        const barSperr = document.getElementById('bar-sperrkonto');
        const barFee = document.getElementById('bar-fee');

        function updateCalculator() {
            const months = parseInt(sliderMonths.value);
            const extra = parseInt(sliderExtra.value);

            labelMonths.innerText = `${months} Ay`;
            labelExtra.innerText = `${extra} €`;

            const officialMonthly = 992;
            const userMonthly = officialMonthly + extra;
            const totalSperr = userMonthly * months;
            const setupFee = 99; // standard setup fee
            const finalTotal = totalSperr + setupFee;

            calcTotal.innerText = `${finalTotal.toLocaleString('de-DE')} €`;
            valMonthly.innerText = `${userMonthly.toLocaleString('de-DE')} € / Ay`;
            valTotalSperr.innerText = `${totalSperr.toLocaleString('de-DE')} €`;
            valFees.innerText = `${setupFee} €`;

            // Update visual ratio
            const sperrRatio = (totalSperr / finalTotal) * 100;
            const feeRatio = (setupFee / finalTotal) * 100;

            barSperr.style.width = `${sperrRatio}%`;
            barFee.style.width = `${feeRatio}%`;
        }

        sliderMonths.addEventListener('input', updateCalculator);
        sliderExtra.addEventListener('input', updateCalculator);
        updateCalculator();

        // ══════════════════════════════════════════
        // INTERACTIVE WIZARD (DENKLİK SİHİRBAZI)
        // ══════════════════════════════════════════
        let wizardData = {};
        function nextWizardStep(step, val) {
            // Save selection
            if (step === 2) wizardData.lise = val;
            if (step === 3) wizardData.diploma = val;
            if (step === 4) wizardData.lang = val;

            // Update step classes
            document.querySelectorAll('.wizard-step').forEach(el => el.classList.remove('active'));
            document.getElementById(`step-${step}`).classList.add('active');

            // Progress bar
            const prog = document.getElementById('wizard-progress');
            prog.style.width = `${step * 25}%`;
        }

        function showWizardResult(yksVal) {
            wizardData.yks = yksVal;
            document.querySelectorAll('.wizard-step').forEach(el => el.classList.remove('active'));
            document.getElementById('step-result').classList.add('active');
            
            const prog = document.getElementById('wizard-progress');
            prog.style.width = `100%`;

            const rTitle = document.getElementById('result-title');
            const rDesc = document.getElementById('result-desc');

            if (wizardData.lise === 'anadolu' && wizardData.yks === 'yes') {
                rTitle.innerText = 'Tebrikler! Doğrudan Kabul Alabilirsiniz';
                rTitle.style.color = 'var(--gold)';
                rDesc.innerText = 'Lise türünüz ve YKS yerleştirme sonucunuz, Almanya devlet üniversitelerine doğrudan şartlı kabul başvurusunda bulunmanız için mükemmel seviyede eşleşiyor. Dil planlaması ve vize evrak hazırlık sürecinizi başlatmak üzere ücretsiz ön görüşme randevusu oluşturun.';
            } else if (wizardData.diploma === 'yes') {
                rTitle.innerText = 'Mükemmel! Uluslararası Diploma Denkliği';
                rTitle.style.color = 'var(--gold)';
                rDesc.innerText = 'Sahip olduğunuz uluslararası diploma (IB, Abitur vb.), YKS sınav puanına ihtiyaç duymaksızın doğrudan Alman yükseköğrenim kurumlarına başvuru hakkı sağlayabilir. Belgelerinizin resmi denklik onayını kontrol etmek üzere randevunuzu planlayalım.';
            } else {
                rTitle.innerText = 'Almanca Hazırlık ve Studienkolleg Gereklidir';
                rTitle.style.color = 'var(--gold-light)';
                rDesc.innerText = 'Mevcut lise mezuniyeti durumunuz ve YKS yerleşmeniz nedeniyle Almanya devlet üniversitelerine kabul alabilmeniz için 1 yıllık Studienkolleg (Hazırlık Okulu) veya yoğun Almanca eğitimi almanız gerekebilir. Sizin için en verimli geçiş rotasını çizelim.';
            }
        }

        // ══════════════════════════════════════════
        // SMART CHATBOT (STARTBOT)
        // ══════════════════════════════════════════
        const startbotWin = document.getElementById('startbot-win');
        function toggleStartbot() {
            if (startbotWin) startbotWin.classList.toggle('active');
        }

        const startbotBtn = document.getElementById('startbot-btn');
        if (startbotBtn) startbotBtn.addEventListener('click', toggleStartbot);

        function handleBotChip(query) {
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
            typingMsg.innerHTML = answer.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\\n/g, '<br>');
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        // Custom time picker selection
        document.querySelectorAll('.picker-cell').forEach(cell => {
            cell.addEventListener('click', () => {
                cell.parentElement.querySelectorAll('.picker-cell').forEach(c => c.classList.remove('active'));
                cell.classList.add('active');
            });
        });

        // ══════════════════════════════════════════
        // ══════════════════════════════════════════
        // CINEMATIC CANVAS GATE — Image Sequence
        // ══════════════════════════════════════════
        const canvas = document.getElementById('gate-canvas');
        const ctx    = canvas ? canvas.getContext('2d') : null;
        const heroSect = document.getElementById('hero');

        const TOTAL_FRAMES = 192;
        const frames = new Array(TOTAL_FRAMES);
        let loadedCount = 0;
        let currentFrameIndex = 0;   // declare BEFORE any function that references it
        let rafPending = false;

        // Loading screen elements
        const loadingScreen = document.getElementById('loading-screen');
        const loadingBar    = document.getElementById('loading-bar');
        const loadingPct    = document.getElementById('loading-pct');

        // Resize canvas to fill window
        function resizeCanvas() {
            if (!canvas) return;
            canvas.width  = window.innerWidth;
            canvas.height = window.innerHeight;
            if (frames[currentFrameIndex] && frames[currentFrameIndex].complete) {
                drawFrame(frames[currentFrameIndex]);
            }
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // Cover-fit draw
        function drawFrame(img) {
            if (!img || !img.complete || !ctx) return;
            var cw = canvas.width, ch = canvas.height;
            var iw = img.naturalWidth, ih = img.naturalHeight;
            var scale = Math.max(cw / iw, ch / ih) * 1.25; // 25% cinematic zoom to permanently physically crop out Meta AI watermarks on all edges
            var x = (cw - iw * scale) / 2;
            var y = (ch - ih * scale) / 2;
            
            // 4K Quality settings
            ctx.imageSmoothingEnabled = true;
            ctx.imageSmoothingQuality = 'high';
            ctx.filter = 'brightness(0.85) contrast(1.05) saturate(1.15)'; // Exposure recovery for overblown highlights
            
            ctx.clearRect(0, 0, cw, ch);
            ctx.drawImage(img, 0, 0, iw, ih, x, y, iw * scale, ih * scale);
        }

        // Schedule draw via rAF (prevent double-queuing)
        function scheduleDrawFrame(idx) {
            if (!rafPending) {
                rafPending = true;
                requestAnimationFrame(() => {
                    rafPending = false;
                    drawFrame(frames[idx]);
                });
            }
        }

        // Preload all frames; show progress
        function onFrameLoaded(i) {
            loadedCount++;
            const pct = Math.round((loadedCount / TOTAL_FRAMES) * 100);
            if (loadingBar)  loadingBar.style.width  = pct + '%';
            if (loadingPct)  loadingPct.textContent  = pct + '%';

            // Draw first frame as soon as it is ready
            if (i === 0) scheduleDrawFrame(0);

            // Hide loading screen once everything is loaded
            if (loadedCount === TOTAL_FRAMES && loadingScreen) {
                loadingScreen.style.opacity = '0';
                setTimeout(() => { loadingScreen.style.display = 'none'; }, 800);
            }
        }

        const cacheBuster = Date.now();
        for (let i = 0; i < TOTAL_FRAMES; i++) {
            const img = new Image();
            img.onload  = (function(idx){ return function(){ frames[idx] = this; onFrameLoaded(idx); }; })(i);
            img.onerror = function(){ loadedCount++; }; // skip broken frames
            img.src = 'assets/gate-frames/frame_' + String(i).padStart(3, '0') + '.webp?v=' + cacheBuster;
            frames[i] = img; // store reference immediately so array slot exists
        }

        // Scroll scrub
        function scrubGate() {
            if (!heroSect || !canvas) return;
            const scrolled   = window.scrollY - heroSect.offsetTop;
            const scrollable = heroSect.offsetHeight - window.innerHeight;
            const p = Math.max(0, Math.min(1, scrolled / scrollable));

            const fi = Math.min(TOTAL_FRAMES - 1, Math.floor(p * TOTAL_FRAMES));
            if (fi !== currentFrameIndex) {
                currentFrameIndex = fi;
                scheduleDrawFrame(fi);
            }

            // Hero title & scroll hint fade out
            const titleEl = document.getElementById('hero-title');
            const hintEl  = document.getElementById('scroller-hint');
            if (titleEl) {
                const titleOp = Math.max(0, 1 - p * 5);
                titleEl.style.opacity = String(titleOp);
                titleEl.style.visibility = (titleOp > 0) ? 'visible' : 'hidden';
            }
            if (hintEl) {
                const hintOp = Math.max(0, 1 - p * 8);
                hintEl.style.opacity  = String(hintOp);
                hintEl.style.visibility = (hintOp > 0) ? 'visible' : 'hidden';
            }

            // Info cards
            const w = document.getElementById('slide-welcome');
            const b = document.getElementById('slide-bridge');
            if (w) {
                const wp = Math.max(0, Math.min(1, (p - 0.30) / 0.25));
                const wq = Math.max(0, Math.min(1, (p - 0.65) / 0.20));
                const op = wp * (1 - wq);
                w.style.opacity   = String(op);
                w.style.transform = 'translateY(' + ((1 - wp) * 40) + 'px)';
                w.style.visibility = (op > 0.05) ? 'visible' : 'hidden';
            }
            if (b) {
                const bp = Math.max(0, Math.min(1, (p - 0.70) / 0.25));
                b.style.opacity   = String(bp);
                b.style.transform = 'translateY(' + ((1 - bp) * 40) + 'px)';
                b.style.visibility = (bp > 0.05) ? 'visible' : 'hidden';
            }
        }

        window.addEventListener('scroll', scrubGate, { passive: true });
        scrubGate();

    
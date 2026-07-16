
        // Init Lucide Icons
        lucide.createIcons();

        // Init Lenis Smooth Scroll
        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            smoothWheel: true
        });

        function raf(time) {
            lenis.raf(time);
            requestAnimationFrame(raf);
        }
        requestAnimationFrame(raf);

        // Header scroll behavior
        const header = document.getElementById('main-header');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });

        // Mobile toggle
        const mobToggle = document.getElementById('mobile-toggle');
        const mobDrawer = document.getElementById('mobile-menu-drawer');
        mobToggle.addEventListener('click', () => {
            mobDrawer.classList.toggle('open');
            const icon = mobToggle.querySelector('i');
            if (mobDrawer.classList.contains('open')) {
                icon.setAttribute('data-lucide', 'x');
            } else {
                icon.setAttribute('data-lucide', 'menu');
            }
            lucide.createIcons();
        });

        // Smooth scroll to anchors with offset using Lenis
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = this.getAttribute('href');
                if (target === '#') return;

                // Close mobile drawer if open
                if (mobDrawer.classList.contains('open')) {
                    mobDrawer.classList.remove('open');
                    mobToggle.querySelector('i').setAttribute('data-lucide', 'menu');
                    lucide.createIcons();
                }

                // Smooth scroll with offset
                lenis.scrollTo(target, {
                    offset: -100,
                    duration: 1.4,
                    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t))
                });
            });
        });

        // ══════════════════════════════════════════
        // GSAP SCROLL GATE PORTAL TIMELINE
        // ══════════════════════════════════════════
        if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
            gsap.registerPlugin(ScrollTrigger);

            const tl = gsap.timeline({
                scrollTrigger: {
                    trigger: '.portal-container',
                    start: 'top top',
                    end: 'bottom bottom',
                    scrub: 1,
                    pin: true,
                    anticipatePin: 1
                }
            });

            // 1. Swing open the double doors in 3D, scale them outward, zoom-in the courtyard and fade initial hero
            tl.to('#panel-left', { rotateY: -110, opacity: 0, scale: 1.8, ease: 'power1.inOut' }, 0)
              .to('#panel-right', { rotateY: 110, opacity: 0, scale: 1.8, ease: 'power1.inOut' }, 0)
              .to('#campus-bg', { opacity: 1, scale: 1.25, ease: 'power1.out' }, 0)
              .to('#hero-title', { opacity: 0, scale: 0.9, y: -50, ease: 'power1.inOut' }, 0)
              .to('#scroller-hint', { opacity: 0, ease: 'power1.inOut' }, 0);

            // 2. Animate Slide 1 (Welcome Card) in and out
            tl.to('#slide-welcome', { opacity: 1, y: 0, pointerEvents: 'auto', duration: 1.5 }, 0.8)
              .to('#slide-welcome', { opacity: 0, y: -50, pointerEvents: 'none', duration: 1.5 }, 2.5);

            // 3. Animate Slide 2 (Academic Bridge) in and out
            tl.to('#slide-bridge', { opacity: 1, y: 0, pointerEvents: 'auto', duration: 1.5 }, 2.8)
              .to('#slide-bridge', { opacity: 0, y: -50, pointerEvents: 'none', duration: 1.5 }, 4.5);
        }

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
            const chatMessages = document.getElementById('startbot-messages');
            
            // Add user message
            const userMsg = document.createElement('div');
            userMsg.className = 'chat-msg user';
            userMsg.innerText = query;
            chatMessages.appendChild(userMsg);

            // Scroll down
            chatMessages.scrollTop = chatMessages.scrollHeight;

            // Generate answer
            setTimeout(() => {
                const botMsg = document.createElement('div');
                botMsg.className = 'chat-msg bot';
                
                if (query.includes('Bloke Hesap')) {
                    botMsg.innerText = 'Almanya öğrenci vizesi için 2026 yılı güncel resmi Bloke Hesap tutarı yıllık 11.904 € (aylık 992 €) düzeyindedir. Sperrkonto kurulum sürecinizi birlikte yönetiyoruz.';
                } else if (query.includes('BuT Desteği')) {
                    botMsg.innerText = 'Almanya\'da Wohngeld, Bürgergeld veya Kinderzuschlag alan ailelerimizin çocuklarının Nachhilfe (ders desteği) ücretleri devlet tarafından %100 karşılanır. Başvuru formlarınızı hazırlıyoruz.';
                } else {
                    botMsg.innerText = 'Start Akademie UG etüt merkezimiz Rüsselsheim am Main\'da Bahnhofstraße 22 adresindedir. Bize dilediğiniz zaman 0179 7424790 numaralı telefonumuzdan da ulaşabilirsiniz.';
                }
                
                chatMessages.appendChild(botMsg);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }, 700);
        }

        function sendBotMsg() {
            const txt = document.getElementById('startbot-text');
            const q = txt.value.trim();
            if (!q) return;

            txt.value = '';
            const chatMessages = document.getElementById('startbot-messages');
            
            const userMsg = document.createElement('div');
            userMsg.className = 'chat-msg user';
            userMsg.innerText = q;
            chatMessages.appendChild(userMsg);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            setTimeout(() => {
                const botMsg = document.createElement('div');
                botMsg.className = 'chat-msg bot';
                botMsg.innerText = 'Talebiniz kaydedilmiştir. Eğitim uzmanlarımız size en kısa sürede dönüş sağlayacaktır. İsterseniz yukarıdaki hızlı butonlardan birini seçebilirsiniz.';
                chatMessages.appendChild(botMsg);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }, 700);
        }

        // Custom time picker selection
        document.querySelectorAll('.picker-cell').forEach(cell => {
            cell.addEventListener('click', () => {
                cell.parentElement.querySelectorAll('.picker-cell').forEach(c => c.classList.remove('active'));
                cell.classList.add('active');
            });
        });

        // ══════════════════════════════════════════
        // HYLIOX-STYLE SCROLL GATE
        // ══════════════════════════════════════════

        // ── SPRITE GATE: 16-frame image sequence ────────────────────
        const gateSprite = document.getElementById('gate-sprite');
        const heroSect   = document.getElementById('hero');
        const COLS = 4, ROWS = 4, TOTAL = 15; // 4×4=16 frames, 0-indexed

        function scrubGate() {
            try {
                if (!heroSect || !gateSprite) return;
                const scrolled   = window.scrollY - heroSect.offsetTop;
                const scrollable = heroSect.offsetHeight - window.innerHeight;
                const p = Math.max(0, Math.min(1, scrolled / scrollable));

                // Pick the right frame
                const frame = Math.min(Math.round(p * TOTAL), TOTAL);
                const col   = frame % COLS;
                const row   = Math.floor(frame / COLS);
                const x     = col === 0 ? 0 : (col / (COLS - 1)) * 100;
                const y     = row === 0 ? 0 : (row / (ROWS - 1)) * 100;
                gateSprite.style.backgroundPosition = `${x}% ${y}%`;

                // Title / hint fade
                const titleEl = document.getElementById('hero-title');
                const hintEl  = document.getElementById('scroller-hint');
                if (titleEl) titleEl.style.opacity = String(Math.max(0, 1 - p * 5));
                if (hintEl)  hintEl.style.opacity  = String(Math.max(0, 1 - p * 8));

                // Info cards
                const w = document.getElementById('slide-welcome');
                const b = document.getElementById('slide-bridge');
                if (w) {
                    const wp = Math.max(0, Math.min(1, (p - 0.30) / 0.25));
                    const wq = Math.max(0, Math.min(1, (p - 0.65) / 0.20));
                    w.style.opacity   = String(wp * (1 - wq));
                    w.style.transform = `translateY(${(1 - wp) * 40}px)`;
                }
                if (b) {
                    const bp = Math.max(0, Math.min(1, (p - 0.70) / 0.25));
                    b.style.opacity   = String(bp);
                    b.style.transform = `translateY(${(1 - bp) * 40}px)`;
                }
            } catch (e) {
                console.error("scrubGate error:", e);
                const dbgSprite = document.getElementById('dbg-sprite');
                if (dbgSprite) dbgSprite.textContent = "ERR: " + e.message;
            }
        }

        window.addEventListener('scroll', scrubGate, { passive: true });
        scrubGate(); // init at page load

    

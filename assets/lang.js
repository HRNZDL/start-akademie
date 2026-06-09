const translations = {
    "tr": {
        "bot.greeting": "Merhaba! Start Akademie eğitim danışmanlığı asistanına hoş geldiniz. Almanya'da eğitim vizesi, bloke hesap ve lise ders destekleri hakkında size nasıl yardımcı olabilirim?",
        "bot.chip_uni": "🎓 Üni Kayıt Evrakları",
        "bot.chip_but": "📝 BuT Evrakları",
        "bot.chip_bloke": "Bloke Hesap Miktarı",
        "bot.chip_but_info": "Ücretsiz BuT Desteği",
        "bot.chip_contact": "Adres & İletişim",

        "nav.home": "Ana Sayfa",
        "nav.programs": "Programlar",
        "nav.universities": "Üniversiteler",
        "nav.consulting": "Danışmanlık",
        "nav.test": "Denklik Testi",
        "nav.camp": "Yaz Kampı",
        "nav.contact": "İletişim",
        "nav.meeting": "Ön Görüşme",

        "hero.main_title": "Almanya'da<br><em>Eğitim Yolunuz</em>",
        "hero.seo_desc": "Almanya'da Eğitim, Nachhilfe ve Üniversite Kabul Danışmanlığı Merkezi",
        "hero.scroll": "GÖRÜŞ İÇİN KAYDIRIN",
        "hero.title": "Almanya'da Eğitim Yolunuz <em>Burada Başlar</em>",
        "hero.desc": "Almanya'nın en prestijli üniversitelerine giriş, bloke hesap yönetimi ve uzman eğitim destek programlarımızla geleceğinizi şansa bırakmayın.",
        "hero.cta1": "Üniversiteleri İncele",
        "hero.cta2": "Ücretsiz Danışmanlık"
    },
    "en": {
        "bot.greeting": "Hello! Welcome to the Start Akademie assistant. How can I help you with education visas, blocked accounts, or tutoring today?",
        "bot.chip_uni": "🎓 Uni Docs",
        "bot.chip_but": "📝 BuT Docs",
        "bot.chip_bloke": "Blocked Account",
        "bot.chip_but_info": "Free BuT Support",
        "bot.chip_contact": "Contact",

        "nav.home": "Home",
        "nav.programs": "Programs",
        "nav.universities": "Universities",
        "nav.consulting": "Consulting",
        "nav.test": "Equivalence Test",
        "nav.camp": "Summer Camp",
        "nav.contact": "Contact",
        "nav.meeting": "Consultation",

        "hero.main_title": "Your Education<br><em>Path in Germany</em>",
        "hero.seo_desc": "Education, Tutoring, and University Admission Consulting in Germany",
        "hero.scroll": "SCROLL TO VIEW",
        "hero.title": "Your Education Path in Germany <em>Starts Here</em>",
        "hero.desc": "Don't leave your future to chance with admission to Germany's most prestigious universities, blocked account management, and expert education support programs.",
        "hero.cta1": "View Universities",
        "hero.cta2": "Free Consultation"
    },
    "de": {
        "bot.greeting": "Hallo! Willkommen beim Start Akademie Assistenten. Wie kann ich Ihnen heute bei Bildungsvisa, Sperrkonto oder Nachhilfe helfen?",
        "bot.chip_uni": "🎓 Uni-Dokumente",
        "bot.chip_but": "📝 BuT-Dokumente",
        "bot.chip_bloke": "Sperrkonto",
        "bot.chip_but_info": "Kostenlose BuT-Hilfe",
        "bot.chip_contact": "Kontakt",

        "nav.home": "Startseite",
        "nav.programs": "Programme",
        "nav.universities": "Universitäten",
        "nav.consulting": "Beratung",
        "nav.test": "Anerkennungstest",
        "nav.camp": "Sommercamp",
        "nav.contact": "Kontakt",
        "nav.meeting": "Gespräch",

        "hero.main_title": "Ihr Bildungsweg<br><em>in Deutschland</em>",
        "hero.seo_desc": "Bildung, Nachhilfe und Universitätszulassungsberatung in Deutschland",
        "hero.scroll": "ZUM ANZEIGEN SCROLLEN",
        "hero.title": "Ihr Bildungsweg in Deutschland <em>Beginnt Hier</em>",
        "hero.desc": "Überlassen Sie Ihre Zukunft nicht dem Zufall mit der Zulassung zu Deutschlands renommiertesten Universitäten, Sperrkontoverwaltung und fachkundigen Bildungsförderprogrammen.",
        "hero.cta1": "Universitäten Ansehen",
        "hero.cta2": "Kostenlose Beratung"
    }
};

function changeLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
        var key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });

    document.querySelectorAll('input[data-i18n-placeholder], textarea[data-i18n-placeholder]').forEach(function(el) {
        var key = el.getAttribute('data-i18n-placeholder');
        if (translations[lang] && translations[lang][key]) {
            el.setAttribute('placeholder', translations[lang][key]);
        }
    });

    document.querySelectorAll('html').forEach(function(el) {
        el.setAttribute('lang', lang);
        
        if (lang === 'ar') {
            el.setAttribute('dir', 'rtl');
        } else {
            el.setAttribute('dir', 'ltr');
        }
    });
    
    document.querySelectorAll('.hero-content, .section-title, .form-group, p, h1, h2, h3, h4').forEach(function(el) {
        if (!el.closest('.startbot-window')) {
            const targetLang = lang;
            if (targetLang === 'ar') {
                el.style.direction = 'rtl';
                el.style.textAlign = 'right';
            } else {
                el.style.direction = 'ltr';
                el.style.textAlign = 'left';
            }
        }
    });

    try { localStorage.setItem('preferredLang', lang); } catch(e) {}
}

document.addEventListener('DOMContentLoaded', function() {
    var savedLang = 'tr';
    try { savedLang = localStorage.getItem('preferredLang') || 'tr'; } catch(e) {}
    changeLanguage(savedLang);

    var btnContainer = document.querySelector('.lang-switcher, .lang-switch-row');
    if (btnContainer) {
        btnContainer.addEventListener('click', function(e) {
            var target = e.target.closest('[data-lang]');
            if (target) {
                var lang = target.getAttribute('data-lang');
                if (lang) changeLanguage(lang);
            }
        });
    }

    // Also wire up active state on lang buttons
    document.querySelectorAll('[data-lang]').forEach(function(btn) {
        btn.addEventListener('click', function() {
            document.querySelectorAll('[data-lang]').forEach(function(b) {
                b.style.color = 'var(--text-muted)';
                b.style.fontWeight = 'normal';
            });
            btn.style.color = 'var(--gold)';
            btn.style.fontWeight = '700';
        });
    });
});

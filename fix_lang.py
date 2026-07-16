js_code = """
function changeLanguage(lang) {
    // 1. Update text nodes (supports innerHTML for <em> tags)
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });
    
    // 2. Update placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (translations[lang] && translations[lang][key]) {
            el.setAttribute('placeholder', translations[lang][key]);
        }
    });

    // 3. Update active button state (colors)
    document.querySelectorAll('.lang-btn').forEach(btn => {
        if(btn.getAttribute('data-lang') === lang) {
            btn.style.color = 'var(--primary)';
            btn.style.fontWeight = '600';
            btn.style.borderBottom = '2px solid var(--primary)';
        } else {
            btn.style.color = 'var(--text-muted)';
            btn.style.fontWeight = 'normal';
            btn.style.borderBottom = 'none';
        }
    });
    
    // 4. Save preference
    localStorage.setItem('preferredLang', lang);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedLang = localStorage.getItem('preferredLang') || 'de';
    changeLanguage(savedLang);
});
"""

with open('assets/lang.js', 'a', encoding='utf-8') as f:
    f.write("\n" + js_code)

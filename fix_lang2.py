import codecs

with codecs.open('assets/lang.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of the translations object
idx = content.find('};')
if idx == -1:
    idx = content.rfind('}')

# Truncate content to just the translations object
clean_content = content[:idx+1]
if not clean_content.endswith(';'):
    clean_content += ';'

js_code = """
function changeLanguage(lang) {
    try {
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
        try {
            localStorage.setItem('preferredLang', lang);
        } catch(e) {}
        
    } catch(err) {
        alert("Language Switch Error: " + err.message);
        console.error(err);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedLang = localStorage.getItem('preferredLang') || 'de';
    changeLanguage(savedLang);
});
"""

with codecs.open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(clean_content + "\n\n" + js_code)

print("Fixed lang.js")

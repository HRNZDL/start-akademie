with open('assets/lang.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 870 is: "footer.terms": "Nutzungsbedingungen"
# Line 871 is: }   (closing de object)  
# Everything from line 872 onward is garbage from previous broken edits
# We keep lines 1-870 (indices 0-869), then properly close the object

clean_lines = []
for i, line in enumerate(lines):
    if i <= 869:  # up to and including line 870 (0-indexed)
        clean_lines.append(line.rstrip('\r\n'))

# Close the de object and translations object
clean_content = '\n'.join(clean_lines)
clean_content += '\n    }\n};\n'

# Add the changeLanguage function
clean_content += """
function changeLanguage(lang) {
    // 1. Update text content
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
        var key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });

    // 2. Update placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {
        var key = el.getAttribute('data-i18n-placeholder');
        if (translations[lang] && translations[lang][key]) {
            el.setAttribute('placeholder', translations[lang][key]);
        }
    });

    // 3. Update active button style
    document.querySelectorAll('.lang-btn').forEach(function(btn) {
        if (btn.getAttribute('data-lang') === lang) {
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
    try { localStorage.setItem('preferredLang', lang); } catch(e) {}
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    var savedLang = 'de';
    try { savedLang = localStorage.getItem('preferredLang') || 'de'; } catch(e) {}
    changeLanguage(savedLang);
});
"""

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(clean_content)

print("Done. Verifying...")

# Quick verification
with open('assets/lang.js', 'r', encoding='utf-8') as f:
    result = f.read()

# Check brace balance
opens = result.count('{')
closes = result.count('}')
print(f"Open braces: {opens}, Close braces: {closes}")

# Check that changeLanguage exists after };
idx_semicolon = result.find('};')
idx_func = result.find('function changeLanguage')
if idx_func > idx_semicolon > 0:
    print("GOOD: changeLanguage is AFTER the translations object closing")
else:
    print("WARNING: positions - '};' at " + str(idx_semicolon) + ", 'function' at " + str(idx_func))

# Check last 5 lines
last_lines = result.strip().split('\n')[-5:]
for l in last_lines:
    print(f"  | {l}")

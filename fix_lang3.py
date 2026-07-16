import re

with open('assets/lang.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Strategy: Find the translations object by counting braces
# Start after 'const translations = {'
start_marker = 'const translations = {'
start_idx = content.find(start_marker)
if start_idx == -1:
    print("ERROR: Could not find 'const translations = {'")
    exit(1)

# Count braces to find where the object ends
brace_count = 0
obj_start = content.index('{', start_idx)
in_string = False
escape_next = False
end_idx = -1

for i in range(obj_start, len(content)):
    c = content[i]
    if escape_next:
        escape_next = False
        continue
    if c == '\\':
        if in_string:
            escape_next = True
        continue
    if c == '"' and not escape_next:
        in_string = not in_string
        continue
    if in_string:
        continue
    if c == '{':
        brace_count += 1
    elif c == '}':
        brace_count -= 1
        if brace_count == 0:
            end_idx = i
            break

if end_idx == -1:
    print("ERROR: Could not find matching closing brace for translations object")
    # Try a different approach - find the last } before any 'function' or 'document.' keyword
    # Find all occurrences of problematic code inside
    print("Attempting recovery...")
    
    # Find where garbage code starts (first occurrence of document. or function outside strings)
    lines = content.split('\n')
    clean_lines = []
    found_garbage = False
    for line in lines:
        stripped = line.strip()
        # If line starts with code that shouldn't be in JSON object
        if stripped.startswith('document.') or stripped.startswith('function ') or stripped.startswith('// ') and not stripped.startswith('//'):
            if stripped.startswith('// Initialize') or stripped.startswith('// 2.') or stripped.startswith('// 3.') or stripped.startswith('// 4.'):
                found_garbage = True
                continue
        if found_garbage and (stripped.startswith('document.') or stripped.startswith('const ') or stripped.startswith('function ') or stripped.startswith('try') or stripped.startswith('alert') or stripped.startswith('console') or stripped.startswith('}') or stripped.startswith('localStorage') or stripped.startswith('el.') or stripped.startswith('btn.') or stripped.startswith('if(') or stripped.startswith('} else') or stripped.startswith('});') or stripped == ''):
            continue
        if found_garbage and (stripped.startswith('"') or stripped.startswith("'")):
            found_garbage = False
        if not found_garbage:
            clean_lines.append(line)
    
    content = '\n'.join(clean_lines)
    # re-find
    start_idx = content.find(start_marker)
    obj_start = content.index('{', start_idx)
    brace_count = 0
    in_string = False
    escape_next = False
    for i in range(obj_start, len(content)):
        c = content[i]
        if escape_next:
            escape_next = False
            continue
        if c == '\\':
            if in_string:
                escape_next = True
            continue
        if c == '"' and not escape_next:
            in_string = not in_string
            continue
        if in_string:
            continue
        if c == '{':
            brace_count += 1
        elif c == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i
                break

if end_idx == -1:
    print("FATAL: Could not parse translations object even after cleanup")
    exit(1)

translations_obj = content[start_idx:end_idx+1]

# Verify it's valid by checking brace balance
open_count = translations_obj.count('{')
close_count = translations_obj.count('}')
print(f"Braces: {open_count} open, {close_count} close")

# Build the clean file
clean_js = translations_obj + ";\n"

# Add the changeLanguage function
clean_js += """
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
    f.write(clean_js)

print("SUCCESS: lang.js rebuilt cleanly")
print(f"Total length: {len(clean_js)} chars")

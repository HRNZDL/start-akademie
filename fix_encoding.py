import os

replacements = {
    'Ã¼': 'ü', 'Ã¶': 'ö', 'Ã§': 'ç', 'Ä±': 'ı', 'ÄŸ': 'ğ', 'ÅŸ': 'ş',
    'Ãœ': 'Ü', 'Ã–': 'Ö', 'Ã‡': 'Ç', 'Ä°': 'İ', 'Äž': 'Ğ', 'Åž': 'Ş',
    'â†’': '→', 'Ã¤': 'ä', 'Ã„': 'Ä', 'ÃŸ': 'ß', 'â‚¬': '€',
    'â€œ': '“', 'â€\x9d': '”', 'â€™': '’', 'â€¢': '•', 'Ã\xad': 'í',
    'Ã¡': 'á', 'Ã©': 'é',
    'ǟ': 'ß',
    '': 'ı' # Just in case some got completely ruined by PowerShell decoding fallback, though this might be dangerous, we'll run the specific ones first.
}

# The above dict has some generic replacements. Let's make it very precise:
replacements = {
    'Ã¼': 'ü', 'Ã¶': 'ö', 'Ã§': 'ç', 'Ä±': 'ı', 'ÄŸ': 'ğ', 'ÅŸ': 'ş',
    'Ãœ': 'Ü', 'Ã–': 'Ö', 'Ã‡': 'Ç', 'Ä°': 'İ', 'Äž': 'Ğ', 'Åž': 'Ş',
    'â†’': '→', 'Ã¤': 'ä', 'Ã„': 'Ä', 'ÃŸ': 'ß', 'â‚¬': '€',
    'â€œ': '“', 'â€\x9d': '”', 'â€™': '’', 'â€¢': '•', 'Ã\xad': 'í',
    'Ã¡': 'á', 'Ã©': 'é',
    'Ǭ': 'ü', 'Y': 'ğ', 'oniversite': 'Üniversite', 's': 'ş', 'c': 'ç',
    # Wait, earlier I saw "TǬrkiye'den", "baYarsn". This means CP1252 to CP1254 mismatch might have happened.
    # Actually, `Ã¼` is CP1252.
    # What does `TǬrkiye` mean? `Ǭ` is U+01EC. 
    # Let's just decode properly instead of dictionary replacing, it's safer.
}

def fix_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'rb') as f:
        raw = f.read()
    
    # We will find UTF-8 valid sequences that are double encoded.
    # The safest way is to decode the whole file as utf-8, 
    # then encode as cp1252, then decode as utf-8.
    
    # But wait, there are correctly encoded parts (like 'Türkçe').
    # If we encode 'Türkçe' as cp1252, it throws an error because 'ç' is not in cp1252? No, 'ç' IS in cp1252.
    # But 'ş' is NOT in cp1252. So 'Görüşme' will throw an error on 'ş'.
    
    # So we can't do the whole file. We must do it word by word, or chunk by chunk.
    import re
    
    text = raw.decode('utf-8')
    
    def replacer(match):
        s = match.group(0)
        try:
            # Try to reverse the double-encoding
            # This assumes the corrupted text was originally UTF-8, read as CP1252, and saved as UTF-8.
            # So s is currently UTF-8. We encode it back to CP1252 to get the original bytes, 
            # and then decode those bytes as UTF-8.
            fixed = s.encode('cp1252').decode('utf-8')
            return fixed
        except Exception:
            return s

    # Find sequences of characters that are NOT ascii and NOT standard Turkish/German characters
    # Actually, the corrupted characters are things like Ã, Ä, Å, â.
    # We can just match any word containing at least one non-ascii character.
    # To be extremely safe, we replace ONLY if the decoding succeeds.
    
    # We need a regex that captures words or symbols with non-ascii characters
    pattern = re.compile(r'[^\x00-\x7F]+')
    
    fixed_text = pattern.sub(replacer, text)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_text)

for f in ['index.html', 'assets/styles/main.css', 'assets/js/main.js', 'assets/lang.js']:
    fix_file(f)

print('Done')

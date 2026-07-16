const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// ============================================
// HELPER
// ============================================
function findSection(html, commentPattern) {
    const idx = html.indexOf(commentPattern);
    if (idx === -1) throw new Error('Could not find: ' + commentPattern.substring(0, 60));
    return idx;
}

function findSectionEnd(html, startIdx, nextCommentPattern) {
    const nextIdx = html.indexOf(nextCommentPattern, startIdx + 1);
    if (nextIdx === -1) throw new Error('Could not find next: ' + nextCommentPattern.substring(0, 60));
    // Walk back to find the </section> before nextCommentPattern
    const closingIdx = html.lastIndexOf('</section>', nextIdx);
    if (closingIdx < startIdx) throw new Error('Could not find closing </section>');
    return closingIdx + '</section>'.length;
}

// ============================================
// 1. PHASE 3: Replace Pillars section with new Pillars + Services + Process
// ============================================
const pillarsStart = findSection(html, '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\r\n         THE 3 PILLARS');
const pillarsEnd = findSectionEnd(html, pillarsStart, '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\r\n         INTERACTIVE SPERRKONTO CALCULATOR');
const phase3Code = fs.readFileSync('phase3.html', 'utf8');
html = html.substring(0, pillarsStart) + phase3Code + '\r\n\r\n    ' + html.substring(pillarsEnd);
console.log('Phase 3 injected.');

// ============================================
// 2. PHASE 4 PART 1: Replace Universities + Pricing
// ============================================
const univStart = findSection(html, '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\r\n         PARTNER VE SE\u00c7K\u0130N \u00dcN\u0130VERS\u0130TELER');
const univEnd = findSectionEnd(html, univStart, '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\r\n         INTERACTIVE DENKL\u0130K VE UYGUNLUK TEST\u0130');
const phase4Code = fs.readFileSync('phase4.html', 'utf8');
html = html.substring(0, univStart) + phase4Code + '\r\n\r\n    ' + html.substring(univEnd);
console.log('Phase 4 Part 1 (Universities + Pricing) injected.');

// ============================================
// 3. PHASE 4 PART 2: Inject Why Us, Team, Cases, Resources BEFORE Wizard
// ============================================
const wizardStart = findSection(html, '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\r\n         INTERACTIVE DENKL\u0130K VE UYGUNLUK TEST\u0130');
const phase4RestCode = fs.readFileSync('phase4_rest.html', 'utf8');
html = html.substring(0, wizardStart) + phase4RestCode + '\r\n\r\n    ' + html.substring(wizardStart);
console.log('Phase 4 Part 2 (Why Us, Team, Cases, Resources) injected.');

// ============================================
// 4. REPLACE FAQ section
// ============================================
const faqStart = findSection(html, '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\r\n         FAQ SIKCA SORULAN SORULAR');
// Find the closing </section> of FAQ - it's the section right before contact
const faqEnd = findSectionEnd(html, faqStart, '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\r\n         REZERVASYON VE \u0130LET\u0130\u015e\u0130M FORMU');
const faqCode = fs.readFileSync('faq.html', 'utf8');
html = html.substring(0, faqStart) + faqCode + '\r\n\r\n    ' + html.substring(faqEnd);
console.log('FAQ section replaced.');

// ============================================
// 5. Fix email from .de to .com in contact section
// ============================================
html = html.replace('info@startakademie.de', 'info@startakademie.com');
console.log('Email fixed to .com.');

// ============================================
// 6. Update service dropdown options
// ============================================
const oldOptions = `<option value="beratung">Almanya Devlet \u00dcniversitesi Dan\u0131\u015fmanl\u0131\u011f\u0131</option>\r\n                                        <option value="nachhilfe">Okul Ders Deste\u011fi (Nachhilfe)</option>\r\n                                        <option value="sprachkurs">\u00c7evrimi\u00e7i Almanca/\u0130ngilizce Dil Kursu</option>\r\n                                        <option value="sommercamp">Yaz Dil Kamp\u0131 2026</option>`;
const newOptions = `<option value="uni">\u00dcniversite Dan\u0131\u015fmanl\u0131\u011f\u0131</option>\r\n                                        <option value="ausbildung">Ausbildung (Mesleki E\u011fitim)</option>\r\n                                        <option value="dil">Dil Kurslar\u0131</option>\r\n                                        <option value="denklik">Denklik S\u00fcre\u00e7leri</option>\r\n                                        <option value="nachhilfe">Okul Ders Deste\u011fi (Nachhilfe)</option>\r\n                                        <option value="degisim">De\u011fi\u015fim / Yaz Programlar\u0131</option>\r\n                                        <option value="konaklama">Konaklama \u00c7\u00f6z\u00fcmleri</option>`;
if (html.includes(oldOptions)) {
    html = html.replace(oldOptions, newOptions);
    console.log('Service options updated.');
} else {
    console.log('WARNING: Could not find old service options to replace.');
}

// ============================================
// 7. Replace StartBot HTML for smaller/modern design + mobile fix
// ============================================
const startbotOldStart = '    <div class="startbot-container">';
const startbotOldEnd = '    </div>\r\n\r\n    <!-- Footer -->';
const startbotIdx = html.indexOf(startbotOldStart);
const footerMarker = '    <!-- Footer -->';
const footerIdx = html.indexOf(footerMarker, startbotIdx);
if (startbotIdx === -1 || footerIdx === -1) {
    console.log('WARNING: Could not find startbot container bounds.');
} else {
    const newStartbot = `    <div class="startbot-container">
        <button class="startbot-bubble" id="startbot-btn" aria-label="StartBot" ontouchend="event.preventDefault(); toggleStartbot();">
            <span class="startbot-pulse"></span>
            <i data-lucide="message-circle" style="width: 20px; height: 20px;"></i>
        </button>

        <div class="startbot-window" id="startbot-win">
            <div class="startbot-header">
                <h4 style="font-weight: 600; font-family: var(--font-sans); display: flex; align-items: center; gap: 8px; font-size: 0.9rem;">
                    <span style="width: 26px; height: 26px; border-radius: 50%; background: linear-gradient(135deg, var(--gold), var(--gold-light)); display: inline-flex; align-items: center; justify-content: center;">
                        <i data-lucide="bot" style="color: var(--bg-deep); width: 14px; height: 14px;"></i>
                    </span>
                    Start Agent
                </h4>
                <button id="startbot-close" style="background: none; border: none; color: var(--text-muted); cursor: pointer; padding: 4px;" onclick="toggleStartbot()" ontouchend="event.preventDefault(); toggleStartbot();"><i data-lucide="x" style="width: 16px; height: 16px;"></i></button>
            </div>
            
            <div class="startbot-chat" id="startbot-messages">
                <div class="chat-msg bot" data-i18n="bot.greeting">
                    Merhaba! \ud83d\udc4b Start Akademie e\u011fitim dan\u0131\u015fmanl\u0131\u011f\u0131 asistan\u0131y\u0131m. Size nas\u0131l yard\u0131mc\u0131 olabilirim?
                </div>
            </div>

            <div class="startbot-chips">
                <span class="startbot-chip" onclick="handleBotChip('\u00dcniversite kay\u0131t ba\u015fvuru evraklar\u0131')" data-i18n="bot.chip_uni">\ud83c\udf93 \u00dcni Evraklar\u0131</span>
                <span class="startbot-chip" onclick="handleBotChip('Bloke Hesap miktar\u0131 ne kadar?')" data-i18n="bot.chip_bloke">\ud83d\udcb0 Bloke Hesap</span>
                <span class="startbot-chip" onclick="handleBotChip('BuT evraklar\u0131 nas\u0131l doldurulur?')" data-i18n="bot.chip_but">\ud83d\udcdd BuT Evraklar\u0131</span>
                <span class="startbot-chip" onclick="handleBotChip('Adresiniz nerede?')" data-i18n="bot.chip_contact">\ud83d\udccd Adres</span>
            </div>

            <div class="startbot-input">
                <label for="startbot-file" style="cursor: pointer; color: var(--text-muted); padding: 6px; flex-shrink: 0;" title="Belge Y\u00fckle">
                    <i data-lucide="paperclip" style="width: 16px; height: 16px;"></i>
                </label>
                <input type="file" id="startbot-file" style="display: none;" accept="image/*,application/pdf">
                <div id="file-indicator" style="display:none; position:absolute; top:-22px; left:10px; background:var(--gold); color:black; font-size:0.65rem; padding:2px 6px; border-radius:4px; font-weight:600;">Dosya \u2713</div>
                
                <input type="text" placeholder="Sorunuzu yaz\u0131n..." id="startbot-text" onkeypress="if(event.key === 'Enter') sendBotMsg()">
                <button onclick="sendBotMsg()" style="flex-shrink: 0;"><i data-lucide="send" style="width: 14px; height: 14px;"></i></button>
            </div>
        </div>
    </div>`;

    html = html.substring(0, startbotIdx) + newStartbot + '\r\n\r\n    ' + html.substring(footerIdx);
    console.log('StartBot replaced with compact modern version.');
}

// ============================================
// 8. Update nav menu with new sections
// ============================================
// The nav already has links; let's update footer services links
const oldFooterServices = `<li><a href="#pillars" data-i18n="footer.s1">Okul Ders Deste\u011fi (Nachhilfe)</a></li>\r\n                        <li><a href="#pricing">\u00dcniversite Dan\u0131\u015fmanl\u0131\u011f\u0131</a></li>\r\n                        <li><a href="#pillars">Online Almanca Kurslar\u0131</a></li>\r\n                        <li><a href="#camp">Yaz Dil Kamplar\u0131 2026</a></li>`;
const newFooterServices = `<li><a href="#services">\u00dcniversite Dan\u0131\u015fmanl\u0131\u011f\u0131</a></li>\r\n                        <li><a href="#services">Ausbildung (Mesleki E\u011fitim)</a></li>\r\n                        <li><a href="#services">Dil Kurslar\u0131</a></li>\r\n                        <li><a href="#pillars">Okul Ders Deste\u011fi (Nachhilfe)</a></li>\r\n                        <li><a href="#services">Denklik S\u00fcre\u00e7leri</a></li>`;
if (html.includes(oldFooterServices)) {
    html = html.replace(oldFooterServices, newFooterServices);
    console.log('Footer services links updated.');
} else {
    console.log('WARNING: Could not find old footer services links.');
}

fs.writeFileSync('index.html', html);
console.log('\n=== ALL UPDATES APPLIED SUCCESSFULLY ===');
console.log('Total file size: ' + html.length + ' bytes');

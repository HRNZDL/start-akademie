const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

function getBounds(html, startId, nextId) {
    const startStr = 'id="' + startId + '"';
    const nextStr = 'id="' + nextId + '"';
    
    // Find where the start section begins
    const startTagIdx = html.indexOf(startStr);
    if (startTagIdx === -1) throw new Error("Could not find start id: " + startId);
    let sectionStart = html.lastIndexOf('<section', startTagIdx);
    
    // Check if there is a comment block right before it, if so include it
    const possibleCommentStart = html.lastIndexOf('<!--', sectionStart);
    if (possibleCommentStart !== -1 && html.substring(possibleCommentStart, sectionStart).trim().length < 200) { // arbitrary length to catch nearby comment
        // Let's just stick to <section> start to be completely safe and predictable.
    }
    
    // Find where the next section begins
    const nextTagIdx = html.indexOf(nextStr);
    if (nextTagIdx === -1) throw new Error("Could not find next id: " + nextId);
    let nextSectionStart = html.lastIndexOf('<section', nextTagIdx);
    
    // If there is an HTML comment right before the next section, let's cut before that comment
    const commentBeforeNext = html.lastIndexOf('<!--', nextSectionStart);
    if (commentBeforeNext !== -1 && html.substring(commentBeforeNext, nextSectionStart).trim() === '') {
        nextSectionStart = commentBeforeNext;
    }

    return { start: sectionStart, end: nextSectionStart };
}

// 1. Phase 3 (Replace pillars up to calculator)
const b1 = getBounds(html, 'pillars', 'calculator');
const p3Html = fs.readFileSync('phase3.html', 'utf8');
html = html.substring(0, b1.start) + p3Html + '\n\n    ' + html.substring(b1.end);
console.log('Phase 3 applied.');

// 2. Phase 4 (Replace universities AND pricing up to wizard)
const b2 = getBounds(html, 'universities', 'wizard');
const p4Html = fs.readFileSync('phase4.html', 'utf8');
const p4RestHtml = fs.readFileSync('phase4_rest.html', 'utf8');
html = html.substring(0, b2.start) + p4Html + '\n\n' + p4RestHtml + '\n\n    ' + html.substring(b2.end);
console.log('Phase 4 applied.');

// 3. FAQ (Replace faq up to contact)
const b3 = getBounds(html, 'faq', 'contact');
const faqHtml = fs.readFileSync('faq.html', 'utf8');
html = html.substring(0, b3.start) + faqHtml + '\n\n    ' + html.substring(b3.end);
console.log('FAQ applied.');

// 4. Contact email and services update
html = html.replace('info@startakademie.de', 'info@startakademie.com');

const oldOptions = `<option value="beratung">Almanya Devlet \u00dcniversitesi Dan\u0131\u015fmanl\u0131\u011f\u0131</option>\r
                                        <option value="nachhilfe">Okul Ders Deste\u011fi (Nachhilfe)</option>\r
                                        <option value="sprachkurs">\u00c7evrimi\u00e7i Almanca/\u0130ngilizce Dil Kursu</option>\r
                                        <option value="sommercamp">Yaz Dil Kamp\u0131 2026</option>`;
const newOptions = `<option value="uni">\u00dcniversite Dan\u0131\u015fmanl\u0131\u011f\u0131</option>\n                                        <option value="ausbildung">Ausbildung (Mesleki E\u011fitim)</option>\n                                        <option value="dil">Dil Kurslar\u0131</option>\n                                        <option value="denklik">Denklik S\u00fcre\u00e7leri</option>\n                                        <option value="nachhilfe">Okul Ders Deste\u011fi (Nachhilfe)</option>\n                                        <option value="degisim">De\u011fi\u015fim / Yaz Programlar\u0131</option>\n                                        <option value="konaklama">Konaklama \u00c7\u00f6z\u00fcmleri</option>`;

// We will use a regex if exact string replacement fails due to \r\n differences
const optionsRegex = /<option value="beratung">.*?<\/option>\s*<option value="nachhilfe">.*?<\/option>\s*<option value="sprachkurs">.*?<\/option>\s*<option value="sommercamp">.*?<\/option>/is;
if (optionsRegex.test(html)) {
    html = html.replace(optionsRegex, newOptions);
    console.log('Contact options updated.');
} else {
    console.log('WARNING: Contact options not found!');
}

// 5. StartBot update
const startbotStart = html.indexOf('<div class="startbot-container">');
const startbotEnd = html.indexOf('<footer>', startbotStart);

if (startbotStart !== -1 && startbotEnd !== -1) {
    const newStartbot = `    <!-- FLOATING SMART CHATBOT (STARTBOT) — Modern & Compact -->
    <div class="startbot-container">
        <button class="startbot-bubble" id="startbot-btn" aria-label="StartBot" ontouchend="event.preventDefault(); toggleStartbot();">
            <span class="startbot-pulse"></span>
            <i data-lucide="message-circle" style="width: 22px; height: 22px;"></i>
        </button>

        <div class="startbot-window" id="startbot-win">
            <div class="startbot-header">
                <h4 style="font-weight: 600; font-family: var(--font-sans); display: flex; align-items: center; gap: 8px; font-size: 0.95rem;">
                    <span style="width: 28px; height: 28px; border-radius: 50%; background: linear-gradient(135deg, var(--gold), var(--gold-light)); display: flex; align-items: center; justify-content: center;">
                        <i data-lucide="bot" style="color: var(--bg-deep); width: 16px; height: 16px;"></i>
                    </span>
                    Start Agent
                </h4>
                <button id="startbot-close" style="background: none; border: none; color: var(--text-muted); cursor: pointer; padding: 4px;" onclick="toggleStartbot()" ontouchend="event.preventDefault(); toggleStartbot();"><i data-lucide="x" style="width: 18px; height: 18px;"></i></button>
            </div>
            
            <div class="startbot-chat" id="startbot-messages">
                <div class="chat-msg bot" data-i18n="bot.greeting">
                    Merhaba! \ud83d\udc4b Start Akademie e\u011fitim dan\u0131\u015fmanl\u0131\u011f\u0131 asistan\u0131y\u0131m. Almanya'da e\u011fitim, bloke hesap ve ders destekleri hakk\u0131nda size nas\u0131l yard\u0131mc\u0131 olabilirim?
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
    </div>\n\n    `;
    
    // Find the comment before footer to slice perfectly
    const commentBeforeFooter = html.lastIndexOf('<!-- Footer -->', startbotEnd);
    const endCut = commentBeforeFooter !== -1 ? commentBeforeFooter : startbotEnd;
    
    html = html.substring(0, startbotStart) + newStartbot + html.substring(endCut);
    console.log('StartBot applied.');
} else {
    console.log('WARNING: Startbot tags not found.');
}

// 6. Nav menu footer update
const newFooterServices = `<li><a href="#services">\u00dcniversite Dan\u0131\u015fmanl\u0131\u011f\u0131</a></li>\n                        <li><a href="#services">Ausbildung (Mesleki E\u011fitim)</a></li>\n                        <li><a href="#services">Dil Kurslar\u0131</a></li>\n                        <li><a href="#pillars">Okul Ders Deste\u011fi (Nachhilfe)</a></li>\n                        <li><a href="#services">Denklik S\u00fcre\u00e7leri</a></li>`;
const oldFooterServicesRegex = /<li><a href="#pillars"[^>]*>Okul Ders Deste\u011fi.*?<\/li>\s*<li><a href="#pricing">\u00dcniversite Dan\u0131\u015fmanl\u0131\u011f\u0131<\/a><\/li>\s*<li><a href="#pillars">Online Almanca Kurslar\u0131<\/a><\/li>\s*<li><a href="#camp">Yaz Dil Kamplar\u0131 2026<\/a><\/li>/is;
if (oldFooterServicesRegex.test(html)) {
    html = html.replace(oldFooterServicesRegex, newFooterServices);
    console.log('Footer links updated.');
} else {
    console.log('WARNING: Footer links not found.');
}

fs.writeFileSync('index.html', html);
console.log('All changes applied successfully!');

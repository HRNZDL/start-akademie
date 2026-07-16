const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// 1. Inject phase4_rest.html before #wizard
const wizardIndex = html.indexOf('<!-- ══════════════════════════════════════════\r\n         INTERACTIVE DENKLİK VE UYGUNLUK TESTİ');
if (wizardIndex === -1) {
    console.error("Could not find wizard section");
    process.exit(1);
}

const p4RestCode = fs.readFileSync('phase4_rest.html', 'utf8');
html = html.substring(0, wizardIndex) + p4RestCode + '\n\n    ' + html.substring(wizardIndex);


// 2. Replace FAQ section
const startFaq = html.indexOf('<!-- ══════════════════════════════════════════\r\n         FAQ SIKÇA SORULAN SORULAR');
if (startFaq === -1) {
    console.error("Could not find FAQ section");
    process.exit(1);
}
const endFaq = html.indexOf('<!-- ══════════════════════════════════════════\r\n         REZERVASYON VE İLETİŞİM FORMU');
if (endFaq === -1) {
    console.error("Could not find end of FAQ section");
    process.exit(1);
}
let actualEndFaq = html.lastIndexOf('</section>', endFaq);
if (actualEndFaq < startFaq) {
    console.error("Could not find closing section of FAQ");
    process.exit(1);
}
actualEndFaq += '</section>'.length;

const faqCode = fs.readFileSync('faq.html', 'utf8');
html = html.substring(0, startFaq) + faqCode + '\n\n    ' + html.substring(actualEndFaq);

fs.writeFileSync('index.html', html);
console.log("Successfully updated index.html for the rest of Phase 4 (Why Us, Team, Cases, Resources, FAQ).");

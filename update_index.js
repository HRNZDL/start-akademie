const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// Phase 3: Pillars + Services + Process
// Replace from `<!-- THE 3 PILLARS` to `</section>` just before `<!-- INTERACTIVE SPERRKONTO CALCULATOR`
const startPillars = html.indexOf('<!-- ══════════════════════════════════════════\r\n         THE 3 PILLARS');
if (startPillars === -1) {
    console.error("Could not find start of PILLARS");
    process.exit(1);
}
const endPillarsTag = '</section>';
const nextSection = '<!-- ══════════════════════════════════════════\r\n         INTERACTIVE SPERRKONTO CALCULATOR';
let endPillars = html.indexOf(nextSection, startPillars);
if (endPillars === -1) {
    console.error("Could not find end of PILLARS");
    process.exit(1);
}
// walk back to find the closing section tag
let actualEndPillars = html.lastIndexOf('</section>', endPillars);
if (actualEndPillars < startPillars) {
    console.error("Could not find closing section of PILLARS");
    process.exit(1);
}
actualEndPillars += '</section>'.length;

const phase3Code = fs.readFileSync('phase3.html', 'utf8');
html = html.substring(0, startPillars) + phase3Code + '\n\n    ' + html.substring(actualEndPillars);


// Phase 4 Part 1: Universities & Pricing
const startUniv = html.indexOf('<!-- ══════════════════════════════════════════\r\n         PARTNER VE SEÇKİN ÜNİVERSİTELER');
if (startUniv === -1) {
    console.error("Could not find start of UNIV");
    process.exit(1);
}
const endPricing = html.indexOf('<!-- ══════════════════════════════════════════\r\n         INTERACTIVE DENKLİK VE UYGUNLUK TESTİ');
if (endPricing === -1) {
    console.error("Could not find end of PRICING");
    process.exit(1);
}
let actualEndPricing = html.lastIndexOf('</section>', endPricing);
if (actualEndPricing < startUniv) {
    console.error("Could not find closing section of PRICING");
    process.exit(1);
}
actualEndPricing += '</section>'.length;

const phase4Code = fs.readFileSync('phase4.html', 'utf8');
html = html.substring(0, startUniv) + phase4Code + '\n\n    ' + html.substring(actualEndPricing);

fs.writeFileSync('index.html', html);
console.log("Successfully updated index.html for Phase 3 and 4.");

const fs = require('fs');
let css = fs.readFileSync('assets/style.css', 'utf8');

// 1. Add color variables to :root
const rootEnd = css.indexOf('}', css.indexOf(':root'));
if (rootEnd !== -1 && !css.includes('--c-uni')) {
    const newVars = `
    /* Services Colors */
    --c-uni: #0077b6;
    --c-dil: #f57c00;
    --c-aus: #009688;
    --c-denk: #7b2cbf;
    --c-deg: #e91e63;
    --c-kon: #d81159;
`;
    css = css.substring(0, rootEnd) + newVars + css.substring(rootEnd);
    console.log('Variables added.');
}

// 2. Make Startbot smaller and modern
const oldWindowRegex = /\.startbot-window\s*\{[^}]+\}/is;
const newWindowCSS = `.startbot-window {
    position: fixed;
    bottom: 80px;
    right: 20px;
    width: 280px;
    height: 380px;
    background: rgba(14, 16, 21, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 20px rgba(212, 175, 100, 0.1);
    display: none;
    flex-direction: column;
    overflow: hidden;
    backdrop-filter: blur(20px) saturate(150%);
    -webkit-backdrop-filter: blur(20px) saturate(150%);
    z-index: 999999;
    transform: translateY(20px) scale(0.95);
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
}`;

if (oldWindowRegex.test(css)) {
    css = css.replace(oldWindowRegex, newWindowCSS);
    console.log('StartBot window CSS updated.');
}

const oldBubbleRegex = /\.startbot-bubble\s*\{[^}]+\}/is;
const newBubbleCSS = `.startbot-bubble {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--gold), var(--gold-light));
    color: var(--bg-deep);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 20px rgba(212, 175, 100, 0.4);
    border: none;
    transition: var(--transition);
    position: relative;
    outline: none;
    -webkit-tap-highlight-color: transparent;
}`;
if (oldBubbleRegex.test(css)) {
    css = css.replace(oldBubbleRegex, newBubbleCSS);
    console.log('StartBot bubble CSS updated.');
}

fs.writeFileSync('assets/style.css', css);
console.log('CSS updated successfully.');

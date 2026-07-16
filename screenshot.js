const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Emulate iPhone 12 Pro Max
    await page.setViewport({
        width: 428,
        height: 926,
        isMobile: true,
        hasTouch: true,
        deviceScaleFactor: 3,
    });

    await page.goto('file:///C:/Users/Harun/Downloads/beautiful-websites-kit-dist/sites/start-akademie/index.html', { waitUntil: 'networkidle2' });
    
    // Take a screenshot
    await page.screenshot({ path: 'mobile-view.png', fullPage: true });

    await browser.close();
    console.log('Screenshot saved to mobile-view.png');
})();

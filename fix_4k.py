import io
import re

# 1. Update index.html for 4K canvas rendering
html_path = 'index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_resize = """        function resizeCanvas() {
            if (!canvas) return;
            canvas.width  = window.innerWidth;
            canvas.height = window.innerHeight;
            if (frames[currentFrameIndex] && frames[currentFrameIndex].complete) {
                drawFrame(frames[currentFrameIndex]);
            }
        }"""
new_resize = """        function resizeCanvas() {
            if (!canvas) return;
            const dpr = window.devicePixelRatio || 1;
            canvas.width  = window.innerWidth * dpr;
            canvas.height = window.innerHeight * dpr;
            if (ctx) {
                ctx.setTransform(1, 0, 0, 1, 0, 0); // Reset transform
                ctx.scale(dpr, dpr);
            }
            if (frames[currentFrameIndex] && frames[currentFrameIndex].complete) {
                drawFrame(frames[currentFrameIndex]);
            }
        }"""
html = html.replace(old_resize, new_resize)

old_draw = """        function drawFrame(img) {
            if (!img || !img.complete || !ctx) return;
            var cw = canvas.width, ch = canvas.height;
            var iw = img.naturalWidth, ih = img.naturalHeight;
            var scale = Math.max(cw / iw, ch / ih) * 1.25; // 25% cinematic zoom to permanently physically crop out Meta AI watermarks on all edges
            var x = (cw - iw * scale) / 2;
            var y = (ch - ih * scale) / 2;
            
            // 4K Quality settings
            ctx.imageSmoothingEnabled = true;
            ctx.imageSmoothingQuality = 'high';
            ctx.filter = 'brightness(0.85) contrast(1.05) saturate(1.15)'; // Exposure recovery for overblown highlights
            
            ctx.clearRect(0, 0, cw, ch);
            ctx.drawImage(img, 0, 0, iw, ih, x, y, iw * scale, ih * scale);
        }"""
new_draw = """        function drawFrame(img) {
            if (!img || !img.complete || !ctx) return;
            // Use CSS logical pixels
            var cw = window.innerWidth;
            var ch = window.innerHeight;
            var iw = img.naturalWidth, ih = img.naturalHeight;
            var scale = Math.max(cw / iw, ch / ih) * 1.15; // Adjusted zoom to retain more sharpness
            var x = (cw - iw * scale) / 2;
            var y = (ch - ih * scale) / 2;
            
            // 4K Ultra Quality settings
            ctx.imageSmoothingEnabled = true;
            ctx.imageSmoothingQuality = 'high';
            // Removed artificial darkening to let the sky look bright and natural
            ctx.filter = 'brightness(1.0) contrast(1.05) saturate(1.10)'; 
            
            ctx.clearRect(0, 0, cw, ch);
            ctx.drawImage(img, 0, 0, iw, ih, x, y, iw * scale, ih * scale);
        }"""
html = html.replace(old_draw, new_draw)

# Bust cache
html = html.replace('assets/style.css?v=3', 'assets/style.css?v=4')
html = html.replace('assets/lang.js?v=5', 'assets/lang.js?v=6')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css to fix dark overlay
css_path = 'assets/style.css'
with io.open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

old_overlay = """        .video-overlay {
            position: absolute;
            inset: 0;
            /* Soft dark vignette to make the gold/white text pop elegantly */
            background: radial-gradient(ellipse at center, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.3) 50%, rgba(0,0,0,0.6) 100%);
            z-index: 2;
            pointer-events: none;
        }"""
new_overlay = """        .video-overlay {
            position: absolute;
            inset: 0;
            /* Lighter elegant vignette to preserve natural sky brightness while keeping text readable */
            background: radial-gradient(ellipse at center, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.3) 100%);
            z-index: 2;
            pointer-events: none;
        }"""
css = css.replace(old_overlay, new_overlay)

with io.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("4K and brightness adjustments applied.")

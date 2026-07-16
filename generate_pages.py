#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Start Akademie – Subpage Generator
Generates all required subpages with consistent header, footer, and styling.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# SHARED HEADER (identical on every subpage)
# ─────────────────────────────────────────────────────────────────────────────
def header(title, desc, active_link=""):
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
    <title>{title} | Start Akademie</title>
    <meta name="description" content="{desc}">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,600;1,9..144,300&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">

    <!-- Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>

    <!-- Scripts -->
    <script src="assets/lang.js?v=21"></script>
    <script src="assets/theme.js"></script>

    <!-- GSAP -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>

    <style>body {{ margin: 0; padding: 0; width: 100%; }}</style>
    <link rel="stylesheet" href="assets/style.css?v=36">

    <style>
      /* ── Subpage Hero Banner ── */
      .page-hero {{
        background: linear-gradient(135deg, var(--navy) 0%, #0a1628 60%, #0d1b2a 100%);
        padding: 140px 0 80px;
        text-align: center;
        position: relative;
        overflow: hidden;
      }}
      .page-hero::before {{
        content: '';
        position: absolute; inset: 0;
        background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(0,80,158,0.25) 0%, transparent 70%);
      }}
      .page-hero h1 {{
        font-family: var(--font-serif);
        font-size: clamp(2rem, 5vw, 3.5rem);
        color: var(--text);
        margin-bottom: 16px;
        position: relative;
      }}
      .page-hero h1 em {{ color: var(--gold); font-style: normal; }}
      .page-hero p.hero-sub {{
        font-size: 1.1rem;
        color: var(--text-muted);
        max-width: 620px;
        margin: 0 auto 32px;
        position: relative;
        line-height: 1.7;
      }}
      .badge-prep {{
        display: inline-block;
        background: rgba(255,193,7,0.12);
        border: 1px solid var(--gold);
        color: var(--gold);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        padding: 5px 12px;
        border-radius: 999px;
        margin-bottom: 16px;
      }}
      /* ── Content sections ── */
      .content-section {{ padding: 80px 0; }}
      .content-section.alt {{ background: var(--surface); }}
      .content-section h2 {{
        font-family: var(--font-serif);
        font-size: clamp(1.6rem, 3vw, 2.4rem);
        margin-bottom: 16px;
        color: var(--text);
      }}
      .content-section h2 em {{ color: var(--gold); font-style: normal; }}
      .lead-text {{
        font-size: 1.05rem;
        color: var(--text-muted);
        line-height: 1.8;
        max-width: 720px;
        margin-bottom: 40px;
      }}
      /* ── Feature grid ── */
      .feat-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 24px;
        margin-top: 32px;
      }}
      .feat-card {{
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        border-radius: 16px;
        padding: 28px;
        transition: transform 0.3s, box-shadow 0.3s;
      }}
      .feat-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.2);
      }}
      .feat-card .icon-wrap {{
        width: 48px; height: 48px;
        border-radius: 12px;
        background: linear-gradient(135deg, var(--blue) 0%, var(--navy) 100%);
        display: flex; align-items: center; justify-content: center;
        margin-bottom: 16px;
        color: #fff;
      }}
      .feat-card h3 {{ font-size: 1rem; margin-bottom: 8px; color: var(--text); }}
      .feat-card p {{ font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin: 0; }}
      /* ── Step list ── */
      .step-list {{ list-style: none; padding: 0; margin: 0; }}
      .step-list li {{
        display: flex; gap: 20px; align-items: flex-start;
        padding: 20px 0;
        border-bottom: 1px solid var(--glass-border);
      }}
      .step-list li:last-child {{ border-bottom: none; }}
      .step-num {{
        min-width: 40px; height: 40px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
        display: flex; align-items: center; justify-content: center;
        font-weight: 700; font-size: 0.9rem; color: var(--navy);
      }}
      .step-content h4 {{ margin: 0 0 4px; font-size: 1rem; color: var(--text); }}
      .step-content p {{ margin: 0; font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; }}
      /* ── CTA Banner ── */
      .cta-banner {{
        background: linear-gradient(135deg, var(--blue) 0%, var(--navy) 100%);
        border-radius: 24px;
        padding: 60px 40px;
        text-align: center;
        margin: 60px 0;
      }}
      .cta-banner h2 {{ font-family: var(--font-serif); font-size: clamp(1.6rem,3vw,2.2rem); color: #fff; margin-bottom: 12px; }}
      .cta-banner p {{ color: rgba(255,255,255,0.75); margin-bottom: 32px; font-size: 1rem; }}
      /* ── FAQ accordion ── */
      .faq-item {{
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        margin-bottom: 12px;
        overflow: hidden;
      }}
      .faq-q {{
        width: 100%; text-align: left; background: var(--glass-bg);
        border: none; padding: 18px 24px; cursor: pointer;
        font-size: 0.95rem; font-weight: 600; color: var(--text);
        display: flex; justify-content: space-between; align-items: center;
        gap: 12px;
      }}
      .faq-q:hover {{ background: rgba(0,80,158,0.08); }}
      .faq-a {{
        max-height: 0; overflow: hidden;
        transition: max-height 0.4s ease, padding 0.4s ease;
        font-size: 0.9rem; color: var(--text-muted); line-height: 1.7;
        padding: 0 24px;
      }}
      .faq-item.open .faq-a {{ max-height: 300px; padding: 0 24px 20px; }}
      .faq-item.open .faq-chevron {{ transform: rotate(180deg); }}
      .faq-chevron {{ transition: transform 0.3s; flex-shrink: 0; }}
      /* ── Contact form ── */
      .form-card {{
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 40px;
      }}
      .form-card h3 {{ font-family: var(--font-serif); font-size: 1.5rem; margin-bottom: 8px; color: var(--text); }}
      .form-card p.form-sub {{ color: var(--text-muted); font-size: 0.9rem; margin-bottom: 28px; }}
      .form-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
      @media (max-width: 600px) {{ .form-row {{ grid-template-columns: 1fr; }} }}
      .form-group {{ display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px; }}
      .form-group label {{ font-size: 0.82rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.06em; }}
      .form-group input, .form-group select, .form-group textarea {{
        background: var(--surface); border: 1px solid var(--glass-border);
        border-radius: 10px; padding: 12px 16px;
        font-size: 0.95rem; color: var(--text); font-family: var(--font-sans);
        transition: border-color 0.3s, box-shadow 0.3s;
        outline: none; width: 100%; box-sizing: border-box;
      }}
      .form-group input:focus, .form-group select:focus, .form-group textarea:focus {{
        border-color: var(--gold); box-shadow: 0 0 0 3px rgba(212,175,55,0.15);
      }}
      .form-group textarea {{ resize: vertical; min-height: 100px; }}
      /* ── Info table ── */
      .info-table {{ width: 100%; border-collapse: collapse; }}
      .info-table tr {{ border-bottom: 1px solid var(--glass-border); }}
      .info-table th, .info-table td {{ padding: 14px 20px; text-align: left; font-size: 0.9rem; }}
      .info-table th {{ color: var(--text-muted); font-weight: 600; width: 200px; }}
      .info-table td {{ color: var(--text); }}
    </style>
</head>
<body>

    <!-- Ambient glows -->
    <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; overflow: hidden; pointer-events: none; z-index: -1;">
        <div class="glow-orb glow-1"></div>
        <div class="glow-orb glow-2"></div>
    </div>

    <!-- Navigation Header -->
    <header id="main-header">
        <div class="container nav-container">
            <a href="index.html" class="brand-logo" style="display: flex; align-items: center; text-decoration: none;">
                <img src="assets/logo-full-white.png" alt="Start Akademie Logo" class="nav-brand-img nav-logo-dark" style="height: 52px; width: auto; margin-top: 4px; transition: all 0.4s ease;">
                <img src="assets/logo-full-dark.png" alt="Start Akademie Logo" class="nav-brand-img nav-logo-light" style="height: 52px; width: auto; margin-top: 4px; transition: all 0.4s ease;">
            </a>
            <div class="nav-menu">
                <a href="index.html" class="nav-link" data-i18n="nav.home">Ana Sayfa</a>
                <a href="uni.html" class="nav-link {'active' if active_link=='uni' else ''}" data-i18n="nav.university">Üniversite</a>
                <a href="dil.html" class="nav-link {'active' if active_link=='dil' else ''}" data-i18n="nav.languages">Dil Kursları</a>
                <a href="ausbildung.html" class="nav-link {'active' if active_link=='ausbildung' else ''}" data-i18n="nav.ausbildung">Ausbildung</a>
                <a href="denklik.html" class="nav-link {'active' if active_link=='denklik' else ''}" data-i18n="nav.recognition">Denklik</a>
                <a href="degisim.html" class="nav-link {'active' if active_link=='degisim' else ''}" data-i18n="nav.exchange">Değişim &amp; Yaz</a>
                <a href="konaklama.html" class="nav-link {'active' if active_link=='konaklama' else ''}" data-i18n="nav.accommodation">Konaklama</a>
                <a href="hakkimizda.html" class="nav-link {'active' if active_link=='hakkimizda' else ''}" data-i18n="nav.about">Hakkımızda</a>
                <a href="iletisim.html" class="nav-link {'active' if active_link=='iletisim' else ''}" data-i18n="nav.contact">İletişim</a>
            </div>
            <div style="display: flex; align-items: center; gap: 16px;">
                <!-- Language Selector -->
                <div style="display: flex; gap: 8px; margin-right: 12px; font-size: 0.8rem; font-weight: 600;">
                    <span class="lang-btn" data-lang="tr" onclick="changeLanguage('tr')" style="cursor: pointer; color: var(--text-muted);">TR</span>
                    <span class="lang-btn" data-lang="en" onclick="changeLanguage('en')" style="cursor: pointer; color: var(--text-muted);">EN</span>
                    <span class="lang-btn" data-lang="de" onclick="changeLanguage('de')" style="cursor: pointer; color: var(--text-muted);">DE</span>
                </div>
                <!-- Theme Toggle -->
                <button onclick="toggleTheme()" aria-label="Tema Değiştir" style="background: none; border: none; color: var(--text); cursor: pointer; display: flex; align-items: center; margin-right: 8px;">
                    <i id="theme-icon" data-lucide="sun"></i>
                </button>
                <a href="iletisim.html" class="btn btn-primary btn-header-consult" style="padding: 10px 20px; font-size: 0.8rem;">
                    <span data-i18n="nav.meeting">Ön Görüşme</span> <i data-lucide="calendar"></i>
                </a>
                <button class="mobile-btn" id="mobile-toggle" aria-label="Menü">
                    <i data-lucide="menu"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Mobile Menu Drawer -->
    <div class="mobile-drawer" id="mobile-menu-drawer">
        <div style="display: flex; gap: 16px; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.1); justify-content: center; font-size: 0.9rem; font-weight: 600;">
            <span class="lang-btn" onclick="changeLanguage('tr')" style="cursor:pointer; color: var(--gold);">TR</span>
            <span style="color: rgba(255,255,255,0.2);">|</span>
            <span class="lang-btn" onclick="changeLanguage('en')" style="cursor:pointer; color: var(--text-muted);">EN</span>
            <span style="color: rgba(255,255,255,0.2);">|</span>
            <span class="lang-btn" onclick="changeLanguage('de')" style="cursor:pointer; color: var(--text-muted);">DE</span>
        </div>
        <a href="index.html" class="nav-link" data-i18n="nav.home">Ana Sayfa</a>
        <a href="uni.html" class="nav-link" data-i18n="nav.university">Üniversite</a>
        <a href="dil.html" class="nav-link" data-i18n="nav.languages">Dil Kursları</a>
        <a href="ausbildung.html" class="nav-link" data-i18n="nav.ausbildung">Ausbildung</a>
        <a href="denklik.html" class="nav-link" data-i18n="nav.recognition">Denklik</a>
        <a href="degisim.html" class="nav-link" data-i18n="nav.exchange">Değişim &amp; Yaz Programları</a>
        <a href="konaklama.html" class="nav-link" data-i18n="nav.accommodation">Konaklama</a>
        <a href="hakkimizda.html" class="nav-link" data-i18n="nav.about">Hakkımızda</a>
        <a href="iletisim.html" class="nav-link" data-i18n="nav.contact">İletişim</a>
        <a href="iletisim.html" class="btn btn-primary" style="margin-top: 20px; width: 100%;" data-i18n="nav.meeting">Ön Görüşme</a>
    </div>
"""


# ─────────────────────────────────────────────────────────────────────────────
# SHARED FOOTER
# ─────────────────────────────────────────────────────────────────────────────
FOOTER = """
    <!-- ══ FOOTER ══ -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <!-- Col 1: Brand -->
                <div>
                    <div class="footer-logo">
                        <img src="assets/logo-full-white.png" alt="Start Akademie Logo" style="height: 56px; width: auto;">
                    </div>
                    <p style="font-size: 0.9rem; margin-bottom: 24px;" data-i18n="footer.desc">
                        Almanya'da eğitim ve kariyer hedefleriniz için kişiye özel danışmanlık.
                    </p>
                    <div class="vnn-stamp">
                        <i data-lucide="shield-check" style="width: 16px; height: 16px;"></i> VNN Üyesi Kurum
                    </div>
                </div>

                <!-- Col 2: Services -->
                <div class="footer-links">
                    <h4 data-i18n="footer.services">Hizmetler</h4>
                    <ul>
                        <li><a href="uni.html" data-i18n="nav.university">Üniversite</a></li>
                        <li><a href="dil.html" data-i18n="nav.languages">Dil Kursları</a></li>
                        <li><a href="ausbildung.html" data-i18n="nav.ausbildung">Ausbildung</a></li>
                        <li><a href="denklik.html" data-i18n="nav.recognition">Denklik</a></li>
                        <li><a href="degisim.html" data-i18n="nav.exchange">Değişim &amp; Yaz Programları</a></li>
                        <li><a href="konaklama.html" data-i18n="nav.accommodation">Konaklama</a></li>
                    </ul>
                </div>

                <!-- Col 3: Other sites -->
                <div class="footer-links">
                    <h4>Diğer Sitelerimiz</h4>
                    <ul>
                        <li><a href="https://www.startakademie.de" target="_blank" rel="noopener">Nachhilfe – startakademie.de</a></li>
                        <li><a href="https://www.startakademie.online" target="_blank" rel="noopener">Online Dil Kursları – startakademie.online</a></li>
                    </ul>
                </div>

                <!-- Col 4: Info -->
                <div class="footer-links">
                    <h4>Bilgilendirme</h4>
                    <ul>
                        <li><a href="index.html#sss">Sık Sorulan Sorular</a></li>
                        <li><a href="index.html#packages">Hizmet Paketleri</a></li>
                        <li><a href="uni.html">Üniversite Uygunluk Değerlendirmesi</a></li>
                    </ul>
                </div>

                <!-- Col 5: Corporate -->
                <div class="footer-links">
                    <h4 data-i18n="footer.corporate">Kurumsal</h4>
                    <ul>
                        <li><a href="hakkimizda.html" data-i18n="nav.about">Hakkımızda</a></li>
                        <li><a href="iletisim.html" data-i18n="nav.contact">İletişim</a></li>
                        <li><a href="impressum.html" data-i18n="footer.l1">Impressum</a></li>
                        <li><a href="datenschutz.html" data-i18n="footer.datenschutz">Datenschutz</a></li>
                    </ul>
                </div>

                <!-- Col 6: Contact -->
                <div class="footer-links">
                    <h4>İletişim</h4>
                    <ul>
                        <li><a href="https://maps.google.com/?q=Mainzer+Straße+18,+65428+Rüsselsheim" target="_blank" rel="noopener">📍 Mainzer Straße 18, 65428 Rüsselsheim am Main</a></li>
                        <li><a href="tel:+491797424790">📞 +49 179 742 47 90</a></li>
                        <li><a href="mailto:info@startakademie.com">✉️ info@startakademie.com</a></li>
                        <li><a href="https://www.instagram.com/startakademie" target="_blank" rel="noopener">📸 @startakademie</a></li>
                    </ul>
                </div>
            </div>

            <div class="footer-bottom">
                <span data-i18n="footer.copyright">&copy; 2026 Start Akademie UG (haftungsbeschränkt). Tüm Hakları Saklıdır.</span>
                <div style="display: flex; gap: 24px;">
                    <a href="impressum.html" data-i18n="footer.l1">Impressum</a>
                    <a href="datenschutz.html" data-i18n="footer.datenschutz">Datenschutz</a>
                    <a href="impressum.html">Kullanım Koşulları</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- StartBot -->
    <div id="startbot-bubble" style="position:fixed;bottom:24px;right:24px;z-index:9999;">
        <button id="startbot-btn" aria-label="StartBot"
            style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--navy));border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:0 4px 20px rgba(0,80,158,0.4);">
            <i data-lucide="bot" style="width:20px;height:20px;"></i>
        </button>
        <div id="startbot-win" style="position:absolute;bottom:60px;right:0;width:280px;height:380px;background:var(--surface);border:1px solid var(--glass-border);border-radius:16px;overflow:hidden;display:none;flex-direction:column;box-shadow:0 8px 32px rgba(0,0,0,0.25);">
            <div style="background:linear-gradient(135deg,var(--blue),var(--navy));padding:14px 16px;display:flex;align-items:center;justify-content:space-between;">
                <span style="font-size:0.85rem;font-weight:700;color:#fff;">StartBot 🤖</span>
                <button id="startbot-close" style="background:none;border:none;color:#fff;cursor:pointer;padding:2px;display:flex;"><i data-lucide="x" style="width:16px;height:16px;"></i></button>
            </div>
            <iframe src="https://www.chatbase.co/chatbot-iframe/wT-KoF8pnpTAbdMcMaorj" style="flex:1;border:none;width:100%;"></iframe>
        </div>
    </div>

    <script>
        lucide.createIcons();

        // Header scroll
        const hdr = document.getElementById('main-header');
        window.addEventListener('scroll', () => {
            hdr.classList.toggle('scrolled', window.scrollY > 60);
        });

        // Mobile menu toggle
        const mobileToggle = document.getElementById('mobile-toggle');
        const mobileDrawer = document.getElementById('mobile-menu-drawer');
        if (mobileToggle && mobileDrawer) {
            mobileToggle.addEventListener('click', () => {
                mobileDrawer.classList.toggle('open');
            });
        }

        // StartBot toggle
        const sBotBtn = document.getElementById('startbot-btn');
        const sBotClose = document.getElementById('startbot-close');
        const sBotWin = document.getElementById('startbot-win');
        if (sBotBtn && sBotWin) {
            sBotBtn.addEventListener('click', () => {
                sBotWin.style.display = sBotWin.style.display === 'flex' ? 'none' : 'flex';
            });
        }
        if (sBotClose && sBotWin) {
            sBotClose.addEventListener('click', () => { sBotWin.style.display = 'none'; });
        }

        // FAQ accordion
        document.querySelectorAll('.faq-q').forEach(btn => {
            btn.addEventListener('click', () => {
                const item = btn.closest('.faq-item');
                item.classList.toggle('open');
            });
        });

        // Language init
        document.addEventListener('DOMContentLoaded', () => {
            const savedLang = localStorage.getItem('lang') || 'tr';
            if (typeof changeLanguage === 'function') changeLanguage(savedLang);
        });
    </script>
</body>
</html>
"""


# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONTENTS
# ─────────────────────────────────────────────────────────────────────────────

def page_uni():
    return header("Almanya'da Üniversite Eğitimi", "Almanya devlet üniversitelerine başvuru, öğrenci vizesi ve dil hazırlık süreçleri için uzman danışmanlık. YKS şartları, APS, DSH ve TestDaF bilgisi.", "uni") + """
    <!-- Hero -->
    <section class="page-hero">
        <div class="container">
            <div class="badge-prep">🎓 Üniversite Danışmanlığı</div>
            <h1>Almanya'da <em>Üniversite</em> Eğitimi</h1>
            <p class="hero-sub">Devlet üniversitelerine başvurudan öğrenci vizesine, dil sınavlarından kayıt süreçlerine kadar adım adım profesyonel destek.</p>
            <a href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px;">Ücretsiz Ön Değerlendirme →</a>
        </div>
    </section>

    <!-- Overview -->
    <section class="content-section">
        <div class="container">
            <h2>Neden Almanya <em>Devlet</em> Üniversitesi?</h2>
            <p class="lead-text">Almanya'da devlet üniversitelerinde yılda yalnızca 300–400 € Semesterbeitrag ödenir; eğitim ücretsizdir. Dünya sıralamalarında üst sıralarda yer alan bu kurumlar, uluslararası tanınırlık ve kariyer imkânı sunar.</p>
            <div class="feat-grid">
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="euro" style="width:22px;height:22px;"></i></div>
                    <h3>Ücretsiz Eğitim</h3>
                    <p>Devlet üniversitelerinde harç yoktur. Yalnızca dönemlik katkı payı (Semesterbeitrag) ödenir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="globe" style="width:22px;height:22px;"></i></div>
                    <h3>Uluslararası Tanınırlık</h3>
                    <p>TU München, LMU, Heidelberg gibi kurumlar QS ve THE dünya sıralamalarında ilk 100'de yer alır.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="briefcase" style="width:22px;height:22px;"></i></div>
                    <h3>Güçlü Kariyer</h3>
                    <p>Almanya'da okuyup çalışma izni (Aufenthaltserlaubnis) ile 18 aya kadar iş arama hakkı kazanırsınız.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="shield-check" style="width:22px;height:22px;"></i></div>
                    <h3>Güvenli Süreç</h3>
                    <p>APS sertifikası, Uni-Assist, Hochschulstart adımlarını sizin için koordine ediyoruz.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="book-open" style="width:22px;height:22px;"></i></div>
                    <h3>Geniş Bölüm Seçimi</h3>
                    <p>Mühendislik, tıp, hukuk, ekonomi, mimarlık gibi yüzlerce İngilizce ve Almanca program.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="users" style="width:22px;height:22px;"></i></div>
                    <h3>Kişisel Danışman</h3>
                    <p>Başvurudan yerleşime kadar size özel bir danışman atanır; hiçbir adımı yalnız geçirmezsiniz.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Requirements -->
    <section class="content-section alt">
        <div class="container">
            <h2>Temel <em>Kabul Şartları</em></h2>
            <p class="lead-text">Almanya devlet üniversitelerine başvurabilmek için aşağıdaki temel koşullar aranmaktadır. Her üniversitenin ek gereksinimleri olabilir; danışmanınız size özel değerlendirme yapar.</p>
            <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; overflow: hidden;">
                <table class="info-table">
                    <tr>
                        <th>YKS Puanı</th>
                        <td>Türk lise diplomasıyla başvuru için YKS (ÖSYM) sınavından 4 yıllık bir programa yerleşmiş olunması şarttır.</td>
                    </tr>
                    <tr>
                        <th>APS Sertifikası</th>
                        <td>Alman Eğitim Kurumu tarafından verilen Akademik Kontrol Belgesi. Başvurudan 6–8 hafta önce hazırlanmalıdır.</td>
                    </tr>
                    <tr>
                        <th>Dil Yeterliliği</th>
                        <td>Almanca programlar için DSH-2 veya TestDaF 4×4; İngilizce programlar için IELTS 6.5+ veya TOEFL iBT 90+.</td>
                    </tr>
                    <tr>
                        <th>Bloke Hesap (Sperrkonto)</th>
                        <td>Vize başvurusu için 2025 itibarıyla yıllık yaklaşık 11.904 € bloke hesap gösterilmesi gerekir.</td>
                    </tr>
                    <tr>
                        <th>Sağlık Sigortası</th>
                        <td>Almanya'da öğrenci sigortası (gesetzliche Krankenversicherung) zorunludur.</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <!-- Process Steps -->
    <section class="content-section">
        <div class="container" style="max-width: 800px;">
            <h2>Başvuru <em>Süreci</em></h2>
            <p class="lead-text">Start Akademie ile başvuru süreci 7 adımda tamamlanır. Her adımda bir danışman sizi yönlendirir.</p>
            <ul class="step-list">
                <li>
                    <div class="step-num">1</div>
                    <div class="step-content">
                        <h4>Ücretsiz Ön Değerlendirme</h4>
                        <p>Akademik geçmişiniz, dil seviyeniz ve hedefleriniz analiz edilir; size uygun program ve üniversiteler belirlenir.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">2</div>
                    <div class="step-content">
                        <h4>APS Sertifikası Hazırlığı</h4>
                        <p>Gerekli belgeler hazırlanır, APS mülakat takvimi oluşturulur ve başvuru koordine edilir.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">3</div>
                    <div class="step-content">
                        <h4>Dil Sınavı Hazırlığı</h4>
                        <p>DSH, TestDaF veya IELTS hedef sınavına yönelik çalışma planı oluşturulur, kaynak ve pratik desteği sağlanır.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">4</div>
                    <div class="step-content">
                        <h4>Üniversite & Bölüm Başvurusu</h4>
                        <p>Uni-Assist veya doğrudan üniversite portalından başvurular hazırlanır ve takip edilir.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">5</div>
                    <div class="step-content">
                        <h4>Vize Belgelerinin Hazırlanması</h4>
                        <p>Kabul mektubu, bloke hesap, sağlık sigortası ve diğer vize evrakları eksiksiz hazırlanır.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">6</div>
                    <div class="step-content">
                        <h4>Vize Randevusu & Takibi</h4>
                        <p>Konsolosluk randevusu alınır; vize sürecinin her aşaması yakından takip edilir.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">7</div>
                    <div class="step-content">
                        <h4>Almanya'ya Varış Desteği</h4>
                        <p>Kayıt (Einschreibung), yurt başvurusu, Anmeldung ve ilk adımlar için rehberlik sunulur.</p>
                    </div>
                </li>
            </ul>
        </div>
    </section>

    <!-- FAQ -->
    <section class="content-section alt">
        <div class="container" style="max-width: 800px;">
            <h2>Sık Sorulan <em>Sorular</em></h2>
            <br>
            <div class="faq-item">
                <button class="faq-q">Almanya'da üniversite ücretsiz mi? <i data-lucide="chevron-down" class="faq-chevron" style="width:18px;height:18px;"></i></button>
                <div class="faq-a">Evet, devlet üniversitelerinde harç alınmaz. Yalnızca dönemlik katkı payı (Semesterbeitrag) ödenir; bu genellikle 250–400 € arasındadır.</div>
            </div>
            <div class="faq-item">
                <button class="faq-q">YKS puanım yeterli mi? <i data-lucide="chevron-down" class="faq-chevron" style="width:18px;height:18px;"></i></button>
                <div class="faq-a">YKS sonucu, Türk lise diplomasını Almanya'da geçerli kılmak için yeterli şartı sağlar; belirli bir puan kesimi değil, 4 yıllık bir bölüme yerleşmiş olmak yeterlidir. Detaylı değerlendirme için ön görüşme talep edin.</div>
            </div>
            <div class="faq-item">
                <button class="faq-q">APS sertifikası almak ne kadar sürer? <i data-lucide="chevron-down" class="faq-chevron" style="width:18px;height:18px;"></i></button>
                <div class="faq-a">Alman Büyükelçiliği'ndeki APS Türkiye ofisi mülakat tarihleri yoğunluğa göre değişir. Genel olarak başvurudan mülakate 4–8 hafta, sonuç alımına kadar 2–4 hafta daha geçmektedir.</div>
            </div>
            <div class="faq-item">
                <button class="faq-q">Almancam yoksa başvurabilir miyim? <i data-lucide="chevron-down" class="faq-chevron" style="width:18px;height:18px;"></i></button>
                <div class="faq-a">Evet. İngilizce dilinde sunulan yüzlerce lisans ve yüksek lisans programı mevcuttur. Almanca program isteyenler için başvurudan önce hazırlık kursu ve dil sınavı sürecini birlikte planlıyoruz.</div>
            </div>
            <div class="faq-item">
                <button class="faq-q">Vize kaç ayda çıkar? <i data-lucide="chevron-down" class="faq-chevron" style="width:18px;height:18px;"></i></button>
                <div class="faq-a">Öğrenci ulusal vizesi (Nationales Visum) başvuruları Türkiye'deki Alman Konsolosluklarında ortalama 8–12 hafta sürmektedir. Belgelerin eksiksiz olması bu süreci önemli ölçüde kısaltır.</div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section style="padding: 60px 0;">
        <div class="container">
            <div class="cta-banner">
                <h2>Üniversite Yolculuğuna Başla</h2>
                <p>Ücretsiz ön değerlendirme görüşmesiyle hangi üniversiteye, hangi bölüme başvurabileceğinizi öğrenin.</p>
                <a href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px; background:#fff; color: var(--navy);">Randevu Al →</a>
            </div>
        </div>
    </section>
""" + FOOTER


def page_dil():
    return header("Almanya'da Dil Kursları", "Almanya'da dil kursları: DSH, TestDaF, Goethe-Zertifikat, telc ve İngilizce sınavlarına hazırlık. Start Akademie dil danışmanlığı.", "dil") + """
    <!-- Hero -->
    <section class="page-hero">
        <div class="container">
            <div class="badge-prep">🗣️ Dil Eğitimi</div>
            <h1>Almanya'da <em>Dil Kursları</em></h1>
            <p class="hero-sub">DSH, TestDaF, Goethe, telc ve IELTS sınavlarına yönelik kurs seçimi, kayıt ve hazırlık süreçlerinde uzman danışmanlık.</p>
            <a href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px;">Dil Seviyen Belirle →</a>
        </div>
    </section>

    <!-- Dil kursları -->
    <section class="content-section">
        <div class="container">
            <h2>Hangi <em>Dil Sınavına</em> İhtiyacınız Var?</h2>
            <p class="lead-text">Hedeflerinize göre doğru sınav ve kurs seçimi kritik önem taşır. Aşağıdaki tablo size rehberlik eder.</p>
            <div class="feat-grid">
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="graduation-cap" style="width:22px;height:22px;"></i></div>
                    <h3>DSH</h3>
                    <p>Deutsche Sprachprüfung für den Hochschulzugang — Almanya'daki devlet üniversitelerine giriş için en yaygın kabul edilen Almanca sınavı.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="file-text" style="width:22px;height:22px;"></i></div>
                    <h3>TestDaF</h3>
                    <p>Uluslararası geçerliliğe sahip standart test. 4×4 hedefi birçok üniversite tarafından DSH muadili olarak kabul edilir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="award" style="width:22px;height:22px;"></i></div>
                    <h3>Goethe-Zertifikat</h3>
                    <p>A1'den C2'ye kadar uluslararası geçerliliği olan sertifikalar. İş vizesi ve uzun dönem oturumlar için tercih edilir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="check-circle" style="width:22px;height:22px;"></i></div>
                    <h3>telc Almanca</h3>
                    <p>Avrupa'nın önde gelen sınav kuruluşlarından biri. B1, B2 ve C1 seviyeleri özellikle entegrasyon ve iş başvurularında tercih edilir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="globe" style="width:22px;height:22px;"></i></div>
                    <h3>IELTS / TOEFL</h3>
                    <p>İngilizce dilindeki programlara başvuru için. IELTS 6.5+ veya TOEFL iBT 90+ birçok üniversite tarafından kabul edilir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="book-open" style="width:22px;height:22px;"></i></div>
                    <h3>Genel Dil Kursları</h3>
                    <p>Sıfırdan başlayanlar için A1–B2 arasında Almanca kursları. Hem online hem de yüz yüze seçenekler.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Hazırlık süreci -->
    <section class="content-section alt">
        <div class="container" style="max-width: 800px;">
            <h2>Danışmanlık <em>Süreci</em></h2>
            <ul class="step-list">
                <li>
                    <div class="step-num">1</div>
                    <div class="step-content">
                        <h4>Dil Seviyesi Testi</h4>
                        <p>Mevcut Almanca veya İngilizce seviyeniz kısa bir test ile belirlenir.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">2</div>
                    <div class="step-content">
                        <h4>Hedef Sınav Seçimi</h4>
                        <p>Üniversite hedeflerinize ve zaman çizelgenize göre en uygun sınav belirlenir.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">3</div>
                    <div class="step-content">
                        <h4>Kurs Seçimi & Kayıt</h4>
                        <p>Almanya'daki veya Türkiye'deki dil okulları ve online platformlar arasından size en uygun seçenek belirlenir.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">4</div>
                    <div class="step-content">
                        <h4>Sınav Kaydı</h4>
                        <p>Seçilen sınav için tarih ve kayıt işlemleri birlikte tamamlanır.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">5</div>
                    <div class="step-content">
                        <h4>Hazırlık Takibi</h4>
                        <p>Sınav öncesi pratik materyaller ve örnek sınavlar paylaşılır; ilerleme izlenir.</p>
                    </div>
                </li>
            </ul>
        </div>
    </section>

    <!-- CTA -->
    <section style="padding: 60px 0;">
        <div class="container">
            <div class="cta-banner">
                <h2>Dil Seviyeni Şimdi Belirle</h2>
                <p>Ücretsiz seviye tespitiyle hangi sınava, ne kadar sürede hazır olabileceğini öğren.</p>
                <a href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px; background:#fff; color: var(--navy);">Görüşme Talep Et →</a>
            </div>
        </div>
    </section>
""" + FOOTER


def page_ausbildung():
    return header("Almanya'da Ausbildung (Mesleki Eğitim)", "Almanya'da ikili mesleki eğitim sistemi (Ausbildung) hakkında bilgi, başvuru süreci ve sektör seçimi için danışmanlık.", "ausbildung") + """
    <!-- Hero -->
    <section class="page-hero">
        <div class="container">
            <div class="badge-prep">🔧 Mesleki Eğitim</div>
            <h1>Almanya'da <em>Ausbildung</em></h1>
            <p class="hero-sub">Almanya'nın dünyaca ünlü ikili mesleki eğitim sistemi ile hem çalışın hem öğrenin. Sektör seçiminden iş bulma ve vize süreçlerine kadar danışmanlık.</p>
            <div class="badge-prep" style="background: rgba(255,165,0,0.12); border-color: orange; color: orange;">⏳ Ön talep alınıyor</div>
        </div>
    </section>

    <!-- Nedir -->
    <section class="content-section">
        <div class="container">
            <h2>Ausbildung <em>Nedir?</em></h2>
            <p class="lead-text">Ausbildung, Almanya'nın en önemli eğitim sistemlerinden biridir. "İkili sistem" (duales System) olarak da bilinen bu yapıda, öğrenciler hem bir şirkette pratik eğitim alırken hem de meslek okulunda (Berufsschule) teorik eğitim görür. Süre genellikle 2–3,5 yıldır ve eğitim boyunca maaş ödenir.</p>
            <div class="feat-grid">
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="euro" style="width:22px;height:22px;"></i></div>
                    <h3>Eğitim Maaşı</h3>
                    <p>Ausbildung süresince aylık 600–1.200 € arasında değişen eğitim ücreti (Ausbildungsvergütung) alırsınız.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="hard-hat" style="width:22px;height:22px;"></i></div>
                    <h3>Pratik Deneyim</h3>
                    <p>Haftanın 3–4 günü gerçek iş ortamında çalışarak mesleğinizi öğrenirsiniz.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="award" style="width:22px;height:22px;"></i></div>
                    <h3>Tanınan Sertifika</h3>
                    <p>IHK veya HWK tarafından verilen sertifika, Avrupa genelinde geçerlidir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="trending-up" style="width:22px;height:22px;"></i></div>
                    <h3>Kariyer Yolu</h3>
                    <p>Ausbildung sonrası tam zamanlı işe geçiş çok yaygındır; aynı şirkette kalma oranı yüksektir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="map-pin" style="width:22px;height:22px;"></i></div>
                    <h3>Oturma İzni</h3>
                    <p>Ausbildung vizesi (§16a AufenthG) ile Almanya'da 3 yıla kadar yasal ikametinizi sürdürebilirsiniz.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="graduation-cap" style="width:22px;height:22px;"></i></div>
                    <h3>Üst Eğitim Hakkı</h3>
                    <p>Ausbildung sonrası Meister veya teknik üniversite programlarına devam etme imkânı mevcuttur.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Sektörler -->
    <section class="content-section alt">
        <div class="container">
            <h2>Popüler <em>Ausbildung Sektörleri</em></h2>
            <p class="lead-text">Almanya'da yaklaşık 325 tanınan Ausbildung mesleği bulunmaktadır. En çok talep gören alanlar şunlardır:</p>
            <div class="feat-grid">
                <div class="feat-card"><div class="icon-wrap"><i data-lucide="monitor" style="width:22px;height:22px;"></i></div><h3>Bilişim (IT)</h3><p>Fachinformatiker, IT-Systemkaufmann gibi pozisyonlar en yüksek maaşlı stajyer pozisyonlarındandır.</p></div>
                <div class="feat-card"><div class="icon-wrap"><i data-lucide="activity" style="width:22px;height:22px;"></i></div><h3>Sağlık</h3><p>Pflegefachmann/Pflegefachfrau, MTA ve diğer sağlık meslek alanlarında ciddi iş gücü açığı mevcuttur.</p></div>
                <div class="feat-card"><div class="icon-wrap"><i data-lucide="zap" style="width:22px;height:22px;"></i></div><h3>Elektrik & Elektronik</h3><p>Elektroniker ve Mechatroniker pozisyonları otomotiv ve enerji sektöründe çok talep görmektedir.</p></div>
                <div class="feat-card"><div class="icon-wrap"><i data-lucide="utensils" style="width:22px;height:22px;"></i></div><h3>Gastronomi & Otelcilik</h3><p>Koch, Restaurantfachmann ve Hotelfachmann pozisyonları turizm sektöründe vazgeçilmezdir.</p></div>
                <div class="feat-card"><div class="icon-wrap"><i data-lucide="truck" style="width:22px;height:22px;"></i></div><h3>Lojistik</h3><p>Fachkraft für Lagerlogistik gibi pozisyonlar büyüyen e-ticaret sektörüyle birlikte genişlemektedir.</p></div>
                <div class="feat-card"><div class="icon-wrap"><i data-lucide="building" style="width:22px;height:22px;"></i></div><h3>Finans & Bankacılık</h3><p>Bankkaufmann gibi pozisyonlar yüksek teorik içerikli ve saygın meslek eğitimleri arasındadır.</p></div>
            </div>
        </div>
    </section>

    <!-- Ön talep -->
    <section style="padding: 60px 0;">
        <div class="container">
            <div class="cta-banner">
                <h2>Ausbildung Başvurusuna Hazır mısın?</h2>
                <p>Şu an ön talep topluyoruz. Formunu doldur, süreç başlar başlamaz seni bilgilendirelim.</p>
                <a href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px; background:#fff; color: var(--navy);">Ön Talep Bırak →</a>
            </div>
        </div>
    </section>
""" + FOOTER


def page_denklik():
    return header("Diploma ve Mesleki Denklik – Almanya", "Türk diplomalarının Almanya'da tanınması, Anabin ve ZAB değerlendirme süreçleri hakkında uzman danışmanlık.", "denklik") + """
    <!-- Hero -->
    <section class="page-hero">
        <div class="container">
            <div class="badge-prep">📜 Diploma Denkliği</div>
            <h1>Diploma ve Mesleki <em>Denklik</em></h1>
            <p class="hero-sub">Türkiye'den getirdiğiniz diplomanın Almanya'da tanınması için Anabin, ZAB ve KMK değerlendirme süreçlerinde adım adım destek.</p>
            <div class="badge-prep" style="background: rgba(255,165,0,0.12); border-color: orange; color: orange;">⏳ Ön talep alınıyor</div>
        </div>
    </section>

    <!-- Genel -->
    <section class="content-section">
        <div class="container">
            <h2>Denklik Neden <em>Önemli?</em></h2>
            <p class="lead-text">Almanya'da bir meslekte çalışmak veya yüksek lisans programına devam etmek için yabancı diplomanın tanınması (Anerkennung) gerekebilir. Doğru süreç seçilmezse onlarca ay kaybedebilirsiniz.</p>
            <div class="feat-grid">
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="database" style="width:22px;height:22px;"></i></div>
                    <h3>Anabin Veritabanı</h3>
                    <p>Alman akademik değerlendirme kurumu HRK'nın veritabanı; Türk üniversitelerinin Almanya'daki statüsünü gösterir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="file-check" style="width:22px;height:22px;"></i></div>
                    <h3>ZAB Değerlendirmesi</h3>
                    <p>Zentralstelle für ausländisches Bildungswesen — akademik diplomalar için resmi denklik belgesi veren kurum.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="briefcase" style="width:22px;height:22px;"></i></div>
                    <h3>Mesleki Denklik</h3>
                    <p>Regulated meslekler (doktor, hemşire, mimar vb.) için eyalet makamlarına ayrı başvuru gerekir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="book-open" style="width:22px;height:22px;"></i></div>
                    <h3>Statement of Comparability</h3>
                    <p>KMK/ZAB tarafından verilen Almanca üniversite derecenizi karşılaştıran resmi belge.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Süreç -->
    <section class="content-section alt">
        <div class="container" style="max-width: 800px;">
            <h2>Değerlendirme <em>Süreci</em></h2>
            <ul class="step-list">
                <li>
                    <div class="step-num">1</div>
                    <div class="step-content">
                        <h4>Belge Analizi</h4>
                        <p>Diplomanız, transkriptleriniz ve diğer akademik belgeleriniz incelenir; hangi denklik yolunun uygun olduğu belirlenir.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">2</div>
                    <div class="step-content">
                        <h4>Anabin Kontrolü</h4>
                        <p>Mezun olduğunuz üniversitenin Almanya'daki tanınırlık durumu araştırılır.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">3</div>
                    <div class="step-content">
                        <h4>Başvuru Hazırlığı</h4>
                        <p>ZAB, eyalet makamı veya ilgili üniversiteye iletilecek evraklar eksiksiz hazırlanır.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">4</div>
                    <div class="step-content">
                        <h4>Tercüme ve Apostil</h4>
                        <p>Yemin etmiş tercüman belgesi ve apostil işlemleri için yönlendirme yapılır.</p>
                    </div>
                </li>
                <li>
                    <div class="step-num">5</div>
                    <div class="step-content">
                        <h4>Takip & Sonuç</h4>
                        <p>Başvuru sonrası süreç yakından takip edilir; eksik belge talepleri anında karşılanır.</p>
                    </div>
                </li>
            </ul>
        </div>
    </section>

    <!-- CTA -->
    <section style="padding: 60px 0;">
        <div class="container">
            <div class="cta-banner">
                <h2>Diplomanın Almanya'daki Değerini Öğren</h2>
                <p>Ücretsiz bir ön değerlendirme ile denklik sürecinizi nasıl planlayacağınızı konuşalım.</p>
                <a href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px; background:#fff; color: var(--navy);">Ön Talep Bırak →</a>
            </div>
        </div>
    </section>
""" + FOOTER


def page_degisim():
    return header("Değişim ve Yaz Programları – Almanya", "Almanya'da yaz dil okulları, kısa dönem değişim programları ve akademik yaz kampları hakkında bilgi ve danışmanlık.", "degisim") + """
    <!-- Hero -->
    <section class="page-hero">
        <div class="container">
            <div class="badge-prep">☀️ Değişim & Yaz Programları</div>
            <h1>Değişim ve <em>Yaz Programları</em></h1>
            <p class="hero-sub">Almanya'da 2 haftadan 3 aya kadar yaz dil okulları, üniversite yaz kampları ve kısa dönem değişim programlarına katılın.</p>
            <div class="badge-prep" style="background: rgba(255,165,0,0.12); border-color: orange; color: orange;">⏳ Hazırlık aşamasında</div>
        </div>
    </section>

    <!-- Programlar -->
    <section class="content-section">
        <div class="container">
            <h2>Program <em>Türleri</em></h2>
            <p class="lead-text">Kısa süreli deneyimler, uzun dönem eğitim kararını vermeden önce Almanya'yı tanımanın en iyi yoludur.</p>
            <div class="feat-grid">
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="sun" style="width:22px;height:22px;"></i></div>
                    <h3>Yaz Dil Okulu</h3>
                    <p>2–8 haftalık yoğun Almanca kursları. Sabah ders, öğleden sonra kültürel aktiviteler ve şehir gezileri.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="graduation-cap" style="width:22px;height:22px;"></i></div>
                    <h3>Üniversite Yaz Kampı</h3>
                    <p>TU Darmstadt, Goethe Üniversitesi gibi kurumların düzenlediği akademik içerikli 3–4 haftalık programlar.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="users" style="width:22px;height:22px;"></i></div>
                    <h3>Gençlik Değişimi</h3>
                    <p>15–25 yaş arası gençler için Türk-Alman kültür değişim programları. Avrupa gençlik fonları ile desteklenebilir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="flask-conical" style="width:22px;height:22px;"></i></div>
                    <h3>Araştırma Stajı</h3>
                    <p>Lisans veya yüksek lisans öğrencileri için Almanya'daki araştırma enstitülerinde kısa dönem staj programları.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Ön talep CTA -->
    <section style="padding: 60px 0;">
        <div class="container">
            <div class="cta-banner">
                <h2>2026 Yaz Programları İçin Ön Kaydını Yaptır</h2>
                <p>Program detayları hazırlanıyor. Şimdi ön talebinizi bırakın, açılır açılmaz bilgilendirelim.</p>
                <a href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px; background:#fff; color: var(--navy);">Ön Talep Bırak →</a>
            </div>
        </div>
    </section>
""" + FOOTER


def page_konaklama():
    return header("Almanya Öğrenci Konaklaması", "Almanya'da öğrenci yurtları (Studentenwohnheim), özel kira ve paylaşımlı ev (WG) seçenekleri hakkında danışmanlık.", "konaklama") + """
    <!-- Hero -->
    <section class="page-hero">
        <div class="container">
            <div class="badge-prep">🏠 Konaklama</div>
            <h1>Almanya'da <em>Öğrenci Konaklaması</em></h1>
            <p class="hero-sub">Studentenwohnheim, WG ve özel kira arasındaki farkları anlayın; size en uygun konaklama çözümünü birlikte bulalım.</p>
            <div class="badge-prep" style="background: rgba(255,165,0,0.12); border-color: orange; color: orange;">⏳ Hazırlık aşamasında</div>
        </div>
    </section>

    <!-- Konaklama türleri -->
    <section class="content-section">
        <div class="container">
            <h2>Konaklama <em>Seçenekleri</em></h2>
            <p class="lead-text">Almanya'da öğrenci konaklaması üç temel kategoride değerlendirilir. Her birinin avantajları ve dezavantajları farklıdır.</p>
            <div class="feat-grid">
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="building-2" style="width:22px;height:22px;"></i></div>
                    <h3>Studentenwohnheim (Öğrenci Yurdu)</h3>
                    <p>Üniversite veya Studentenwerk tarafından işletilen yurtlar. Aylık 200–400 € arasında uygun fiyatlı seçenekler sunar; ancak bekleme listeleri uzun olabilir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="users" style="width:22px;height:22px;"></i></div>
                    <h3>WG (Wohngemeinschaft)</h3>
                    <p>Paylaşımlı ev sistemi. Mutfak ve banyolar ortak kullanılır, oda kiraları genellikle 300–600 € arasındadır. Sosyalleşme açısından idealdir.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="home" style="width:22px;height:22px;"></i></div>
                    <h3>Özel Kira</h3>
                    <p>Tek başına kiralık daire. Frankfurt gibi büyük şehirlerde 600–1.200 € arasında değişir. Kapora ve gerekli belgeler için hazırlıklı olunmalıdır.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="hotel" style="width:22px;height:22px;"></i></div>
                    <h3>İlk Ay Geçici Çözüm</h3>
                    <p>Varmadan önce kalıcı yer bulamayanlar için ilk haftalara yönelik geçici konaklama seçenekleri (hostel, kurumsal yurt) araştırılır.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Önemli bilgiler -->
    <section class="content-section alt">
        <div class="container" style="max-width: 800px;">
            <h2>Bilmeniz <em>Gerekenler</em></h2>
            <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; overflow: hidden;">
                <table class="info-table">
                    <tr>
                        <th>Anmeldung</th>
                        <td>Almanya'ya vardıktan sonra 14 gün içinde ikamet adresinizi belediyeye (Einwohnermeldeamt) tescil ettirmeniz zorunludur.</td>
                    </tr>
                    <tr>
                        <th>Kapora (Kaution)</th>
                        <td>Genellikle 1–3 aylık kira tutarında kapora (Kaution) istenir. Kira sözleşmesi bitiminde iade edilir.</td>
                    </tr>
                    <tr>
                        <th>Schufa</th>
                        <td>Ev sahipleri çoğunlukla Schufa kredi raporu ister. Yeni gelenler için bu bazen sorun yaratır; alternatif belgeler sunulabilir.</td>
                    </tr>
                    <tr>
                        <th>WG-Gesucht</th>
                        <td>En popüler kiralık ilan platformu. Profil oluşturarak ilanları takip etmek ve hızlı başvurmak önemlidir.</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section style="padding: 60px 0;">
        <div class="container">
            <div class="cta-banner">
                <h2>Konaklama Desteği Al</h2>
                <p>Almanya'ya gitmeden önce nerede kalacağınızı planlamak için ön talebinizi bırakın.</p>
                <a href="iletisim.html" class="btn btn-primary" style="font-size:1rem; padding:14px 32px; background:#fff; color: var(--navy);">Ön Talep Bırak →</a>
            </div>
        </div>
    </section>
""" + FOOTER


def page_hakkimizda():
    return header("Hakkımızda – Start Akademie", "Start Akademie hakkında: kuruluş hikayesi, ekip, misyon ve Almanya eğitim danışmanlığı vizyonu.", "hakkimizda") + """
    <!-- Hero -->
    <section class="page-hero">
        <div class="container">
            <div class="badge-prep">🏛️ Kurumsal</div>
            <h1>Start Akademie <em>Hakkında</em></h1>
            <p class="hero-sub">Rüsselsheim am Main merkezli Start Akademie UG, Almanya'da yaşayan ve buraya gelmeyi planlayan bireylerin eğitim yolculuklarında güvenilir rehberi olmayı misyon edinmiştir.</p>
        </div>
    </section>

    <!-- Hikaye -->
    <section class="content-section">
        <div class="container" style="max-width: 860px;">
            <h2>Biz <em>Kimiz?</em></h2>
            <p class="lead-text">Start Akademie, Frankfurt'un hemen yanı başında, Rüsselsheim am Main'da Mevlüt Uysal tarafından kurulmuştur. Hem yerel okul öğrencilerine ders desteği (Nachhilfe) sunan hem de yurt dışından Almanya'ya gelmek isteyen bireylere danışmanlık veren bir eğitim merkezi olarak büyüdük.</p>
            <p class="lead-text">Bugün iki temel misyonumuzu sürdürüyoruz: <strong>Nachhilfe</strong> ile Rüsselsheim ve çevresindeki lise öğrencilerini akademik olarak desteklemek; <strong>danışmanlık</strong> hizmetiyle Türkiye'den ve diğer ülkelerden gelen adayların Almanya devlet üniversitelerine, Ausbildung programlarına ve dil kurslarına güvenli şekilde ulaşmalarını sağlamak.</p>

            <div class="feat-grid" style="margin-top: 40px;">
                <div class="feat-card" style="text-align:center;">
                    <div style="font-family: var(--font-serif); font-size: 2.5rem; color: var(--gold); margin-bottom: 8px;">300+</div>
                    <h3>Danışmanlık Görüşmesi</h3>
                    <p>Şimdiye kadar gerçekleştirilen ön değerlendirme ve danışmanlık görüşmesi sayısı.</p>
                </div>
                <div class="feat-card" style="text-align:center;">
                    <div style="font-family: var(--font-serif); font-size: 2.5rem; color: var(--gold); margin-bottom: 8px;">7+</div>
                    <h3>Yıl Deneyim</h3>
                    <p>Almanya'da eğitim ve danışmanlık alanında kesintisiz hizmet.</p>
                </div>
                <div class="feat-card" style="text-align:center;">
                    <div style="font-family: var(--font-serif); font-size: 2.5rem; color: var(--gold); margin-bottom: 8px;">VNN</div>
                    <h3>Üye Kurum</h3>
                    <p>Verband für Nachhilfe- und Nachmittagsangebote üyesi, tanınan Lernförderanbieter.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Misyon / Vizyon -->
    <section class="content-section alt">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
                <div>
                    <h2>🎯 <em>Misyonumuz</em></h2>
                    <p style="color: var(--text-muted); line-height: 1.8;">Her bireyin eğitim hedeflerine ulaşmasını kolaylaştırmak. Almanya'ya gelmek isteyen adaylara doğru bilgi, güvenilir süreç ve kişiye özel rehberlik sunmak. Yanlış yönlendirme veya belirsiz beklentilerle zaman ve para kaybını engellemek.</p>
                </div>
                <div>
                    <h2>🔭 <em>Vizyonumuz</em></h2>
                    <p style="color: var(--text-muted); line-height: 1.8;">Almanya'da eğitim ve kariyer fırsatlarına erişimi demokratikleştiren; şeffaf, dijital ve güvenilir bir danışmanlık platformu olmak. Nachhilfe'den üniversite danışmanlığına, dil kurslarından Ausbildung'a kadar bütüncül bir eğitim ekosistemine liderlik etmek.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Değerler -->
    <section class="content-section">
        <div class="container">
            <h2>Temel <em>Değerlerimiz</em></h2>
            <div class="feat-grid">
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="shield" style="width:22px;height:22px;"></i></div>
                    <h3>Şeffaflık</h3>
                    <p>Süreçler, ücretler ve beklentiler konusunda tam şeffaflık. Sizi yanıltacak hiçbir vaat verilmez.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="user-check" style="width:22px;height:22px;"></i></div>
                    <h3>Kişiselleştirme</h3>
                    <p>Her danışanımızın koşulları farklıdır. Tek tip değil, kişiye özel çözümler üretiriz.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="clock" style="width:22px;height:22px;"></i></div>
                    <h3>Güvenilirlik</h3>
                    <p>Söz verdiğimiz iletişim ve geri bildirim sürelerine mutlaka uyarız.</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap"><i data-lucide="leaf" style="width:22px;height:22px;"></i></div>
                    <h3>Etik</h3>
                    <p>Garanti verilemeyen sonuçlar için garanti iddiasında bulunmayız. Gerçekçi beklentiler yönetiriz.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Adres -->
    <section class="content-section alt">
        <div class="container" style="max-width: 720px; text-align: center;">
            <h2>Bizi <em>Ziyaret Edin</em></h2>
            <p style="color: var(--text-muted); margin-bottom: 32px;">Merkezimiz Frankfurt yakınlarında, Rüsselsheim am Main'dadır. Yüz yüze görüşmeler için randevu talep edebilirsiniz.</p>
            <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 32px;">
                <p style="font-size: 1rem; color: var(--text); line-height: 2;">
                    <strong>Start Akademie UG (haftungsbeschränkt)</strong><br>
                    Mainzer Straße 18<br>
                    65428 Rüsselsheim am Main<br>
                    📞 <a href="tel:+491797424790" style="color: var(--gold);">+49 179 742 47 90</a><br>
                    ✉️ <a href="mailto:info@startakademie.com" style="color: var(--gold);">info@startakademie.com</a>
                </p>
                <a href="https://maps.google.com/?q=Mainzer+Straße+18,+65428+Rüsselsheim+am+Main" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top: 16px;">Google Maps'te Aç →</a>
            </div>
        </div>
    </section>
""" + FOOTER


def page_iletisim():
    return header("İletişim & Randevu – Start Akademie", "Start Akademie ile iletişime geçin. Ücretsiz ön görüşme ve ayrıntılı ön değerlendirme formu için buraya tıklayın.", "iletisim") + """
    <!-- Hero -->
    <section class="page-hero">
        <div class="container">
            <div class="badge-prep">📅 Randevu & İletişim</div>
            <h1>Bize <em>Ulaşın</em></h1>
            <p class="hero-sub">Kısa tanışma görüşmesi veya ayrıntılı ön değerlendirme formuyla sürecinizi başlatın.</p>
        </div>
    </section>

    <!-- İki form -->
    <section class="content-section">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: start;">

                <!-- Form 1: Kısa tanışma -->
                <div class="form-card">
                    <h3>⚡ Kısa Tanışma Görüşmesi</h3>
                    <p class="form-sub">15 dakikalık ücretsiz görüşme için formu doldurun. En geç 1 iş günü içinde size ulaşıyoruz.</p>
                    <form id="form-tanis" action="https://formspree.io/f/xdkoknzy" method="POST" onsubmit="handleSubmit(event, 'form-tanis')">
                        <div class="form-group">
                            <label for="tanis-ad">Ad Soyad *</label>
                            <input type="text" id="tanis-ad" name="ad_soyad" required placeholder="Adınız Soyadınız">
                        </div>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="tanis-email">E-posta *</label>
                                <input type="email" id="tanis-email" name="email" required placeholder="email@domain.com">
                            </div>
                            <div class="form-group">
                                <label for="tanis-tel">Telefon / WhatsApp</label>
                                <input type="tel" id="tanis-tel" name="telefon" placeholder="+90 5XX XXX XXXX">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="tanis-konu">Konu *</label>
                            <select id="tanis-konu" name="konu" required>
                                <option value="">Seçiniz...</option>
                                <option value="universite">Almanya Üniversite Danışmanlığı</option>
                                <option value="dil">Dil Kursu & Sınav Hazırlığı</option>
                                <option value="ausbildung">Ausbildung</option>
                                <option value="denklik">Diploma Denkliği</option>
                                <option value="degisim">Değişim / Yaz Programı</option>
                                <option value="konaklama">Konaklama</option>
                                <option value="diger">Diğer</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="tanis-mesaj">Kısa Notunuz</label>
                            <textarea id="tanis-mesaj" name="mesaj" placeholder="Merak ettiklerinizi kısaca yazın..."></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width:100%; padding:14px; font-size:1rem;">Görüşme Talep Et →</button>
                        <div id="form-tanis-msg" style="display:none; margin-top:16px; padding:12px; border-radius:8px; font-size:0.9rem;"></div>
                    </form>
                </div>

                <!-- Form 2: Ayrıntılı Ön Değerlendirme -->
                <div class="form-card">
                    <h3>📋 Ayrıntılı Ön Değerlendirme</h3>
                    <p class="form-sub">Daha kapsamlı bir analiz için detayları paylaşın. Danışmanınız 48 saat içinde kişiselleştirilmiş bir değerlendirme sunar.</p>
                    <form id="form-deger" action="https://formspree.io/f/xdkoknzy" method="POST" onsubmit="handleSubmit(event, 'form-deger')">
                        <div class="form-row">
                            <div class="form-group">
                                <label for="d-ad">Ad Soyad *</label>
                                <input type="text" id="d-ad" name="ad_soyad" required placeholder="Ad Soyad">
                            </div>
                            <div class="form-group">
                                <label for="d-yas">Doğum Yılı</label>
                                <input type="number" id="d-yas" name="dogum_yili" placeholder="2000" min="1970" max="2010">
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="d-email">E-posta *</label>
                                <input type="email" id="d-email" name="email" required placeholder="email@domain.com">
                            </div>
                            <div class="form-group">
                                <label for="d-tel">Telefon / WhatsApp *</label>
                                <input type="tel" id="d-tel" name="telefon" required placeholder="+90 5XX XXX XXXX">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="d-hedef">Hedef Hizmet *</label>
                            <select id="d-hedef" name="hedef_hizmet" required>
                                <option value="">Seçiniz...</option>
                                <option value="universite_lisans">Üniversite – Lisans</option>
                                <option value="universite_yuksek">Üniversite – Yüksek Lisans / Doktora</option>
                                <option value="ausbildung">Ausbildung</option>
                                <option value="dil_kursu">Dil Kursu</option>
                                <option value="denklik">Diploma Denkliği</option>
                                <option value="degisim_yaz">Değişim / Yaz Programı</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="d-egitim">Mevcut Eğitim Durumu *</label>
                            <select id="d-egitim" name="egitim_durumu" required>
                                <option value="">Seçiniz...</option>
                                <option value="lise">Lise öğrencisi / mezunu</option>
                                <option value="universite">Üniversite öğrencisi / mezunu</option>
                                <option value="yuksek">Yüksek lisans mezunu</option>
                                <option value="calisan">Çalışan profesyonel</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="d-dil">Almanca Seviyesi</label>
                            <select id="d-dil" name="almanca_seviye">
                                <option value="">Seçiniz...</option>
                                <option value="yok">Hiç yok</option>
                                <option value="A1-A2">A1–A2</option>
                                <option value="B1-B2">B1–B2</option>
                                <option value="C1+">C1 ve üzeri</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="d-takvim">Hedef Başlangıç Tarihi</label>
                            <select id="d-takvim" name="baslangic_tarihi">
                                <option value="">Seçiniz...</option>
                                <option value="2025ws">2025 Kış Dönemi</option>
                                <option value="2026ss">2026 Yaz Dönemi</option>
                                <option value="2026ws">2026 Kış Dönemi</option>
                                <option value="daha_sonra">Henüz belirlemedim</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="d-not">Ek Notlar</label>
                            <textarea id="d-not" name="ek_notlar" placeholder="Önceki başvurular, özel koşullar, bölüm tercihleri..."></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width:100%; padding:14px; font-size:1rem;">Değerlendirme Talebi Gönder →</button>
                        <div id="form-deger-msg" style="display:none; margin-top:16px; padding:12px; border-radius:8px; font-size:0.9rem;"></div>
                    </form>
                </div>

            </div>
        </div>
    </section>

    <!-- Diğer iletişim -->
    <section class="content-section alt">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; text-align: center;">
                <div class="feat-card">
                    <div class="icon-wrap" style="margin: 0 auto 16px;"><i data-lucide="map-pin" style="width:22px;height:22px;"></i></div>
                    <h3>Adres</h3>
                    <p>Mainzer Straße 18<br>65428 Rüsselsheim am Main<br>Deutschland</p>
                    <a href="https://maps.google.com/?q=Mainzer+Straße+18,+65428+Rüsselsheim" target="_blank" style="color: var(--gold); font-size:0.85rem;">Haritada Göster →</a>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap" style="margin: 0 auto 16px;"><i data-lucide="phone" style="width:22px;height:22px;"></i></div>
                    <h3>Telefon & WhatsApp</h3>
                    <p><a href="tel:+491797424790" style="color: var(--gold);">+49 179 742 47 90</a></p>
                    <p style="font-size:0.82rem; color:var(--text-muted);">Pzt–Cum 09:00–18:00</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap" style="margin: 0 auto 16px;"><i data-lucide="mail" style="width:22px;height:22px;"></i></div>
                    <h3>E-posta</h3>
                    <p><a href="mailto:info@startakademie.com" style="color: var(--gold);">info@startakademie.com</a></p>
                    <p style="font-size:0.82rem; color:var(--text-muted);">1 iş günü içinde yanıt</p>
                </div>
                <div class="feat-card">
                    <div class="icon-wrap" style="margin: 0 auto 16px;"><i data-lucide="instagram" style="width:22px;height:22px;"></i></div>
                    <h3>Instagram</h3>
                    <p><a href="https://www.instagram.com/startakademie" target="_blank" rel="noopener" style="color: var(--gold);">@startakademie</a></p>
                    <p style="font-size:0.82rem; color:var(--text-muted);">DM ile de ulaşabilirsiniz</p>
                </div>
            </div>
        </div>
    </section>

    <script>
    async function handleSubmit(e, formId) {
        e.preventDefault();
        const form = e.target;
        const msgDiv = document.getElementById(formId + '-msg');
        const btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;
        btn.textContent = 'Gönderiliyor...';
        try {
            const res = await fetch(form.action, {
                method: 'POST',
                body: new FormData(form),
                headers: { 'Accept': 'application/json' }
            });
            if (res.ok) {
                msgDiv.style.display = 'block';
                msgDiv.style.background = 'rgba(34,197,94,0.12)';
                msgDiv.style.border = '1px solid #22c55e';
                msgDiv.style.color = '#22c55e';
                msgDiv.textContent = '✅ Talebiniz alındı! En kısa sürede size ulaşacağız.';
                form.reset();
            } else {
                throw new Error();
            }
        } catch {
            msgDiv.style.display = 'block';
            msgDiv.style.background = 'rgba(239,68,68,0.12)';
            msgDiv.style.border = '1px solid #ef4444';
            msgDiv.style.color = '#ef4444';
            msgDiv.textContent = '❌ Bir hata oluştu. Lütfen info@startakademie.com adresine e-posta gönderin.';
        }
        btn.disabled = false;
        btn.textContent = 'Gönder →';
    }
    </script>
""" + FOOTER


def page_impressum():
    return header("Impressum – Start Akademie", "Start Akademie UG Impressum — yasal bilgiler, sorumlu kişi ve iletişim bilgileri.", "") + """
    <section class="page-hero" style="padding: 120px 0 60px;">
        <div class="container">
            <h1>Impressum</h1>
            <p class="hero-sub">Yasal Bilgiler / Angaben gemäß § 5 TMG</p>
        </div>
    </section>

    <section class="content-section">
        <div class="container" style="max-width: 760px;">
            <div class="form-card">
                <h3>Anbieter</h3>
                <p>
                    <strong>Start Akademie UG (haftungsbeschränkt)</strong><br>
                    Mainzer Straße 18<br>
                    65428 Rüsselsheim am Main<br>
                    Deutschland
                </p>

                <h3 style="margin-top: 32px;">Vertreten durch / Sorumlu Kişi</h3>
                <p>Mevlüt Uysal (Geschäftsführer)</p>

                <h3 style="margin-top: 32px;">Kontakt / İletişim</h3>
                <p>
                    Telefon: <a href="tel:+491797424790" style="color: var(--gold);">+49 179 742 47 90</a><br>
                    E-Mail: <a href="mailto:info@startakademie.com" style="color: var(--gold);">info@startakademie.com</a><br>
                    Web: <a href="https://www.startakademie.com" style="color: var(--gold);">www.startakademie.com</a>
                </p>

                <h3 style="margin-top: 32px;">Registergericht / Ticaret Sicili</h3>
                <p>Amtsgericht Darmstadt<br>
                Handelsregisternummer: (aşamasında güncelleme yapılacaktır)</p>

                <h3 style="margin-top: 32px;">Umsatzsteuer-ID / Vergi Numarası</h3>
                <p>Vergi numarası ilgili makamdan alındıktan sonra buraya eklenecektir.</p>

                <h3 style="margin-top: 32px;">Verantwortlich für den Inhalt / İçerik Sorumlusu</h3>
                <p>Mevlüt Uysal<br>Mainzer Straße 18<br>65428 Rüsselsheim am Main</p>

                <h3 style="margin-top: 32px;">Haftungsausschluss / Sorumluluk Reddi</h3>
                <p style="color: var(--text-muted); line-height: 1.8; font-size: 0.9rem;">
                    Die Inhalte unserer Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich.
                </p>

                <h3 style="margin-top: 32px;">Urheberrecht / Telif Hakkı</h3>
                <p style="color: var(--text-muted); line-height: 1.8; font-size: 0.9rem;">
                    Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.
                </p>
            </div>
        </div>
    </section>
""" + FOOTER


def page_datenschutz():
    return header("Datenschutzerklärung – Start Akademie", "Start Akademie gizlilik politikası ve DSGVO / KVKK uyumlu veri koruma beyannamesi.", "") + """
    <section class="page-hero" style="padding: 120px 0 60px;">
        <div class="container">
            <h1>Datenschutzerklärung</h1>
            <p class="hero-sub">Gizlilik Politikası / DSGVO &amp; KVKK Uyum Beyannamesi</p>
        </div>
    </section>

    <section class="content-section">
        <div class="container" style="max-width: 760px;">
            <div class="form-card" style="gap: 0;">

                <h3>1. Veri Sorumlusu</h3>
                <p style="color: var(--text-muted); line-height: 1.8;">
                    <strong>Start Akademie UG (haftungsbeschränkt)</strong><br>
                    Mainzer Straße 18, 65428 Rüsselsheim am Main<br>
                    E-posta: <a href="mailto:info@startakademie.com" style="color: var(--gold);">info@startakademie.com</a>
                </p>

                <h3 style="margin-top: 32px;">2. Toplanan Veriler</h3>
                <p style="color: var(--text-muted); line-height: 1.8;">
                    Web sitemizi ziyaret ettiğinizde veya iletişim formlarını doldurduğunuzda aşağıdaki kişisel veriler işlenebilir:
                </p>
                <ul style="color: var(--text-muted); line-height: 2; padding-left: 20px;">
                    <li>Ad, soyad</li>
                    <li>E-posta adresi</li>
                    <li>Telefon numarası</li>
                    <li>Eğitim geçmişi ve hedefler (isteğe bağlı form alanları)</li>
                    <li>Teknik veriler: IP adresi, tarayıcı türü, ziyaret süresi (log dosyaları)</li>
                </ul>

                <h3 style="margin-top: 32px;">3. Verilerin Kullanım Amacı</h3>
                <p style="color: var(--text-muted); line-height: 1.8;">
                    Toplanan veriler yalnızca şu amaçlarla kullanılır: danışmanlık görüşmesi organizasyonu, hizmet bilgilendirmesi, teknik web site işletimi. Veriler üçüncü taraflarla pazarlama amacıyla paylaşılmaz.
                </p>

                <h3 style="margin-top: 32px;">4. Çerezler (Cookies)</h3>
                <p style="color: var(--text-muted); line-height: 1.8;">
                    Web sitemiz yalnızca teknik gereklilik nedeniyle zorunlu çerezler kullanmaktadır. Analitik veya reklam çerezleri için açık onayınız alınır. Tercihlerinizi dilediğiniz zaman tarayıcı ayarlarınızdan değiştirebilirsiniz.
                </p>

                <h3 style="margin-top: 32px;">5. Haklarınız (DSGVO Art. 15–22)</h3>
                <p style="color: var(--text-muted); line-height: 1.8;">
                    Kişisel verilerinize erişim, düzeltme, silme ve işlemeyi kısıtlama haklarına sahipsiniz. Bu haklarınızı kullanmak için <a href="mailto:info@startakademie.com" style="color: var(--gold);">info@startakademie.com</a> adresine yazabilirsiniz. Şikâyet hakkınız için Alman Veri Koruma Otoritesi (BfDI) veya ilgili Eyalet Veri Koruma Otoritesi'ne başvurabilirsiniz.
                </p>

                <h3 style="margin-top: 32px;">6. Veri Saklama Süresi</h3>
                <p style="color: var(--text-muted); line-height: 1.8;">
                    Kişisel veriler, danışmanlık ilişkisinin sona ermesinden itibaren yasal saklama yükümlülükleri (Almanya'da genellikle 6–10 yıl) çerçevesinde saklanır ve ardından güvenli şekilde silinir.
                </p>

                <h3 style="margin-top: 32px;">7. Üçüncü Taraf Hizmetler</h3>
                <p style="color: var(--text-muted); line-height: 1.8;">
                    İletişim formları Formspree altyapısını kullanmaktadır. StartBot AI chatbot Chatbase altyapısıyla çalışmaktadır. Google Fonts tipografi hizmeti kullanılmaktadır. Her üçüncü tarafın kendi gizlilik politikası geçerlidir.
                </p>

                <p style="margin-top: 32px; font-size: 0.82rem; color: var(--text-muted);">Son güncelleme: Temmuz 2026</p>
            </div>
        </div>
    </section>
""" + FOOTER


def page_404():
    return header("Sayfa Bulunamadı – Start Akademie", "Aradığınız sayfa bulunamadı. Start Akademie ana sayfasına dönün.", "") + """
    <section style="min-height: 80vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 80px 20px;">
        <div>
            <div style="font-family: var(--font-serif); font-size: clamp(6rem, 20vw, 12rem); color: var(--gold); line-height: 1; margin-bottom: 24px; opacity: 0.4;">404</div>
            <h1 style="font-family: var(--font-serif); font-size: clamp(1.5rem, 4vw, 2.5rem); margin-bottom: 16px;">Sayfa Bulunamadı</h1>
            <p style="color: var(--text-muted); font-size: 1rem; max-width: 480px; margin: 0 auto 40px; line-height: 1.8;">Aradığınız sayfa kaldırılmış, adı değiştirilmiş veya geçici olarak kullanılamıyor olabilir.</p>
            <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                <a href="index.html" class="btn btn-primary" style="padding: 14px 32px; font-size: 1rem;">Ana Sayfaya Dön →</a>
                <a href="iletisim.html" class="btn" style="padding: 14px 32px; font-size: 1rem; border: 1px solid var(--glass-border); background: var(--glass-bg); color: var(--text);">İletişime Geç</a>
            </div>
        </div>
    </section>
""" + FOOTER


# ─────────────────────────────────────────────────────────────────────────────
# WRITE ALL PAGES
# ─────────────────────────────────────────────────────────────────────────────
PAGES = {
    "uni.html":          page_uni(),
    "dil.html":          page_dil(),
    "ausbildung.html":   page_ausbildung(),
    "denklik.html":      page_denklik(),
    "degisim.html":      page_degisim(),
    "konaklama.html":    page_konaklama(),
    "hakkimizda.html":   page_hakkimizda(),
    "iletisim.html":     page_iletisim(),
    "impressum.html":    page_impressum(),
    "datenschutz.html":  page_datenschutz(),
    "404.html":          page_404(),
}

for filename, content in PAGES.items():
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅  {filename}  ({len(content):,} bytes)")

print("\n🎉  All subpages generated successfully!")

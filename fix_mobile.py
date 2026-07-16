import codecs

mobile_css = """

/* --- COMPREHENSIVE MOBILE FIXES --- */
@media (max-width: 768px) {
    /* Typography Scaling */
    .gate-initial-hero h1, .hero-content h1 { font-size: 2.8rem !important; line-height: 1.1 !important; }
    .gate-initial-hero h1 em, .hero-content h1 em { font-size: 2.8rem !important; }
    .gate-initial-hero p, .hero-content p { font-size: 1.1rem !important; padding: 0 10px; }
    .section-title h2 { font-size: 2.2rem !important; }
    .section-title p { font-size: 1rem !important; }
    
    /* Layout & Spacing */
    section { padding: 60px 0 !important; }
    .container { padding: 0 20px !important; }
    
    /* Portal Slides (Cinematic Gate) */
    .portal-slide { width: 95% !important; max-width: 100% !important; }
    .portal-slide .glass-panel { padding: 24px 16px !important; }
    
    /* StartBot Chat Window */
    .startbot-window { 
        width: 100% !important; 
        right: 0 !important; 
        bottom: 0 !important; 
        height: 85vh !important; 
        border-radius: 24px 24px 0 0 !important; 
    }
    
    /* Pricing & University Cards */
    .pkg-card { padding: 24px !important; }
    .pkg-header h3 { font-size: 1.5rem !important; }
    
    /* Calculator Modal */
    .calculator-layout { gap: 20px !important; }
    
    /* Forms & Inputs */
    input, textarea, select { font-size: 16px !important; /* Prevents iOS Zoom */ }
    
    /* Modals */
    .univ-modal-content {
        width: 95% !important;
        max-height: 95vh !important;
    }
    .univ-grid {
        grid-template-columns: 1fr !important;
    }
}
"""

with codecs.open('assets/style.css', 'a', 'utf-8') as f:
    f.write(mobile_css)

print("Mobile CSS appended successfully.")

# -*- coding: utf-8 -*-

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* --- CHIP BUTTONS (Path Selector & Timeline) --- */
.chip-btn {
    display: inline-block;
    padding: 10px 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 30px;
    color: var(--text-color);
    font-size: 0.95rem;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}

.chip-btn:hover {
    background: rgba(212, 175, 100, 0.15);
    border-color: var(--gold);
    color: var(--gold);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(212, 175, 100, 0.1);
}

:root[data-theme="light"] .chip-btn {
    background: rgba(0, 0, 0, 0.04);
    border-color: rgba(0, 0, 0, 0.08);
    color: var(--text-color);
}

:root[data-theme="light"] .chip-btn:hover {
    background: rgba(212, 175, 100, 0.1);
    border-color: var(--gold);
}

.step-chip {
    display: inline-block;
    padding: 4px 12px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    font-size: 0.8rem;
    color: var(--text-muted);
}

:root[data-theme="light"] .step-chip {
    background: rgba(0, 0, 0, 0.06);
}

.service-icon {
    width: 56px;
    height: 56px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}

.service-icon i {
    width: 28px;
    height: 28px;
}
'''

if '.chip-btn' not in css:
    with open('assets/style.css', 'a', encoding='utf-8') as f:
        f.write(new_css)

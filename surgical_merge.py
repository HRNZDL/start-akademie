from bs4 import BeautifulSoup
import re

# SOURCE: index-test.html - kullanicinin ozgun metinleri
with open('index-test.html', 'r', encoding='utf-8') as f:
    src = BeautifulSoup(f, 'html.parser')

# TARGET: index.backup.html - dogru ID sistemi ve JS'e uygun yapı
with open('index.backup.html', 'r', encoding='utf-8') as f:
    tgt = BeautifulSoup(f, 'html.parser')

def get_text_clean(el):
    return el.get_text(separator=' ', strip=True)

# --- NAVBAR metinlerini aktar ---
src_nav = src.find(id='main-header')
tgt_nav = tgt.find(id='navbar')
if src_nav and tgt_nav:
    src_links = src_nav.find_all('a')
    tgt_links = tgt_nav.find_all('a')
    for i, tl in enumerate(tgt_links):
        if i < len(src_links) and src_links[i].string:
            tl.string = src_links[i].get_text(strip=True)
    print("Navbar aktarildi")

# --- HERO section: slide-1 (slide-welcome -> portal-slide 1) ---
src_slide1 = src.find(id='slide-welcome')
tgt_slide1 = tgt.find('div', class_='portal-slide')  # ilk portal-slide
if src_slide1 and tgt_slide1:
    # Baslik
    src_h1 = src_slide1.find(['h1','h2'])
    tgt_h1 = tgt_slide1.find(['h1','h2'])
    if src_h1 and tgt_h1:
        tgt_h1.clear()
        for child in src_h1.children:
            tgt_h1.append(child.__copy__() if hasattr(child, '__copy__') else type(child)(child))
    # Paragraf
    src_p = src_slide1.find('p')
    tgt_p = tgt_slide1.find('p')
    if src_p and tgt_p:
        tgt_p.string = src_p.get_text(strip=True)
    print("Hero Slide 1 aktarildi")

# --- PILLARS (3 kanat) ---
src_pillars = src.find(id='pillars')
tgt_pillars = tgt.find(id='pillars')
if src_pillars and tgt_pillars:
    # Baslik
    src_h2 = src_pillars.find('h2')
    tgt_h2 = tgt_pillars.find('h2')
    if src_h2 and tgt_h2:
        tgt_h2.string = src_h2.get_text(strip=True)
    
    # Alt baslik paragraf
    src_intro_p = src_pillars.find('p')
    tgt_intro_p = tgt_pillars.find('p')
    if src_intro_p and tgt_intro_p:
        tgt_intro_p.string = src_intro_p.get_text(strip=True)
    print("Pillars aktarildi")

# --- UNIVERSITIES ---
src_unis = src.find(id='universities')
tgt_unis = tgt.find(id='universities')
if src_unis and tgt_unis:
    src_h2 = src_unis.find('h2')
    tgt_h2 = tgt_unis.find('h2')
    if src_h2 and tgt_h2:
        tgt_h2.string = src_h2.get_text(strip=True)
    src_p = src_unis.find('p')
    tgt_p = tgt_unis.find('p')
    if src_p and tgt_p:
        tgt_p.string = src_p.get_text(strip=True)
    print("Universities aktarildi")

# --- PRICING ---
src_pricing = src.find(id='pricing')
tgt_pricing = tgt.find(id='pricing')
if src_pricing and tgt_pricing:
    src_h2 = src_pricing.find('h2')
    tgt_h2 = tgt_pricing.find('h2')
    if src_h2 and tgt_h2:
        tgt_h2.string = src_h2.get_text(strip=True)
    print("Pricing aktarildi")

# --- CONTACT ---
src_contact = src.find(id='contact')
tgt_contact = tgt.find(id='contact')
if src_contact and tgt_contact:
    src_h2 = src_contact.find('h2')
    tgt_h2 = tgt_contact.find('h2')
    if src_h2 and tgt_h2:
        tgt_h2.string = src_h2.get_text(strip=True)
    src_p = src_contact.find('p')
    tgt_p = tgt_contact.find('p')
    if src_p and tgt_p:
        tgt_p.string = src_p.get_text(strip=True)
    print("Contact aktarildi")

# --- WIZARD ---
src_wizard = src.find(id='wizard')
tgt_wizard = tgt.find(id='wizard')
if src_wizard and tgt_wizard:
    src_h2 = src_wizard.find('h2')
    tgt_h2 = tgt_wizard.find('h2')
    if src_h2 and tgt_h2:
        tgt_h2.string = src_h2.get_text(strip=True)
    print("Wizard aktarildi")

# --- CAMP ---
src_camp = src.find(id='camp')
tgt_camp = tgt.find('section', id=lambda x: x and 'camp' in x.lower()) if tgt else None
if not tgt_camp:
    # Try to find by class
    tgt_camp = tgt.find(lambda tag: tag.name == 'section' and tag.get_text(strip=True) and 'Yaz' in tag.get_text())
if src_camp and tgt_camp:
    src_h2 = src_camp.find('h2')
    tgt_h2 = tgt_camp.find('h2')
    if src_h2 and tgt_h2:
        tgt_h2.string = src_h2.get_text(strip=True)
    print("Camp aktarildi (eger bulunduysa)")

# Sonucu kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(tgt))

print("\nTAMAM! index.html guncellendi.")
print("Boyut:", len(str(tgt)), "byte")

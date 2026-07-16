import json

with open('assets/lang.js', 'r', encoding='utf-8') as f:
    text = f.read()

# TR Updates
text = text.replace(
    '"hero.main_title": "Almanya\'daki Eğitim <br><em>Yolculuğunuz</em>",',
    '"hero.main_title": "Almanya\'da ve Almanya\'ya Giden <br><em>Eğitim Yolunuz</em>",'
)
text = text.replace(
    '"hero.title": "Almanya’da Eğitim ve Kariyer Yolculuğunuz <em>Burada Başlıyor</em>",',
    '"hero.title": "Almanya\'da ve Almanya\'ya Giden <br><em>Eğitim Yolunuz</em>",'
)
text = text.replace(
    '"hero.subtitle": "Start Akademie, Almanya\'daki üniversite, dil kursu ve kariyer hedeflerinize ulaşmanız için yanınızda. Başvurudan konaklamaya kadar tüm süreçlerinizi uzman ekibimizle güvenle yönetiyoruz.",',
    '"hero.subtitle": "Start Akademie, Frankfurt yakınlarında yerleşik bir eğitim kurumudur. Almanya\'daki öğrencileri nitelikli ders desteği (Nachhilfe) ile destekliyor ve Türkiye\'den Almanya\'ya eğitim yolculuğuna çıkan adaylara rehberlik ediyoruz. Ek olarak, Almanca ve İngilizce için çevrimiçi dil kursları sunuyoruz.",'
)

# EN Updates
text = text.replace(
    '"hero.main_title": "Your Education Path <br><em>in Germany</em>",',
    '"hero.main_title": "Your Education Path <br><em>In and To Germany</em>",'
)
text = text.replace(
    '"hero.title": "Your Education Journey <br><em>Starts Here</em>",',
    '"hero.title": "Your Education Path <br><em>In and To Germany</em>",'
)
text = text.replace(
    '"hero.subtitle": "Start Akademie, with its center near Frankfurt, increases the school success (Nachhilfe) of students in Germany and provides university admission support to prospective students coming to Germany from Turkey.",',
    '"hero.subtitle": "Start Akademie is an educational institution located near Frankfurt. We support students in Germany with qualified tutoring (Nachhilfe) and guide applicants from Turkey on their educational journey to Germany. Additionally, we offer online language courses for German and English.",'
)

# DE Updates
text = text.replace(
    '"hero.main_title": "Ihr Bildungsweg <br><em>in Deutschland</em>",',
    '"hero.main_title": "Ihr Bildungsweg <br><em>in und nach Deutschland</em>",'
)
text = text.replace(
    '"hero.title": "Ihr Bildungsweg <br><em>Beginnt Hier</em>",',
    '"hero.title": "Ihr Bildungsweg <br><em>in und nach Deutschland</em>",'
)
text = text.replace(
    '"hero.subtitle": "Die Start Akademie mit Zentrum in der Nähe von Frankfurt steigert den schulischen Erfolg (Nachhilfe) von Schülern in Deutschland und bietet Studienbewerbern aus der Türkei Unterstützung bei der Hochschulzulassung.",',
    '"hero.subtitle": "Start Akademie ist eine in der Nähe von Frankfurt ansässige Bildungseinrichtung. Wir unterstützen Schülerinnen und Schüler in Deutschland mit qualifizierter Nachhilfe und begleiten Bewerberinnen und Bewerber aus der Türkei auf ihrem Bildungsweg nach Deutschland. Ergänzend bieten wir Online-Sprachkurse für Deutsch und Englisch an.",'
)

with open('assets/lang.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Hero text updated.")

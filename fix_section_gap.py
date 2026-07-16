import re

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Reduce desktop padding from 140px to 100px
old_desktop = '''        .section-padding {
            padding: 140px 0;'''
new_desktop = '''        .section-padding {
            padding: 90px 0; /* Reduced from 140px to close the huge gaps */'''
css = css.replace(old_desktop, new_desktop)

# Add mobile override at the end of the file
mobile_override = '''
    /* Tighter section gaps on mobile */
    .section-padding { padding: 60px 0 !important; }
'''

# Find the end of the mobile media query
# We know the last few lines of style.css:
#    .univ-grid {
#        grid-template-columns: 1fr !important;
#    }
#}

end_of_media_query = '''    .univ-grid {
        grid-template-columns: 1fr !important;
    }
}'''

new_end_of_media_query = '''    .univ-grid {
        grid-template-columns: 1fr !important;
    }
    .section-padding { padding: 50px 0 !important; }
}'''

css = css.replace(end_of_media_query, new_end_of_media_query)

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'assets/style\.css\?v=\d+', 'assets/style.css?v=29', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import sys

def remove_camp_section(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_str = 'id="camp"'
    start_idx = content.find(start_str)
    
    if start_idx == -1:
        print("Could not find id='camp' in HTML")
        return

    # Find the beginning of the <section tag
    tag_start = content.rfind('<section', 0, start_idx)
    
    # Find the closing </section> tag that corresponds to it
    # We must be careful if there are nested <section> tags, but usually there aren't in these landing pages inside the main section.
    # To be safe, we track depth.
    depth = 0
    i = tag_start
    tag_end = -1
    
    while i < len(content):
        if content[i:i+8] == '<section':
            depth += 1
            i += 8
        elif content[i:i+10] == '</section>':
            depth -= 1
            if depth == 0:
                tag_end = i + 10
                break
            i += 10
        else:
            i += 1

    if tag_end != -1:
        # Also remove the preceding comment block if it exists
        comment_start = content.rfind('<!--', max(0, tag_start - 200), tag_start)
        if comment_start != -1 and 'YAZ KAMPLARI' in content[comment_start:tag_start].upper():
            tag_start = comment_start
        
        # Remove it
        new_content = content[:tag_start] + content[tag_end:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully removed the camp section.")
    else:
        print("Could not find matching </section> tag.")

remove_camp_section('index.html')

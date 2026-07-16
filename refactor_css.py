import io

index_path = 'index.html'
style_path = 'assets/style.css'

with io.open(index_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<style>' in line and start_idx == -1:
        start_idx = i
    if '</style>' in line and end_idx == -1:
        end_idx = i

if start_idx != -1 and end_idx != -1:
    css_content = ''.join(lines[start_idx+1:end_idx])
    with io.open(style_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    new_lines = lines[:start_idx] + ['    <link rel="stylesheet" href="assets/style.css">\n'] + lines[end_idx+1:]
    with io.open(index_path, 'w', encoding='utf-8') as f:
        f.write(''.join(new_lines))
    print('CSS extracted successfully.')
else:
    print('Could not find tags.')

s = 'ðŸ”¶'
try:
    fixed = s.encode('cp1252').decode('utf-8')
    with open('out.txt', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print("Success")
except Exception as e:
    print('FAILED:', e)

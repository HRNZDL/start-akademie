import json

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        if 'Sağladığınız tam onay ve güven için teşekkür ederim' in line:
            data = json.loads(line)
            print(f"Found at step: {data.get('step_index')}")
            print(f"Type: {data.get('type')}")
            content = data.get('content', '')
            if content:
                print(f"Content: {content[:200]}")
            else:
                print("No content")

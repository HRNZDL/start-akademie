import json
log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        if step in [3011, 3014, 3040, 3077, 3087, 3090]:
            tc = data.get('tool_calls', [])
            for call in tc:
                args = call.get('args', {})
                print(f"Step {step} - view_file: {args}")

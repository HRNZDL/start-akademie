import json

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        tc = data.get('tool_calls', [])
        if tc:
            for call in tc:
                args = call.get('args', {})
                if 'CommandLine' in args and 'index.backup.html' in args['CommandLine']:
                    print(f"Step {data.get('step_index')} CMD: {args['CommandLine']}")

import json

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'
with open('all_backup_commands.txt', 'w', encoding='utf-8') as out:
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            step = data.get('step_index')
            tc = data.get('tool_calls', [])
            for call in tc:
                args = call.get('args', {})
                for k, v in args.items():
                    val = str(v).lower()
                    if ('copy' in val or 'cp ' in val or 'backup' in val) and ('index' in val and '.html' in val):
                        out.write(f"Step {step} - {call.get('name')}: {val[:300]}\n")

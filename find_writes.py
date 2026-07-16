import json

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'
with open('index_writes.txt', 'w', encoding='utf-8') as out:
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            step = data.get('step_index')
            if step and step > 1000:
                tc = data.get('tool_calls', [])
                for call in tc:
                    name = call.get('name', '')
                    args = call.get('args', {})
                    if name in ['write_to_file', 'replace_file_content', 'multi_replace_file_content']:
                        if 'TargetFile' in args and 'index.html' in args['TargetFile']:
                            out.write(f"Step {step} - {name}\n")

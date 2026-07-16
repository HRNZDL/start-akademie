import json

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        step = data.get('step_index')
        if step and 3200 <= step <= 3300:
            tc = data.get('tool_calls', [])
            if tc:
                for call in tc:
                    name = call.get('name', '')
                    args = call.get('args', {})
                    if name == 'run_command':
                        cmd = args.get('CommandLine', '')
                        if 'js' in cmd or 'assets' in cmd or 'Get-Content' in cmd:
                            print(f"Step {step} CMD: {cmd[:200]}")

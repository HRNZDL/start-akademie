import json

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        step = data.get('step_index')
        if step and 3190 <= step <= 3215:
            tc = data.get('tool_calls', [])
            if tc:
                for call in tc:
                    name = call.get('name', '')
                    args = call.get('args', {})
                    if name == 'write_to_file' or name == 'replace_file_content':
                        tf = args.get('TargetFile', '')
                        print(f"Step {step} - {name} on {tf}")
                    elif name == 'run_command':
                        print(f"Step {step} - {name}: {args.get('CommandLine')}")

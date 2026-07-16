import json

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        step = data.get('step_index')
        if step and 3170 <= step <= 3195:
            tc = data.get('tool_calls', [])
            if tc:
                for call in tc:
                    name = call.get('function', {}).get('name', '')
                    if not name: name = call.get('name', '')
                    args = call.get('function', {}).get('arguments', '')
                    if not args: args = call.get('arguments', '')
                    if type(args) == str:
                        try: args = json.loads(args)
                        except: pass
                    if isinstance(args, dict):
                        if 'TargetFile' in args or 'AbsolutePath' in args:
                            val = args.get('TargetFile') or args.get('AbsolutePath')
                            print(f'Step {step} - Tool: {name} File: {val}')

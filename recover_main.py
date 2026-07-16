import json
import os
import glob

log_dir = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs'
log_file = os.path.join(log_dir, 'transcript.jsonl')

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        if 'assets/js/main.js' in line:
            try:
                data = json.loads(line)
            except Exception:
                continue
            if data.get('type') == 'PLANNER_RESPONSE':
                if 'tool_calls' in data:
                    for tc in data['tool_calls']:
                        args = tc.get('args', {})
                        if tc['name'] == 'write_to_file' and 'main.js' in args.get('TargetFile', ''):
                            print(f"Found write_to_file at step {data.get('step_index')}")
                            with open('recovered_main_write.js', 'w', encoding='utf-8') as out:
                                out.write(args.get('CodeContent', ''))
                        if tc['name'] == 'replace_file_content' and 'main.js' in args.get('TargetFile', ''):
                            print(f"Found replace_file_content at step {data.get('step_index')}")
                            
            elif data.get('type') == 'TOOL_RESPONSE':
                # Check for run_command output that might contain the file contents
                if 'output' in data.get('content', '') and 'TOTAL_FRAMES' in data.get('content', ''):
                    print(f"Found TOTAL_FRAMES in tool response at step {data.get('step_index')}")

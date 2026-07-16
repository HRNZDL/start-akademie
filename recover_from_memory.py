import json
import re

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'

with open('index-test.html', 'r', encoding='utf-8') as f:
    text = f.read().replace('\r\n', '\n')

def apply_replacement(current_text, target, replacement, step):
    target_norm = target.replace('\r\n', '\n')
    repl_norm = replacement.replace('\r\n', '\n')
    
    if target_norm in current_text:
        return current_text.replace(target_norm, repl_norm, 1), True
    else:
        # Try to find by ignoring leading/trailing whitespace of the target
        # Sometimes there are minor differences.
        # This is riskier but if exact match fails, it's better than nothing.
        import fnmatch
        return current_text, False

applied_count = 0
failed_count = 0
failed_steps = []

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        
        # 1594 is when index-test.html was copied.
        # We want to go up to step 3129 (last edit before the modularization on June 3)
        if step and 1595 <= step <= 3150:
            tc = data.get('tool_calls', [])
            for call in tc:
                name = call.get('name', '')
                args = call.get('args', {})
                if name in ['replace_file_content', 'multi_replace_file_content']:
                    tf = args.get('TargetFile', '')
                    if 'index.html' in tf:
                        if name == 'replace_file_content':
                            tc_text = args.get('TargetContent', '')
                            rc_text = args.get('ReplacementContent', '')
                            new_text, success = apply_replacement(text, tc_text, rc_text, step)
                            if success: 
                                text = new_text
                                applied_count += 1
                            else: 
                                failed_count += 1
                                failed_steps.append(step)
                                
                        elif name == 'multi_replace_file_content':
                            chunks = args.get('ReplacementChunks', [])
                            if type(chunks) == str:
                                try: chunks = json.loads(chunks)
                                except: chunks = []
                            for chunk in chunks:
                                tc_text = chunk.get('TargetContent', '')
                                rc_text = chunk.get('ReplacementContent', '')
                                new_text, success = apply_replacement(text, tc_text, rc_text, step)
                                if success:
                                    text = new_text
                                    applied_count += 1
                                else:
                                    failed_count += 1
                                    failed_steps.append(step)

print(f"Applied: {applied_count}, Failed: {failed_count}")
if failed_steps:
    print(f"Failed steps: {failed_steps[:10]}...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Recovered index.html saved.")

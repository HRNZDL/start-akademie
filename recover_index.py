import json
import re

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'
with open('index-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def apply_replacement(lines, target_content, replacement_content):
    text = "".join(lines)
    # The agent might use slight variations in whitespace or line endings, so direct replacement is best if exact,
    # otherwise we might fail. Let's try direct string replace first.
    if target_content in text:
        text = text.replace(target_content, replacement_content, 1)
        return [l + '\n' for l in text.split('\n')]
    else:
        # Normalize line endings
        norm_text = text.replace('\r\n', '\n')
        norm_target = target_content.replace('\r\n', '\n')
        if norm_target in norm_text:
            norm_text = norm_text.replace(norm_target, replacement_content.replace('\r\n', '\n'), 1)
            return [l + '\n' for l in norm_text.split('\n')]
    print("WARNING: Could not apply a patch!")
    return lines

patch_count = 0
failed_count = 0

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        if step and 1594 <= step <= 3200:
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
                            old_len = len("".join(lines))
                            lines = apply_replacement(lines, tc_text, rc_text)
                            if len("".join(lines)) == old_len: failed_count += 1
                            patch_count += 1
                        elif name == 'multi_replace_file_content':
                            chunks = args.get('ReplacementChunks', [])
                            if type(chunks) == str:
                                try: chunks = json.loads(chunks)
                                except: chunks = []
                            for chunk in chunks:
                                tc_text = chunk.get('TargetContent', '')
                                rc_text = chunk.get('ReplacementContent', '')
                                old_len = len("".join(lines))
                                lines = apply_replacement(lines, tc_text, rc_text)
                                if len("".join(lines)) == old_len: failed_count += 1
                                patch_count += 1

print(f"Applied {patch_count} patches. Failed: {failed_count}")
with open('index_recovered.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

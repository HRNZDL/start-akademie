import json
import re

log_path = r'C:\Users\Harun\.gemini\antigravity\brain\1ab7292d-dfa0-40d4-8d0f-e7bddbfc9bf6\.system_generated\logs\transcript.jsonl'

# We start from the original monolithic file
with open('index.backup.html', 'r', encoding='utf-8') as f:
    text = f.read()

def apply_replacement(text, target_content, replacement_content):
    if target_content in text:
        return text.replace(target_content, replacement_content, 1)
    else:
        # Normalize line endings
        norm_text = text.replace('\r\n', '\n')
        norm_target = target_content.replace('\r\n', '\n')
        if norm_target in norm_text:
            return norm_text.replace(norm_target, replacement_content.replace('\r\n', '\n'), 1)
    return text

patch_count = 0
failed_count = 0

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        # All steps from 1000 up to the split at 3200
        if step and 1000 <= step <= 3200:
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
                            new_text = apply_replacement(text, tc_text, rc_text)
                            if new_text == text: failed_count += 1
                            else: patch_count += 1
                            text = new_text
                        elif name == 'multi_replace_file_content':
                            chunks = args.get('ReplacementChunks', [])
                            if type(chunks) == str:
                                try: chunks = json.loads(chunks)
                                except: chunks = []
                            for chunk in chunks:
                                tc_text = chunk.get('TargetContent', '')
                                rc_text = chunk.get('ReplacementContent', '')
                                new_text = apply_replacement(text, tc_text, rc_text)
                                if new_text == text: failed_count += 1
                                else: patch_count += 1
                                text = new_text

print(f"Applied {patch_count} patches to index.backup.html. Failed: {failed_count}")
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

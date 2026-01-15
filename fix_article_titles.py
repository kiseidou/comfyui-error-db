import os
import re

CONTENT_DIR = r"d:\ANTIGRAVITY\comfyui-error-db\src\content\blog"

# Map filename tokens to Title Prefixes
PREFIX_MAP = {
    "UnityML": "UnityML",
    "Python": "Python",
    "CivitAI": "CivitAI",
    "HuggingFace": "HuggingFace",
    "ReactNative": "ReactNative",
    # ComfyUI is default, but if we see explicit ComfyUI in filename, we keep it.
    "ComfyUI": "ComfyUI" 
}

def fix_titles():
    print("🔧 Starting Title Prefix Fixer...")
    count = 0
    
    for root, dirs, files in os.walk(CONTENT_DIR):
        for f in files:
            if f.endswith(".md"):
                # Determine correct category from filename
                # e.g. issue-UnityML-123.md -> UnityML
                correct_cat = None
                for key in PREFIX_MAP:
                    if f"issue-{key}-" in f:
                        correct_cat = PREFIX_MAP[key]
                        break
                
                # If filename doesn't have a known prefix, it might be legacy ComfyUI or manually named.
                # If legacy (issue-123.md), we assume ComfyUI, but let's check content.
                if not correct_cat:
                    # check if legacy ComfyUI
                    if re.match(r'issue-\d+\.md', f):
                         correct_cat = "ComfyUI"
                    else:
                         continue # Skip unknown patterns
                
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                # Regex to find title line
                # title: "【Prefix】..."
                # We want to replace 【WrongPrefix】 with 【CorrectPrefix】
                
                # Capture the existing prefix inside the brackets
                match = re.search(r'title:\s*["\']【(.*?)】', content)
                if match:
                    current_prefix = match.group(1)
                    if current_prefix != correct_cat:
                        print(f"  Fixing {f}: 【{current_prefix}】 -> 【{correct_cat}】")
                        new_content = content.replace(f"【{current_prefix}】", f"【{correct_cat}】")
                        with open(path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        count += 1
                else:
                    # No brackets? Try to insert them?
                    # For now, only fix mismatched brackets to be safe.
                    pass
                    
    print(f"✅ Fixed {count} files.")

if __name__ == "__main__":
    fix_titles()

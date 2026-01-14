import os
import re
import yaml

TARGET_DIR = r"d:\ANTIGRAVITY\comfyui-error-db\src\content\blog"

def validate_and_nuke():
    print(f"☢️  Scanning {TARGET_DIR} for corrupt content...")
    deleted_count = 0
    
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue
                
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check 1: Frontmatter Fences
                match = re.search(r'^---\s*\n(.*?)\n---\s*', content, re.DOTALL | re.MULTILINE)
                valid = False
                reason = "Unknown"
                
                if match:
                    yaml_text = match.group(1).strip()
                    if yaml_text:
                        try:
                            # Check 2: Valid YAML
                            data = yaml.safe_load(yaml_text)
                            if isinstance(data, dict):
                                # Check 3: Required Keys
                                if "title" in data and "pubDate" in data:
                                    valid = True
                                else:
                                    reason = "Missing title or pubDate"
                            else:
                                reason = "YAML is not a dict"
                        except Exception as e:
                            reason = f"YAML Parse Error: {e}"
                    else:
                        reason = "Empty Frontmatter"
                else:
                    reason = "No Frontmatter Fences"
                
                if not valid:
                    print(f"❌ Deleting {file} ({reason})")
                    os.remove(path)
                    deleted_count += 1
                    
            except Exception as e:
                print(f"⚠️ Error reading {file}: {e}")

    print(f"✅ Sweep Complete. Deleted {deleted_count} corrupt files.")

if __name__ == "__main__":
    validate_and_nuke()

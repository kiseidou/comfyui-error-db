
import os
import re
import yaml

content_dir = r"d:\ANTIGRAVITY\comfyui-error-db\src\content\blog"

print(f"Checking markdown files in {content_dir}...")

for filename in os.listdir(content_dir):
    if not filename.endswith(".md"):
        continue
        
    filepath = os.path.join(content_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract frontmatter between first two ---
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        print(f"[WARN] No frontmatter found: {filename}")
        continue
        
    frontmatter_raw = match.group(1)
    
    try:
        data = yaml.safe_load(frontmatter_raw)
        # Check required keys
        if not data.get('title'):
             print(f"[ERR] Missing title: {filename}")
        if not data.get('description'):
             print(f"[ERR] Missing description: {filename}")
        if not data.get('pubDate'):
             print(f"[ERR] Missing pubDate: {filename}")
             
    except yaml.YAMLError as exc:
        print(f"[FAIL] Invalid YAML in {filename}: {exc}")
    except Exception as e:
        print(f"[FAIL] Error parsing {filename}: {e}")

print("Validation complete.")

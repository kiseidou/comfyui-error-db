import os
import glob
import yaml

content_dir = r"d:\ANTIGRAVITY\comfyui-error-db\src\content\blog"
files = glob.glob(os.path.join(content_dir, "*.md"))

print(f"Checking {len(files)} files...")

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    if not content.startswith('---\n'):
        print(f"[ERROR] {os.path.basename(file_path)}: No frontmatter start")
        continue
        
    try:
        parts = content.split('---', 2)
        if len(parts) < 3:
             print(f"[ERROR] {os.path.basename(file_path)}: Malformed frontmatter")
             continue
        
        frontmatter = parts[1]
        yaml.safe_load(frontmatter)
        # print(f"[OK] {os.path.basename(file_path)}")
        
    except yaml.YAMLError as e:
        print(f"[FAIL] {os.path.basename(file_path)}: YAML Error: {e}")
    except Exception as e:
        print(f"[FAIL] {os.path.basename(file_path)}: Error: {e}")

print("Validation complete.")

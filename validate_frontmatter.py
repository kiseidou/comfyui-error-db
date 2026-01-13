import os
import glob
import yaml
import sys

# Ensure PyYAML is available
try:
    import yaml
except ImportError:
    print("PyYAML not found. Please install it using 'pip install pyyaml'")
    sys.exit(1)

content_dir = r"d:\ANTIGRAVITY\comfyui-error-db\src\content\blog"
files = glob.glob(os.path.join(content_dir, "*.md"))

print(f"Checking {len(files)} files in {content_dir}...")

error_count = 0

for file_path in files:
    filename = os.path.basename(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Check for BOM or weird whitespace at start
        if not content.startswith('---'):
            # Check if it has BOM
            if content.startswith('\ufeff---'):
                 print(f"[WARN] {filename}: Has BOM. Fixing...")
                 # Fix: write back without BOM
                 with open(file_path, 'w', encoding='utf-8') as f:
                     f.write(content.lstrip('\ufeff'))
                 continue
            else:
                print(f"[ERROR] {filename}: Does not start with '---'")
                print(f"       First 20 chars: {repr(content[:20])}")
                error_count += 1
                continue

        # 2. Extract and Validate YAML
        try:
            _, frontmatter, body = content.split('---', 2)
        except ValueError:
            print(f"[ERROR] {filename}: Cannot split frontmatter (missing closing '---'?)")
            error_count += 1
            continue

        # Check for tabs in frontmatter
        if '\t' in frontmatter:
             print(f"[ERROR] {filename}: Contains TABS in frontmatter (YAML forbids tabs)")
             error_count += 1
             continue

        # Parse YAML
        data = yaml.safe_load(frontmatter)
        
        # 3. specific field checks (Astro requires these)
        if 'title' not in data:
            print(f"[ERROR] {filename}: Missing 'title'")
            error_count += 1
        if 'pubDate' not in data:
             print(f"[ERROR] {filename}: Missing 'pubDate'")
             error_count += 1

        # print(f"[OK] {filename}")

    except yaml.YAMLError as e:
        print(f"[FAIL] {filename}: YAML Error: {e}")
        error_count += 1
    except Exception as e:
        print(f"[FAIL] {filename}: General Error: {e}")
        error_count += 1

print(f"\nValidation complete. Found {error_count} errors.")
if error_count > 0:
    sys.exit(1)


import os
import yaml
import re

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "src", "content", "blog")

def validate_frontmatter(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return f"❌ Read Error: {e}"

    # 1. Check for basic delimiters count
    # Note: Regex is better but let's be simple first
    if content.count('---') < 2:
        return "❌ Missing Frontmatter Fences (---)"

    # 2. Extract YAML block using robust regex
    match = re.search(r'^---\s*\n(.*?)\n---\s*', content, re.DOTALL | re.MULTILINE)
    if not match:
        return "❌ Could not parse Frontmatter block"
    
    yaml_text = match.group(1).strip()
    if not yaml_text:
        return "❌ Empty Frontmatter Body"

    try:
        data = yaml.safe_load(yaml_text)
    except yaml.YAMLError as e:
        return f"❌ Invalid YAML Syntax: {e}"
    
    if not isinstance(data, dict):
        return "❌ Frontmatter is not a dictionary"

    # 3. Check Required Keys
    required = ["title", "description", "pubDate"]
    missing = [k for k in required if k not in data]
    if missing:
        return f"❌ Missing keys: {missing}"

    # 4. Check Empty Values
    if not data.get('title'): return "❌ Empty title"
    if not data.get('pubDate'): return "❌ Empty pubDate"

    # 5. Check Date Format Strict
    pdate = str(data.get("pubDate", "")).strip()
    import datetime
    
    # Common formats
    formats = ['%Y-%m-%d', '%Y-%m-%d %H:%M:%S', '%Y/%m/%d', '%Y-%m-%dT%H:%M:%S.%fZ']
    valid_date = False
    for fmt in formats:
        try:
            datetime.datetime.strptime(pdate, fmt)
            valid_date = True
            break
        except ValueError:
            continue
    
    if not valid_date:
        # Check simple regex for YYYY-MM-DD
        if not re.match(r'^\d{4}-\d{2}-\d{2}', pdate):
            return f"❌ Invalid Date Format: '{pdate}'"

    return None

def main():
    print(f"🔍 Scanning {CONTENT_DIR}...")
    error_count = 0
    
    for root, dirs, files in os.walk(CONTENT_DIR):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                error = validate_frontmatter(filepath)
                if error:
                    print(f"📄 {filename} ({os.path.basename(root)})")
                    print(f"   {error}")
                    error_count += 1
                    
                    # AUTO-DELETE FOR USER REQUEST "全部の検品"
                    try:
                        os.remove(filepath)
                        print(f"   🗑️ DELETED (Bad File)")
                    except Exception as ex:
                        print(f"   ⚠️ Failed to delete: {ex}")

    if error_count == 0:
        print("\n✅ All files look good!")
    else:
        print(f"\n⚠️ Found {error_count} invalid files.")

if __name__ == "__main__":
    main()

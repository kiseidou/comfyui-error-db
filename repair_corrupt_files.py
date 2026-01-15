
import os
import re
import yaml
from datetime import datetime

def repair_file(path):
    """
    Attempts to repair a markdown file with corrupt or missing frontmatter.
    Returns:
        True if the file is valid or successfully repaired.
        False if the file is unrecoverable (should be deleted).
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # check for completely empty file
        if not content.strip():
            return False

        # Check existing frontmatter
        # We use a more lenient regex than strict YAML parsers might
        match = re.search(r'^---\s*\n(.*?)\n---\s*', content, re.DOTALL | re.MULTILINE)
        
        has_valid_frontmatter = False
        existing_yaml = {}
        
        if match:
            yaml_text = match.group(1).strip()
            # Basic cleanup of common YAML errors we've seen
            # e.g. **title:** instead of title:
            # Also handle *title*: and title**:
            # Regex Explanation:
            # ^\s*       : Start of line, optional whitespace
            # [*]*       : Optional leading asterisks
            # ([a-zA-Z0-9_]+) : The key (alphanumeric+underscore) capture group 1
            # [*]*       : Optional trailing asterisks BEFORE matches colon
            # \s*        : Optional whitespace
            # :          : Colon
            yaml_text_clean = re.sub(r'^\s*[*]*([a-zA-Z0-9_]+)[*]*\s*:', r'\1:', yaml_text, flags=re.MULTILINE)
            
            # HANDLE ASTERISKS AFTER COLON (e.g. title:** "...")
            yaml_text_clean = re.sub(r':\s*\*\*', ':', yaml_text_clean)
            
            # Also handle cases with missing colon if commonly seen, e.g. title** "Value"
            # But let's stick to standard YAML fix first.
            
            try:
                existing_yaml = yaml.safe_load(yaml_text_clean)
                if isinstance(existing_yaml, dict):
                    # sanitize keys if they still have asterisks (paranoid check)
                    clean_yaml = {}
                    for k, v in existing_yaml.items():
                         clean_key = k.replace('*', '').strip()
                         clean_yaml[clean_key] = v
                    existing_yaml = clean_yaml

                    if "title" in existing_yaml and "pubDate" in existing_yaml:
                        has_valid_frontmatter = True
                        
                        # CRITICAL: Even if valid, we must ensure it is at the very START of the file.
                        if match.start() > 0:
                             print(f"🔧 Trimming leading garbage from {os.path.basename(path)}...")
                             has_valid_frontmatter = False 
                        
                        if yaml_text != yaml_text_clean:
                           # If we just fixed the bold keys, force rewrite
                           has_valid_frontmatter = False 
                           
                        # Additional check: If keys had asterisks that regex didn't catch inside existing_yaml
                        # (e.g. if PyYAML loaded 'title**' as a key)
                        if any('*' in k for k in yaml.safe_load(yaml_text).keys()):
                             has_valid_frontmatter = False

            except Exception:
                pass # Invalid YAML, we will try to repair
        
        if has_valid_frontmatter:
            return True

        # --- REPAIR LOGIC ---
        print(f"🔧 Repairing {os.path.basename(path)}...")
        
        # 1. Extract Body (everything after the first --- ... --- block if it exists)
        body = content
        if match:
             body = content[match.end():].strip()
        else:
             # If no frontmatter, maybe there's a weird unclosed one or just raw markdown?
             # If it starts with --- but fails regex, might be tricky.
             # Let's assume content is everything.
             pass

        # 2. Extract Metadata candidates
        title = existing_yaml.get('title')
        pub_date = existing_yaml.get('pubDate')
        description = existing_yaml.get('description')
        
        # Fallback Title: First H1
        if not title:
            h1_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
            if h1_match:
                title = h1_match.group(1).strip()
        
        # Fallback Title: Filename
        if not title:
            filename = os.path.basename(path)
            name_part = os.path.splitext(filename)[0]
            title = name_part.replace('issue-', 'Issue ').replace('-', ' ')
        
        # Fallback Description
        if not description:
            description = f"Fix guide for {title}"
            
        # Fallback Date
        if not pub_date:
            try:
                # Try to get file creation time or mod time? 
                # Or just use today. Using today is safest for "published now".
                pub_date = datetime.now().strftime('%Y-%m-%d')
            except:
                pub_date = "2024-01-01"

        # Sanitize for YAML (escape quotes)
        def clean_str(s):
            return str(s).replace('"', '\\"')

        new_frontmatter = f"""---
title: "{clean_str(title)}"
description: "{clean_str(description)}"
pubDate: "{pub_date}"
---

"""
        
        new_content = new_frontmatter + body
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"✅ Repaired: {os.path.basename(path)}")
        return True

    except Exception as e:
        print(f"⚠️ Failed to repair {os.path.basename(path)}: {e}")
        return False

if __name__ == "__main__":
    # Test run on current dir if run directly
    pass

import os
import shutil
import time

# Configuration
DEST_BASE = r"d:\ANTIGRAVITY\comfyui-error-db\src\content\blog"

# Source Map: Path -> ShortPrefix
SOURCES = {
    r"d:\ANTIGRAVITY\Empire\unity-error-db\src\content\blog": "UnityML",
    r"d:\ANTIGRAVITY\Empire\python-error-db\src\content\blog": "Python",
    r"d:\ANTIGRAVITY\Empire\civitai-model-db\src\content\blog": "CivitAI",
    r"d:\ANTIGRAVITY\Empire\huggingface-news-db\src\content\blog": "HuggingFace",
    r"d:\ANTIGRAVITY\Empire\mobile-bug-db\src\content\blog": "ReactNative"
}

def migrate():
    print(f"🚀 Starting Empire Content Migration...")
    total_copied = 0
    
    for src_base, prefix in SOURCES.items():
        if not os.path.exists(src_base):
            print(f"⚠️ Source not found: {src_base}")
            continue
            
        print(f"\n📂 Processing {prefix} from {src_base}...")
        
        # 1. Process files in the ROOT of blog folder (Flat structure fallback)
        # 2. Process files in subfolders (ja/en/zh)
        
        all_files = []
        # Walk root files
        for f in os.listdir(src_base):
            if f.endswith(".md"):
                all_files.append((f, None)) # None = detect language
                
        # Walk subfolders
        for lang in ["ja", "en", "zh"]:
            lang_dir = os.path.join(src_base, lang)
            if os.path.exists(lang_dir):
                for f in os.listdir(lang_dir):
                    if f.endswith(".md"):
                         all_files.append((f, lang))

        print(f"   Found {len(all_files)} candidates...")

        for filename, forced_lang in all_files:
            # Resolve Source Path
            if forced_lang:
                src_file = os.path.join(src_base, forced_lang, filename)
            else:
                src_file = os.path.join(src_base, filename)
            
            # Detect Language if needed
            lang = forced_lang
            if not lang:
                try:
                    with open(src_file, 'r', encoding='utf-8') as f:
                        content = f.read(500) # Read header
                        if "title:" in content:
                            title_line = [l for l in content.split('\n') if "title:" in l][0]
                            # Simple heuristic
                            if any("\u3000" <= c <= "\u303f" or "\u3040" <= c <= "\u309f" or "\u30a0" <= c <= "\u30ff" for c in title_line):
                                lang = "ja"
                            elif any("\u4e00" <= c <= "\u9fff" for c in title_line):
                                lang = "zh"
                            else:
                                lang = "en"
                        else:
                            lang = "en" # Fallback
                except:
                    lang = "en"

            dest_lang_dir = os.path.join(DEST_BASE, lang)
            os.makedirs(dest_lang_dir, exist_ok=True)
            
            # Naming Logic
            if f"issue-{prefix}-" in filename:
                new_filename = filename
            else:
                parts = filename.split('-')
                if len(parts) >= 2 and parts[0] == 'issue':
                    rest = "-".join(parts[1:])
                    new_filename = f"issue-{prefix}-{rest}"
                else:
                    new_filename = f"issue-{prefix}-{filename}"
                    
            dest_file = os.path.join(dest_lang_dir, new_filename)
            
            if not os.path.exists(dest_file):
                try:
                    shutil.copy2(src_file, dest_file)
                    total_copied += 1
                except Exception as e:
                    print(f"Failed to copy {filename}: {e}")
                    
            if total_copied > 0 and total_copied % 100 == 0:
                print(f"  ...copied {total_copied} files so far")
                            
    print(f"\n✅ Migration Complete! Total files copied: {total_copied}")

if __name__ == "__main__":
    migrate()

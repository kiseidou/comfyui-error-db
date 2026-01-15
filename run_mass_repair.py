import os
from repair_corrupt_files import repair_file

CONTENT_DIR = r"d:\ANTIGRAVITY\comfyui-error-db\src\content\blog"

def main():
    print("🚀 Starting Mass Repair...")
    count = 0
    repaired = 0
    
    for root, dirs, files in os.walk(CONTENT_DIR):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                # Force check everything
                if repair_file(path):
                    repaired += 1
                count += 1
                if count % 100 == 0:
                    print(f"Checked {count} files...")
                    
    print(f"✅ Finished. Processed: {count}")

if __name__ == "__main__":
    main()

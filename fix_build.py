import subprocess
import os
import re
import sys

def main():
    print("🚀 Starting Hyper-Aggressive Build Fixer...")
    attempts = 0
    max_attempts = 50 # Prevent infinite loops
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\n⚡ Attempt {attempts}: Running Build...")
        
        # Run build and capture ALL output
        process = subprocess.run("npm run build", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='ignore')
        
        output = process.stdout + process.stderr
        
        if process.returncode == 0:
            print("✅ BUILD SUCCESS! The garden is clean.")
            break
            
        print("❌ Build Failed. Analyzing logs...")
        
        # Regex to find the culprit file in Astro error logs
        # Pattern 1: [InvalidContentEntryDataError] blog -> ja/issue-2829
        # Pattern 2: Location: .../src/content/blog/ja/issue-2829.md
        
        match = re.search(r'src[\\/]content[\\/]blog[\\/](.*?)\.md', output)
        if not match:
             # Try simpler pattern
             match = re.search(r'blog -> (.*?)\s', output)
             
        if match:
            rel_path = match.group(1).strip()
            # If pattern 2 matched, it might be 'ja/issue-2829'
            # If pattern 1 matched 'blog -> ', it might match 'ja/issue-2829'
            
            # Normalize path
            if not rel_path.endswith(".md"):
                rel_path += ".md"
                
            full_path = os.path.join(os.getcwd(), "src", "content", "blog", rel_path)
            
            if os.path.exists(full_path):
                print(f"💣 FOUND CULPRIT: {rel_path}")
                try:
                    os.remove(full_path)
                    print("   🗑️ DELETED.")
                except Exception as e:
                    print(f"   ⚠️ Could not delete: {e}")
                    sys.exit(1)
            else:
                 # Try to find it if regex was slightly off
                 # E.g. log said 'ja/issue-2829' but regex captured 'ja/issue-2829 data'
                 print(f"⚠️ File not found at calculated path: {full_path}")
                 print("Dumping log snippet:")
                 print(output[-500:])
                 
                 # Try manual fallback for the specific format seen in logs
                 m2 = re.search(r'\[InvalidContentEntryDataError\] blog -> (.*?)\s', output)
                 if m2:
                     p2 = m2.group(1)
                     if not p2.endswith(".md"): p2 += ".md"
                     fp2 = os.path.join(os.getcwd(), "src", "content", "blog", p2)
                     if os.path.exists(fp2):
                         print(f"💣 FOUND CULPRIT (Fallback): {p2}")
                         os.remove(fp2)
                         print("   🗑️ DELETED.")
                     else:
                        print("❌ Could not locate file. Stopping.")
                        sys.exit(1)
                 else:
                     sys.exit(1)
        else:
            print("❌ Build failed but could not identify a specific file in the logs.")
            print("Last 1000 chars of log:")
            print(output[-1000:])
            sys.exit(1)
            
    if attempts >= max_attempts:
        print("⚠️ Max attempts reached. There are too many errors!")

if __name__ == "__main__":
    main()

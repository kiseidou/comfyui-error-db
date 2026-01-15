
import os
import json
import urllib.request
import urllib.error
import time
from datetime import datetime
import subprocess
import re
import yaml 

# --- Configuration ---
SOURCE_REPOS = [
    {"name": "comfyanonymous/ComfyUI", "short": "ComfyUI", "role": "ComfyUI Expert"},
    {"name": "Unity-Technologies/ml-agents", "short": "UnityML", "role": "Unity Machine Learning Expert"},
    {"name": "pypa/pip", "short": "Python", "role": "Python Package Expert"},
    {"name": "civitai/civitai", "short": "CivitAI", "role": "AI Model Resource Expert"},
    {"name": "huggingface/transformers", "short": "HuggingFace", "role": "AI Transformer Architecture Expert"},
    {"name": "facebook/react-native", "short": "ReactNative", "role": "Cross-Platform Mobile Dev Expert"},
]
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:14b" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "src", "content", "blog")

def get_issues(repo_config, page=1):
    """Fetch closed issues from GitHub"""
    url = f"https://api.github.com/repos/{repo_config['name']}/issues?state=closed&sort=comments&direction=desc&per_page=100&page={page}"
    print(f"Fetching hot topics from {url}...")
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Python-Factory-Bot')
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching issues: {e}")
        return []

def generate_content(issue, repo_config, lang="ja"):
    """
    Generate content in specific language.
    lang: "ja", "en", "zh"
    """
    title = issue.get('title', 'No Title')
    body = issue.get('body', '')
    if not body: return None
    
    role = repo_config['role']
    short_name = repo_config['short']

    # --- Prompt Switching ---
    if lang == "ja":
        prompt = f"""
        あなたは{role}です。
        以下のGitHub Issue（不具合報告）を元に、「エラー解決の完全ガイド」を日本語で作成してください。
        
        【構成】
        1. タイトル: "【完全解決】{short_name}で「{title}」エラーの対処法"
        2. フロントマター(厳守):
           ---
           title: "【{short_name}】{title} の完全解決ガイド"
           description: "Error fix guide for {title}"
           pubDate: "{datetime.now().strftime('%Y-%m-%d')}"
           ---
        3. 本文: 初心者向けに、原因と解決コマンド(pip install等)を解説。
        
        【Issue】
        {body[:1500]}
        """
    elif lang == "zh":
         prompt = f"""
        你是一位 {role}。
        根据以下的 GitHub Issue，创建一个“错误解决完全指南（简体中文）”。
        
        【结构】
        1. 标题: "【完美解决】{short_name} 报错 “{title}” 的修复方法"
        2. Frontmatter (必须遵守):
           ---
           title: "【{short_name}】{title} 完美解决指南"
           description: "{short_name} Error fix for {title}"
           pubDate: "{datetime.now().strftime('%Y-%m-%d')}"
           ---
        3. 正文: 针对初学者，解释原因并提供具体的解决命令（如 pip install 等）。
        
        【Issue】
        {body[:1500]}
        """
    else: # English
        prompt = f"""
        You are a {role}.
        Based on the GitHub Issue below, create a "Complete Error Fix Guide".

        [Structure]
        1. Title: "How to fix '{title}' in {short_name}"
        2. Frontmatter:
           ---
           title: "How to fix '{title}' in {short_name}"
           description: "Step-by-step fix for {title}"
           pubDate: "{datetime.now().strftime('%Y-%m-%d')}"
           ---
        3. Body: Explain cause and solution commands (pip install etc) for beginners.

        [Issue]
        {body[:1500]} 
        """

    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    print(f"Generating [{lang.upper()}] article for: {title}...")
    try:
        req = urllib.request.Request(OLLAMA_API_URL, data=json.dumps(data).encode(), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            raw_md = result['response']
            
            # --- Sanitization ---
            if "###" in raw_md and "Frontmatter" in raw_md:
                raw_md = raw_md.replace("### Frontmatter", "")
            
            match = re.search(r'^---\s*\n(.*?)\n---\s*\n', raw_md, re.DOTALL | re.MULTILINE)
            
            if match:
                yaml_content = match.group(1)
                # Basic cleanup of common YAML errors we've seen
                # e.g. **title:** instead of title:
                # Also handle *title*: etc
                yaml_check = re.sub(r'^\s*[*]*([a-zA-Z0-9_]+)[*]*\s*:', r'\1:', yaml_content, flags=re.MULTILINE)
                
                try:
                    yaml.safe_load(yaml_check)
                    raw_md = raw_md.replace(yaml_content, yaml_check)
                except yaml.YAMLError:
                    match = None 

            if not match:
                if "---" in raw_md: raw_md = raw_md.split("---")[-1]
                
                # Default Frontmatter Fallback
                t_safe = title.replace('"', '\\"').replace(':', ' -')
                if lang == "ja":
                    raw_md = f'---\ntitle: "【{short_name}】{t_safe} 解決ガイド"\ndescription: "Fix: {t_safe}"\npubDate: "{datetime.now().strftime("%Y-%m-%d")}"\n---\n{raw_md.strip()}'
                elif lang == "zh":
                    raw_md = f'---\ntitle: "【{short_name}】{t_safe} 修复指南"\ndescription: "Fix: {t_safe}"\npubDate: "{datetime.now().strftime("%Y-%m-%d")}"\n---\n{raw_md.strip()}'
                else:
                    raw_md = f'---\ntitle: "Fix {t_safe} in {short_name}"\ndescription: "Fix: {t_safe}"\npubDate: "{datetime.now().strftime("%Y-%m-%d")}"\n---\n{raw_md.strip()}'
            
            return raw_md

    except Exception as e:
        print(f"Error generating ({lang}): {e}")
        return None

def save_article(article_data, issue_number, repo_config, lang="ja"):
    if not article_data: return
    target_dir = os.path.join(CONTENT_DIR, lang)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    # NEW: Filename includes repo short name to avoid collisions
    filename = f"issue-{repo_config['short']}-{issue_number}.md"
    filepath = os.path.join(target_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(article_data)
    print(f"Saved [{lang}]: {filepath}")

def git_push_batch(count):
    print(f"\n🚀 Batch update: Pushing {count}th items...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "--allow-empty", "-m", f"Auto-deploy: New Global Content (Batch {count//20})"], check=True)
        subprocess.run(["git", "push", "origin", "deploy-final-v2"], check=True) # Ensure correct branch
        print("✅ Shipment complete!\n")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git push failed: {e}")

import shutil

# ... existing imports ...

def self_diagnose():
    print("🏥 Running Self-Diagnosis...")
    langs = ["ja", "en", "zh"]
    
    if not os.path.exists(CONTENT_DIR):
        os.makedirs(CONTENT_DIR, exist_ok=True)
        
    for lang in langs:
        path = os.path.join(CONTENT_DIR, lang)
        if os.path.exists(path):
            if os.path.isfile(path):
                print(f"⚠️ CRITICAL: '{lang}' is a file! Renaming and creating directory.")
                backup_name = path + f"_backup_{int(time.time())}.md"
                os.rename(path, backup_name)
                os.makedirs(path, exist_ok=True)
                # Move backup into the folder
                try: shutil.move(backup_name, os.path.join(path, f"restored_{int(time.time())}.md"))
                except: pass
        else:
            os.makedirs(path, exist_ok=True)

    # --- NEW: Corrupt File Sweeper (Repair Mode) ---
    print("🧹 Scanning for corrupt articles and attempting repair...")
    from repair_corrupt_files import repair_file

    valid_count = 0
    repaired_count = 0
    deleted_count = 0
    
    for root, dirs, files in os.walk(CONTENT_DIR):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                try:
                    # repair_file returns True if valid/repaired, False if effectively empty/unusable
                    if repair_file(path):
                        valid_count += 1
                        # We don't distinguish valid vs repaired in return boolean easily without changing signature,
                        # but the script prints logs. We'll simply count "survived" files.
                    else:
                        print(f"💣 Deleting unrecoverable file: {f}")
                        os.remove(path)
                        deleted_count += 1
                        
                except Exception as e:
                    print(f"⚠️ Error checking {f}: {e}")
                    
    print(f"✅ Diagnosis Complete. Verified/Repaired: {valid_count}, Deleted: {deleted_count}")

def main():
    print("=== ComfyUI & Unity Error Database Factory v4.0 (Multi-Repo) ===")
    self_diagnose()
    
    page = 1

    total_items = 0
    
    while True:
        print(f"\n--- Starting Page {page} ---")
        
        # Iterate over all repositories
        for repo in SOURCE_REPOS:
            print(f"\n=== Processing Repo: {repo['name']} ===")
            issues = get_issues(repo, page)
            
            if not issues:
                print(f"No more issues for {repo['name']} on page {page}.")
                continue

            print(f"Found {len(issues)} popular issues for {repo['name']}. Production running...")
            
            success_count_batch = 0
            for issue in issues:
                # 1. Japanese
                if not os.path.exists(os.path.join(CONTENT_DIR, "ja", f"issue-{repo['short']}-{issue['number']}.md")):
                    art = generate_content(issue, repo, "ja")
                    save_article(art, issue['number'], repo, "ja")
                    success_count_batch += 1
                    total_items += 1
                
                # 2. English
                if not os.path.exists(os.path.join(CONTENT_DIR, "en", f"issue-{repo['short']}-{issue['number']}.md")):
                    art = generate_content(issue, repo, "en")
                    save_article(art, issue['number'], repo, "en")
                    success_count_batch += 1
                    total_items += 1
                    
                # 3. Chinese
                if not os.path.exists(os.path.join(CONTENT_DIR, "zh", f"issue-{repo['short']}-{issue['number']}.md")):
                    art = generate_content(issue, repo, "zh")
                    save_article(art, issue['number'], repo, "zh")
                    success_count_batch += 1
                    total_items += 1

                if success_count_batch > 0 and success_count_batch % 5 == 0: # Faster push for testing
                    git_push_batch(total_items)

                time.sleep(1)
                
        print(f"=== Page {page} Complete. ===")
        page += 1
        print("Moving to next page in 60 seconds...")
        time.sleep(60)

if __name__ == "__main__":
    main()

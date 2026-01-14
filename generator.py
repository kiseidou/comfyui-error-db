import os
import json
import urllib.request
import urllib.error
import time
from datetime import datetime
import subprocess

# --- Configuration ---
# ターゲットリポジトリ (Target Repository)
GITHUB_REPO = "comfyanonymous/ComfyUI"
# Ollamaのエンドポイント (Ollama Endpoint)
OLLAMA_API_URL = "http://localhost:11434/api/generate"
# 使用するモデル (Model Name) - Make sure to run 'ollama pull llama3' first!
MODEL_NAME = "qwen2.5:14b" 
# 記事の保存先 (Output Directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "src", "content", "blog")

def get_issues(page=1):
    """GitHubからClosedなIssueを取得する (人気順)"""
    # sort=comments でコメントが多い順（＝みんなが困っている/議論が活発な順）に取得
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues?state=closed&sort=comments&direction=desc&per_page=100&page={page}"
    print(f"Fetching hot topics from {url}...")
    try:
        req = urllib.request.Request(url)
        # GitHub API requires a User-Agent
        req.add_header('User-Agent', 'Python-Factory-Bot')
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching issues: {e}")
        return []

# ... (generate_article, save_article, git_push_batch remain largely same but ensure context) ...

def main():
    print("=== ComfyUI Error Database Factory v3.0 (Infinite Loop) ===")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
    page = 1
    total_articles = 0
    
    while True:
        print(f"\n--- Starting Page {page} ---")
        issues = get_issues(page)
        
        if not issues:
            print(f"No more issues found on page {page}. Resetting to Page 1 in 1 hour.")
            time.sleep(3600) # Sleep 1 hour before restart
            page = 1
            continue

        print(f"Found {len(issues)} popular issues on page {page}. Production running...")
        
        success_count_batch = 0
        for issue in issues:
            filename = f"issue-{issue['number']}.md"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            # Skip if exists (Fast Skip)
            if os.path.exists(filepath):
                # print(f"Skipping existing issue #{issue['number']}")
                continue

            article = generate_article(issue)
            if article:
                save_article(article, issue['number'])
                success_count_batch += 1
                total_articles += 1
                
                # Push every 5 new articles
                if success_count_batch > 0 and success_count_batch % 5 == 0:
                    git_push_batch(total_articles)

            time.sleep(1) 
            
        print(f"=== Page {page} Complete. New Articles: {success_count_batch} ===")
        
        # If we didn't generate anything new on this page, it might be fully scraped.
        # But we still move to next page to find older issues we haven't scraped.
        
        page += 1
        print("Moving to next page in 10 seconds...")
        time.sleep(10)

if __name__ == "__main__":
    main()

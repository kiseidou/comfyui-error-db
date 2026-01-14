
import os
import json
import urllib.request
import urllib.error
import time
from datetime import datetime
import subprocess
import re
import yaml # Check validity

# --- Configuration ---
GITHUB_REPO = "comfyanonymous/ComfyUI"
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:14b" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "src", "content", "blog")

def get_issues(page=1):
    """GitHubからClosedなIssueを取得する (人気順) - Infinite Page Loop support"""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues?state=closed&sort=comments&direction=desc&per_page=100&page={page}"
    print(f"Fetching hot topics from {url}...")
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Python-Factory-Bot')
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching issues: {e}")
        return []

def generate_article(issue):
    """Ollamaを使って日本語記事を生成する"""
    title = issue.get('title', 'No Title')
    body = issue.get('body', '')
    if not body:
        return None
    
    prompt = f"""
    あなたはComfyUIのエキスパートであり、初心者にも優しく教える「技術系メンター」です。
    以下のGitHub Issue（不具合報告）を元に、
    「誰でも確実にエラーを解決できる完全ガイド（チュートリアル記事）」を作成してください。

    【ターゲット読者】
    - ComfyUIを使っているが、Pythonやプログラミングには詳しくないクリエイター
    - エラーが出て困り果てており、手取り足取り教えてほしい人

    【記事の構成ルール】
    1. **キャッチーなタイトル**:
       - "【完全解決】ComfyUIで「{title}」エラーが出た時の対処法" 
    2. **フロントマター**: 以下の形式を厳守。
       ---
       title: "【ComfyUI】{title} の完全解決ガイド"
       description: "ComfyUIのエラー '{title}' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
       pubDate: "{datetime.now().strftime('%Y-%m-%d')}"
       ---
       ※注意: キー名にアスタリスク(**)を使わないこと。正しいYAML形式を守ること。
    3. **本文構成**:
       - **はじめに**: 読者に寄り添う導入。
       - **原因の解説**: 技術用語を噛み砕いて説明。
       - **解決ステップ (Step-by-Step)**: 具体的なコマンドや操作。
       - **まとめ**: 励ましの言葉。

    【元データ (Issue)】
    {body[:2500]} 
    """
    
    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    print(f"Asking AI to write a tutorial about: {title}...")
    try:
        req = urllib.request.Request(OLLAMA_API_URL, data=json.dumps(data).encode(), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            raw_md = result['response']
            
            # --- Sanitization & Validation ---
            
            # 1. Clean up "### Frontmatter" hallucinations
            if "### フロントマター:" in raw_md:
                raw_md = raw_md.replace("### フロントマター:", "")
            
            # 2. Extract YAML block
            match = re.search(r'^---\s*\n(.*?)\n---\s*\n', raw_md, re.DOTALL | re.MULTILINE)
            
            if match:
                # Validate YAML
                yaml_content = match.group(1)
                # Remove bolding if present
                yaml_content_clean = yaml_content.replace('**title:**', 'title:').replace('**description:**', 'description:').replace('**pubDate:**', 'pubDate:')
                
                try:
                    # Test parse
                    yaml.safe_load(yaml_content_clean)
                    # If valid, replace the original block with clean block
                    raw_md = raw_md.replace(yaml_content, yaml_content_clean)
                except yaml.YAMLError:
                    print(f"⚠️ Invalid YAML generated for {title}. Regenerating default.")
                    match = None # Force fallback

            # 3. Fallback if no valid frontmatter
            if not match:
                # Remove any broken top content
                if "---" in raw_md:
                     raw_md = raw_md.split("---")[-1]

                raw_md = f"""---
title: "【ComfyUI】{title.replace('"', '\\"').replace(':', ' -')} の完全解決ガイド"
description: "ComfyUI Error: {title.replace('"', '\\"').replace(':', ' -')}"
pubDate: "{datetime.now().strftime('%Y-%m-%d')}"
---
{raw_md.strip()}"""
            
            return raw_md

    except Exception as e:
        print(f"Error generating article: {e}")
        return None

def save_article(article_data, issue_number):
    """記事をMarkdownファイルとして保存する"""
    if not article_data:
        return

    filename = f"issue-{issue_number}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(article_data)
    print(f"Saved: {filepath}")

def git_push_batch(count):
    """記事をGitHubにPushしてCloudflare Pagesの更新をトリガーする"""
    print(f"\n🚀 Batch update: Pushing {count}th article to production...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "--allow-empty", "-m", f"Auto-deploy: New Tutorial Articles (Batch {count//10})"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Shipment complete! Site is updating...\n")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git push failed: {e}")

def main():
    print("=== ComfyUI Error Database Factory v3.1 (Infinite + Robust) ===")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
    page = 1
    total_articles = 0
    
    while True:
        print(f"\n--- Starting Page {page} ---")
        issues = get_issues(page)
        
        if not issues:
            print(f"No more issues found on page {page}. Resetting to Page 1 in 1 hour.")
            time.sleep(3600)
            page = 1
            continue

        print(f"Found {len(issues)} popular issues on page {page}. Production running...")
        
        success_count_batch = 0
        for issue in issues:
            filename = f"issue-{issue['number']}.md"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            if os.path.exists(filepath):
                continue
            
            # Generate
            article = generate_article(issue)
            
            if article:
                # Final Paranoid Check: Does it start with ---?
                if not article.strip().startswith("---"):
                    print(f"❌ Critical: Generated article for #{issue['number']} missing frontmatter. Skipping.")
                    continue
                    
                save_article(article, issue['number'])
                success_count_batch += 1
                total_articles += 1
                
                if success_count_batch > 0 and success_count_batch % 5 == 0:
                    git_push_batch(total_articles)

            time.sleep(1) 
            
        print(f"=== Page {page} Complete. New Articles: {success_count_batch} ===")
        page += 1
        print("Moving to next page in 10 seconds...")
        time.sleep(10)

if __name__ == "__main__":
    main()

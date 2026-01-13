import os
import json
import urllib.request
import urllib.error
import time
from datetime import datetime

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

def get_issues():
    """GitHubからClosedなIssueを取得する"""
    # 5件だけ取得 (Start small)
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues?state=closed&per_page=5"
    print(f"Fetching issues from {url}...")
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
    
    # AIへの指示書 (Prompt)
    prompt = f"""
    You are a technical writer managing a blog about ComfyUI error solutions.
    Analyze the following GitHub Issue and output the result in JSON format.
    
    Issue Title: {title}
    Issue Body: {body}
    
    Task:
    1. Identify the 'Cause of Error' (エラーの原因).
    2. Identify the 'Solution' (解決策).
    3. Create a catchy Japanese blog title (title).
    4. Write a 50-character Japanese summary (description).
    5. Compose the full blog post in Japanese Markdown (content_markdown). Use headers (## causes, ## solutions).
    
    Output Format (JSON Only):
    {{
        "title": "...",
        "description": "...",
        "content_markdown": "..."
    }}
    """
    
    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "format": "json",
        "stream": False
    }
    
    print(f"Asking AI to write about: {title}...")
    try:
        req = urllib.request.Request(OLLAMA_API_URL, data=json.dumps(data).encode(), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            # Parse the JSON inside the response text
            ai_response_text = result['response']
            return json.loads(ai_response_text)
    except urllib.error.URLError as e:
        print(f"Connection Error to Ollama: {e}")
        print("Hint: Is Ollama running? (Start 'Ollama' from Start Menu)")
        return None
    except Exception as e:
        print(f"Error generating article: {e}")
        return None

def save_article(article_data, issue_number):
    """記事をMarkdownファイルとして保存する"""
    if not article_data:
        return

    today = datetime.now().strftime('%Y-%m-%d')
    safe_title = "".join([c for c in article_data['title'] if c.isalnum() or c in (' ', '-', '_')]).strip()
    filename = f"issue-{issue_number}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Astro Blog Frontmatter
    md_content = f"""---
title: '{article_data['title']}'
description: '{article_data['description']}'
pubDate: '{today}'
---

{article_data['content_markdown']}

<br>

---
*この記事はAIによって自動生成されました。 [元のIssue #{issue_number}](https://github.com/{GITHUB_REPO}/issues/{issue_number})*
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Saved: {filepath}")

def main():
    print("=== ComfyUI Error Database Factory ===")
    
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        print(f"Creating directory: {OUTPUT_DIR}")
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
    issues = get_issues()
    if not issues:
        print("No issues found or network error.")
        return

    print(f"Found {len(issues)} issues. Starting production...")
    
    success_count = 0
    for issue in issues:
        article = generate_article(issue)
        if article:
            save_article(article, issue['number'])
            success_count += 1
        time.sleep(1) 
        
    print(f"=== Production Complete: {success_count} articles generated. ===")
    print("Run 'npm run dev' to view your site.")

if __name__ == "__main__":
    main()

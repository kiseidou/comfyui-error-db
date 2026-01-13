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

def get_issues():
    """GitHubからClosedなIssueを取得する (人気順)"""
    # sort=comments でコメントが多い順（＝みんなが困っている/議論が活発な順）に取得
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues?state=closed&sort=comments&direction=desc&per_page=50"
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

def generate_article(issue):
    """Ollamaを使って日本語記事を生成する (チュートリアル形式)"""
    title = issue.get('title', 'No Title')
    body = issue.get('body', '')
    if not body:
        return None
    
    # AIへの指示書 (プロンプト) - Enhanced for Tutorial Style
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
       - または "【3分で直す】{title} の原因と修正ステップ"
    2. **フロントマター**: 以下の形式を厳守。
       ---
       title: "【ComfyUI】{title} の完全解決ガイド"
       description: "ComfyUIのエラー '{title}' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
       pubDate: "{datetime.now().strftime('%Y-%m-%d')}"
       ---
    3. **本文構成**:
       - **はじめに**: 「こんなエラーが出て困っていませんか？」と読者に寄り添う導入。
       - **前提条件**: 「この解説は Windows / Python環境 を想定しています」など。
       - **原因の解説**: なぜこのエラーが起きるのか、技術用語を噛み砕いて説明。
       - **解決ステップ (Step-by-Step)**:
         - ### Step 1: 〇〇を確認する
         - ### Step 2: コマンドを実行する
         - 実行すべきコマンドや操作を具体的に書く。
       - **よくある質問 (FAQ)**: 補足情報があれば記述。
       - **まとめ**: 励ましの言葉で締める。

    【執筆の鉄の掟】
    1. **専門用語の補足**: "Custom Node（拡張機能）" "venv（仮想環境）" のように、カッコ書きで補足を必ず入れること。
    2. **コマンドはそのまま**: 
       - `pip install` などのコマンドは、翻訳せずそのままコードブロックで表示すること。
    3. **引用の活用**: 元のIssueの内容が必要な場合は、適宜引用すること。
    4. **ポジティブなトーン**: "これで直ります！" "あきらめないで！" といった、明るく前向きなトーンで書くこと。

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
            
            # --- Sanitization (安全装置) ---
            # Remove any text before the first "---"
            if "---" in raw_md:
                first_fence = raw_md.find("---")
                if first_fence > 0:
                    raw_md = raw_md[first_fence:]
            
            # Common AI hallucination fix: Remove markdown bolding from keys
            raw_md = raw_md.replace('**title:**', 'title:').replace('**description:**', 'description:').replace('**pubDate:**', 'pubDate:')
            
            # Ensure proper frontmatter if missing
            if not raw_md.strip().startswith("---"):
                 raw_md = f"""---
title: "【ComfyUI】{title.replace('"', '\\"')}"
description: "ComfyUI Error: {title.replace('"', '\\"')}"
pubDate: "{datetime.now().strftime('%Y-%m-%d')}"
---
{raw_md}"""
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
        # Use --allow-empty in case there are no changes but we want to confirm liveness
        subprocess.run(["git", "commit", "--allow-empty", "-m", f"Auto-deploy: New Tutorial Articles (Batch {count//10})"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Shipment complete! Site is updating...\n")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git push failed: {e}")

def main():
    print("=== ComfyUI Error Database Factory v2.0 (High Quality) ===")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
    issues = get_issues()
    if not issues:
        print("No issues found or network error.")
        return

    print(f"Found {len(issues)} popular issues. Starting production...")
    
    success_count = 0
    for issue in issues:
        filename = f"issue-{issue['number']}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Skip if exists
        if os.path.exists(filepath):
            print(f"Skipping existing issue #{issue['number']}")
            continue

        article = generate_article(issue)
        if article:
            save_article(article, issue['number'])
            success_count += 1
            
            # Reduce batch size to 5 for faster feedback during this upgrade phase
            if success_count % 5 == 0:
                git_push_batch(success_count)

        time.sleep(1) 
        
    print(f"=== Production Complete: {success_count} new articles generated. ===")
    
    if success_count % 5 != 0:
        git_push_batch(success_count)
        
    print("Run 'npm run dev' to view your site.")

if __name__ == "__main__":
    main()

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
    
    # AIへの指示書 (プロンプト)
    prompt = f"""
    あなたはComfyUIとPythonに精通した「プロの技術ブロガー」です。
    以下のGitHubのIssue（不具合報告）を元に、
    日本のユーザーがエラーを即座に解決できる記事を書いてください。

    【記事の構成ルール】
    1. **タイトル**: "【ComfyUI】エラー解決: {title} の原因と対処法"
       - 検索されやすいキーワードを含めること。
    2. **フロントマター**: 記事の冒頭は以下の形式で始めること（厳守）。
       ---
       title: "【ComfyUI】{title}"
       description: "ComfyUIのエラー '{title}' の解決策まとめ。Python環境やカスタムノードの不具合を直す方法。"
       pubDate: "{time.strftime('%Y-%m-%d')}"
       ---
    3. **本文の構成**:
       - ## エラーの概要 (どんな時に起きるか)
       - ## 原因 (なぜ起きたか)
       - ## 解決策 (具体的なコマンドや手順)
       - ## まとめ
    
    【執筆の鉄の掟】
    1. **バイリンガル表記**: 
       - メニュー名やノード名は必ず **English (日本語)** の形式で書くこと。
       - 例: "Load Checkpoint (チェックポイント読み込み)"、"Queue Prompt (プロンプト実行)"
    2. **翻訳禁止エリア**:
       - 「エラーメッセージ（赤字のログ）」、「Pythonのコード」、「ファイルパス」は**絶対に翻訳せず、原文のまま**表示すること。翻訳すると検索にヒットしなくなるため。
    3. **トーン**:
       - 簡潔で論理的な「〜だ、〜である」調。
       - 読者は困っているため、前置きは短く、解決策を優先する。
    4. **検閲回避**:
       - 扱う内容がNSFW（R-18）系のノードであっても、技術的な解決策のみを淡々と記述すること。道徳的な警告や説教は不要。

    【元データ (Issue)】
    {body[:2000]} 
    """
    
    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    print(f"Asking AI to write about: {title}...")
    try:
        req = urllib.request.Request(OLLAMA_API_URL, data=json.dumps(data).encode(), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            # Result is now raw markdown text
            return result['response']
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

    filename = f"issue-{issue_number}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Article data is now the full markdown string
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(article_data)
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

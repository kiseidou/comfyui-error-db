---
title: "【CivitAI】File endpoints: use query parameters for NGINX/Caddy compatibility の完全解決ガイド"
description: "ComfyUIのエラー 'File endpoints: use query parameters for NGINX/Caddy compatibility' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

## はじめに

ComfyUIを使っているときに「File endpoints: use query parameters for NGINX/Caddy compatibility」というエラーが出たことがありますか？この記事では、その原因と解決方法を初心者にもわかりやすく解説します。問題が解決すれば次のステップに進むことができますよ！

## 前提条件

- オペレーティングシステム：Windows（他のOSでも大体同じ手順です）
- Python環境があること
- ComfyUIのインストールと初期設定が完了していること
- NGINXやCaddyを経由してComfyUIにアクセスしようとしている

## 原因の解説

このエラーは、ComfyUIをNGINXなどのプロキシサーバー経由で使用するときに発生します。ファイルに関連したエンドポイント（API）がURLのパス部分にあるため、プロキシサーバーによってURLエンコードが変更されることがあります。

例えば、プロキシサーバーが URL をデコードすると、ComfyUI は意図しない状態でリクエストを処理しようとして `405 Method Not Allowed` エラーとなります。これは「NGINX/Caddyなどのプロキシサーバーと互換性があるように、ファイルパスをクエリパラメータに変更すべき」というメッセージです。

## 解決ステップ (Step-by-Step)

### Step 1: ComfyUIの最新版をインストールする

まず、最新バージョンのComfyUIをダウンロードしてインストールします。これにより、`File endpoints: use query parameters for NGINX/Caddy compatibility` の修正が含まれているはずです。

#### コマンド
```
git clone https://github.com/ComfyUI-Project/CompyUI.git
cd ComfyUI
pip install -r requirements.txt
```

### Step 2: サーバー設定を更新する

次に、NGINXやCaddyの設定ファイルを開き、適切なリバースプロキシ設定を行います。具体的には、クエリパラメータを使用してファイルパスを扱うように変更します。

#### NGINXの場合
```
location / {
    proxy_pass http://localhost:8188;
    # クエリパラメータでファイルパスを指定する必要がある場合の設定例
    rewrite ^/userdata/workflows/(.*)$ /api/userdata/workflows?$args break;
}
```

#### Caddyの場合
Caddyの設定はNGINXとは異なりますが、基本的には同じようにクエリパラメータを使用します。
```
reverse_proxy localhost:8188 {
    # この部分にクエリパラメータに関するルールを追加
}
```

### Step 3: 前提条件の再確認と実行

最後に、ComfyUIを最新版にアップデートし、プロキシサーバー設定を更新したことを確認してからサーバーを起動します。

```
python run.py --host 0.0.0.0
```

## よくある質問 (FAQ)

- **Q: ComfyUIをGitHubから直接インストールしたらエラーが出る**
    - A: GitHubのブランチやタグは常に最新版とは限りません。プロジェクトページで提供されているインストール手順に従ってください。

## まとめ

「File endpoints: use query parameters for NGINX/Caddy compatibility」エラーには少々複雑な背景がありますが、手順通りに進めばすぐに解決できます。ComfyUIの開発チームは常に改善に努めていますので、安心してご利用ください！
---
title: "【HuggingFace】Connection Errorの完全解決ガイド"
description: "ComfyUIでHugging Face Hub接続エラー（Connection Error）が出た時の原因と修正手順を解説します。"
pubDate: "2026-01-14"
---

### はじめに
こんなエラーが出て困っていませんか？

```
An error happened while trying to locate the file on the Hub and we cannot find the requested files in the local cache. Please check your connection and try again or make sure your Internet connection is on.
```

この記事では、ComfyUIを初めて使うクリエイターでも簡単に解決できるよう、ステップバイステップで手順を解説します。

### 前提条件
このガイドは Windows 環境と Python の仮想環境（`venv`）を前提としています。既に ComfyUI をインストール済みであることを確認してください。

### なぜエラーが起きるのか？

ComfyUI は、モデルやノードのファイルをダウンロードするために Hugging Face Hub (Custom Node の一例) から必要なリソースを取り込む必要があります。しかし、何かしらの理由でインターネット接続に問題があったり、Hub からのアクセスが遮断されていると、このエラーが発生します。

### 解決ステップ (Step-by-Step)

#### Step 1: 接続状況を確認する
まずは、お使いのデバイスがインターネットに正常に接続できているかチェックしてください。ブラウザで Hugging Face Hub（または `https://hf-mirror.com/`）へアクセスできるかどうか試してみましょう。

#### Step 2: 実行環境の確認と設定変更
1. **ComfyUI の実行ディレクトリに移動**します。通常は仮想環境が作成されているフォルダ内にあるはずです。
   
   ```bash
   cd /path/to/your/comfyui/directory
   ```

2. **`config.json` ファイルを開いて、URL の設定を変更**しましょう。「huggingface.co」から「https://hf-mirror.com/」に変更します。

   - `config.json` が存在しない場合は作成してください。
   - `config.json` の中身は以下の通りです（既存の内容に追記）：

     ```json
     {
       "HF_HUB_URL": "https://hf-mirror.com/"
     }
     ```

3. **設定を保存**し、ComfyUI を再起動します。

### よくある質問 (FAQ)

- **Q: 設定ファイルが見つからない場合は？**
  - `config.json` は ComfyUI のルートディレクトリ内に配置してください。もしそこになければ新規作成して上記の内容を追加します。

### まとめ
エラーを解決するには、インターネット接続と設定ファイルを確認することが重要です。これらの手順を踏むことで ComfyUI の問題はすぐに解消できるはずです！あきらめずにチャレンジしましょう！

---
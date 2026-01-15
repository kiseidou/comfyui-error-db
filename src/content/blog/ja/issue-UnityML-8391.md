---
title: "【UnityML】mat1 and mat2 shapes cannot be multiplied (1x1 and 768x3072) K sampler issue の完全解決ガイド"
description: "ComfyUIのエラー 'mat1 and mat2 shapes cannot be multiplied (1x1 and 768x3072) K sampler issue' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

## 【UnityML】mat1 and mat2 shapes cannot be multiplied (1x1 and 768x3072) K sampler issue の完全解決ガイド

### はじめに
こんにちは、クリエイターの皆さん！ComfyUIを使って画像生成やAIアートを楽しんでいる中で「mat1 and mat2 shapes cannot be multiplied (1x1 and 768x3072)」というエラーが出たことありませんか？この記事では、そんなエラーが発生した時にどう対処するべきかを初心者にもわかりやすく解説します。これで安心してComfyUIを使い続けられますよ！

### 前提条件
- オペレーティングシステム：Windows / Linux / macOS
- Python環境：Python 3.7 以上がインストールされていること
- ComfyUI：最新版またはエラーが発生するバージョン

### 原因の解説
このエラーは、ComfyUIでKSamplerノード（画像生成やAIアートを実行する際に重要な役割を持つ拡張機能）を使用している際に発生します。具体的には、数値行列が正しく計算できない状況で発生します。

「mat1 and mat2 shapes cannot be multiplied (1x1 and 768x3072)」とは、「2つの配列（matrix）のサイズ（shape）が掛け算として不適切である」という意味です。この場合、一つは1行1列の行列と768行3072列の行列を掛けるよう指示しており、これは数学的には不可能な計算となります。

### 解決ステップ (Step-by-Step)

#### Step 1: 環境設定を確認する
まず、Pythonの仮想環境（venv）が正しく設定されているかチェックしてください。ComfyUIは複数の依存関係を持つため、適切なバージョンのライブラリがインストールされていることが重要です。

##### コマンド:
```bash
python -m venv my_comfy_env
source my_comfy_env/bin/activate  # Windowsの場合、コマンドを `my_comfy_env\Scripts\activate` に変更してください。
pip install comfyui
```

#### Step 2: カスタムノードの影響を確認する
カスタムノード（拡張機能）がエラーを引き起こしている可能性があります。一時的にすべてのカスタムノードを無効にして、問題が解消するかどうか試してみましょう。

##### コマンド:
ComfyUIの公式ドキュメントに記載されている手順に従ってください：
- [カスタムノードの問題をテストする](https://docs.comfy.org/troubleshooting/custom-node-issues#step-1%3A-test-with-all-custom-nodes-disabled)

#### Step 3: ノードの設定を再確認する
KSamplerノードを使用している場合、そのパラメータが適切に設定されているか再度確認してください。特に、「Latent Channels」や「Steps」などの重要なフィールドを見直します。

### よくある質問 (FAQ)

**Q: 他のエラーも同時に表示される場合は？**
A: この記事の対処法を試しても解決しない場合、複数の問題が絡んでいる可能性があります。まずは各エラーメッセージの内容を理解し、順番に対策していきましょう。

**Q: エラーが出る場所は特定できますか？**
A: スタックトレース（上記ログ）を見ると、エラーが発生した箇所や関連するコードスニペットを見つけることができます。詳細な情報があれば、原因をより具体的に特定できます。

### まとめ
「mat1 and mat2 shapes cannot be multiplied (1x1 and 768x3072)」というエラーは複雑そうに見えますが、一つずつ手順を追って確認すれば必ず解決します！初期設定からカスタムノードの影響まで、ステップバイステップで進めてみてください。あきらめずに挑戦すれば、ComfyUIでの創作活動がさらに楽しくなること間違いなしです！

これでエラーから解放されましたか？もしご不明な点がありましたら、気軽にコメント欄でお聞きくださいね！
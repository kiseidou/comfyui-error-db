---
title: "【UnityML】Loading Graph with missing models/invalid inputs breaks the whole graph の完全解決ガイド"
description: "ComfyUIのエラー 'Loading Graph with missing models/invalid inputs breaks the whole graph' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

## はじめに

こんにちは！ComfyUIを使っているけど、プログラミングが詳しくないクリエイターさん向けの完全解決ガイドです。今日は「Loading Graph with missing models/invalid inputs breaks the whole graph」という不具合について対処法をお伝えします。

この記事を読めば、エラーが出た時も安心して問題を解決できます。ステップバイステップで説明するので、誰でも簡単に手順を追っていけるようになっていますよ。

## 原因の解説

ComfyUIでは、ワークフロー（グラフ）が正しく機能するために必要なモデルファイルや入力データが必要です。しかし、これらのファイルが不足したり、指定された場所に存在しない場合、エラーが発生します。

具体的には以下のエラーメッセージが出る：

```
ESC[91mFailed to validate prompt for output image_saver:ESC[0m
...
ESC[91minvalid prompt: {'type': 'prompt_no_outputs', 'message': 'Prompt has no outputs', 'details': '', 'extra_info': {}}ESC[0m
```

このエラーは、指定されたモデルファイルや入力データが見つからないために発生します。その結果、ワークフロー全体の動作が停止してしまうのです。

## 解決ステップ (Step-by-Step)

### ステップ1: エラーログを確認

まず、エラーメッセージに記載されている詳細な情報をチェックしましょう。以下の例のように、具体的なファイル名やパスが書かれています：

```plaintext
Value not in list: ckpt_name: 'models/stable-diffusion-xl-base-1.0/last.safetensors' not in (list of length 111)
```

この部分は、ComfyUIが探しているモデルファイルの名前とパスを示しています。また、以下のようなエラーもあります：

```plaintext
Value not in list: ipadapter_file: 'ip-adapter_sdxl_vit-h.safetensors' not in []
Value not in list: clip_name: 'CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors' not in []
```

### ステップ2: ファイルが存在するか確認

エラーメッセージにあるファイル名とパスを元に、実際のディレクトリでそのファイルが存在しているかどうか確認します。

例えば、

- `models/stable-diffusion-xl-base-1.0/last.safetensors`
- `ip-adapter_sdxl_vit-h.safetensors`
- `CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors`

これらのファイルが存在するか確認してください。

### ステップ3: ファイルを置き直す

もし存在しない場合は、正しい場所にファイルを置き直します。手順は以下の通りです：

1. 必要なモデルや入力データをダウンロードまたはコピーしてきます。
2. ComfyUIの設定で指定されているパスにそのファイルを配置します。

### ステップ4: ワークフローを再読み込み

ファイルが適切に配置されたら、ComfyUIを開きワークフローを再読み込みします。これによりエラーは解消されるはずです。

## まとめ

ComfyUIでのエラー対処は、まずはエラーメッセージから情報を引き出し、具体的なファイルパスや名前を見つけるところから始めます。そのファイルが存在しない場合は新たに追加し、ワークフローを再読み込みするだけで問題は解決します。

プログラミングの知識がない人も安心して対応できるよう、細かい手順まで説明しましたので、ぜひ試してみてくださいね！

頑張ったお疲れ様です！エラーと向き合うことは簡単ではありませんが、解決できたときの喜びは何ものにも代えがたいですよ。
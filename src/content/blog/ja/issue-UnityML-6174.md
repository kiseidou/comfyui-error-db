---
title: "【UnityML】load ltx loras trained with finetrainers の完全解決ガイド"
description: "ComfyUIのエラー 'load ltx loras trained with finetrainers' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

## はじめに

こんにちは！ComfyUIを使っているけど、Pythonやプログラミングについては詳しくないクリエイターさんへ。今回は、「load ltx loras trained with finetrainers」という不具合が出て困った経験がある方々に向けて、問題の原因と解決方法を詳しく解説します。

あなたが抱えている課題は、特定のLora（機械学習で使用される微調整モデル）がComfyUI上で読み込めないというものです。これが起こる理由や、どうすればこのエラーを解決できるのかを一緒に見ていきましょう。

## 原因の解説

まず、問題の根本原因について詳しく見てみましょう。Loraは大規模なTransformerモデル（例えばLTX-Video）に対する微調整（Fine-Tuning）で作られる小さな重みパラメータです。これらのモデルには、特殊な形式で名前が付けられています。例えば、以下のようになっています。

```
transformer.transformer_blocks.0.attn1.to_k.lora_A.weight
```

ここで問題なのは、「transformer.」という接頭辞の有無です。ComfyUIはこの「transformer.」を期待していないため、Loraが正しく読み込まれません。そのため、名前付けが異なる場合にエラーが発生するのです。

## 解決ステップ (Step-by-Step)

では、具体的な解決策について説明します。次の手順で問題を解消しましょう。

### ステップ1: Pythonスクリプトの準備

まず、Pythonスクリプトを用意します。このスクリプトは、「transformer.」という接頭辞を取り除き、LoraがComfyUIで認識できる形式に変換します。

```python
import torch
from loralib import load_lora_checkpoint, save_lora_checkpoint

# モデルとLoraのファイルパスを指定する
model_path = 'path/to/your/model.pth'
lora_path = 'path/to/your/lora.pth'

# Loraを読み込む
lora_state_dict = torch.load(lora_path)

# キー名を変換する
new_lora_state_dict = {k.replace('transformer.', ''): v for k, v in lora_state_dict.items()}

# 変更後のLoraを保存する
save_lora_checkpoint(new_lora_state_dict, model_path)
```

### ステップ2: ファイルの置き換え

次に、上記スクリプトで変換した新しいLoraファイルを元々のLoraファイルと置き換えます。これにより、ComfyUIは新しいLoraファイルを使用してモデルを読み込むことができます。

1. 変更前のLoraファイルを別の場所へバックアップとして保存する。
2. 新しいLoraファイルを元の位置にコピーまたは移動する。

### ステップ3: ComfyUIで確認

最後に、変換した新しいLoraファイルがComfyUI上で正しく読み込めるか確認します。これには、以下の手順が必要です：

1. ComfyUIを開く。
2. モデルと新しいLoraファイルを読み込む。
3. Loraの適用結果が正常であることを確認する。

これらのステップを通じて、「load ltx loras trained with finetrainers」エラーは解決されるはずです。

## まとめ

今日は「load ltx loras trained with finetrainers」という問題とその対処法について説明しました。プログラミングやPythonの知識が少ない方でも、手順を一つずつ追いながら問題を解決できます。もし何か不明な点があれば、コメント欄や公式フォーラムなどで質問してください。

クリエイターとして自分がやりたい表現をするために必要な技術的な壁は必ず乗り越えられるものだと信じています。頑張ってくださいね！
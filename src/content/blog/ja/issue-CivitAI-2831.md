---
title: "【CivitAI】Support for Stable Cascade LoRAs and embeddings の完全解決ガイド"
description: "ComfyUIのエラー 'Support for Stable Cascade LoRAs and embeddings' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

## はじめに

こんにちは！あなたのクリエイティブな旅において、ComfyUIは素晴らしいツールですが、時折遭遇するエラーがつまづきを生むことがありますね。特に「Support for Stable Cascade LoRAs and embeddings」エラーは複雑そうに見えますが、実はステップバイステップで解決することができます。この記事では、あなたが手元のプロジェクトをスムーズに進められるよう、具体的な対処法をお伝えします。

## 原因の解説

まず最初に、エラーの本質について理解しましょう。このエラーは、ComfyUIがStable Diffusionモデルの追加機能（特にLoRAsやembeddings）に対応していないことを示しています。LoRA（Low-Rank Adaptation）とは、既存の大規模な安定性のあるディフュージョンモデルに小さなアダプションを提供するテクニックで、特定のタスクに対してモデルを調整します。

Embeddingsは、学習済みの文脈埋め込みを使って画像生成を行う機能です。これらの技術を使用して高度なカスタマイズが可能になりますが、それらのサポートが必要な場合に、ComfyUIがまだ完全に対応していないためエラーが出ます。

## 解決ステップ (Step-by-Step)

では実際にどのように解決すれば良いのかを具体的にお伝えします。以下の手順で進めてください。

### Step 1: 特定のブランチを使用する

GitHubのリンクから、特定のバージョン（stable_cascade）を利用可能な最新のOneTrainerプロジェクトを入手しましょう。
```
git clone https://github.com/Nerogar/OneTrainer.git
cd OneTrainer
git checkout stable_cascade
```

### Step 2: 必要なファイルのインポート

次に、LoRAとembeddingのサポートが追加された最新の例をダウンロードして、プロジェクトの適切なディレクトリに格納します。
```
wget https://github.com/comfyanonymous/ComfyUI/files/14350805/examples.zip
unzip examples.zip
cd examples
mv lora_example.pt embedding_example.pt /path/to/your/project/directory/
```

### Step 3: ComfyUIの設定変更

ComfyUIを最新版にアップデートし、新たに導入された機能を使用できるように設定ファイルを調整します。具体的な手順は以下の通りです。
```
cd /path/to/comfyui
git pull origin main
# ディレクトリ内のコンフィギュレーションファイルを確認し、必要に応じて更新する。
nano config.yaml
```

### Step 4: 実際にモデルを使用する

準備ができたら、実際にComfyUIで生成を行います。これによりエラーが解消されていることを確認できます。

## まとめ

初心者のあなたでも、手順を踏んでいけば「Support for Stable Cascade LoRAs and embeddings」のエラーも解決可能です。ただし、技術的な詳細や新しいツールを使う際には不安を感じるかもしれませんが、その度に学びを得ることができます。これはクリエイティブな旅の一部であり、それが新しい世界を開くキッカケとなるでしょう。

もし何か不明瞭な点があれば、ComfyUIのコミュニティーや公式サポートまでお気軽にお問い合わせください。あなたがクリエイティブな表現を続けることを応援しています！
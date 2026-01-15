---
title: "【CivitAI】torch 2.9 incompatible with Pascal architectures の完全解決ガイド"
description: "ComfyUIのエラー 'torch 2.9 incompatible with Pascal architectures' の原因と、初心者でもできる修正手順をステップバイステプで解説します。"
pubDate: "2026-01-14"
---

## 【CivitAI】torch 2.9 incompatible with Pascal architectures の完全解決ガイド

### はじめに
最近ComfyUIを使ってみようとして、画面が真っ白になったり、 Flux Schnellを動かそうとするとエラーが出たりして困ったことはありませんか？この記事では、「torch 2.9 incompatible with Pascal architectures」というエラーに対処する方法をステップバイステップで詳しく説明します。初心者でも安心して取り組めるように、丁寧に解説しますので、ぜひ最後まで読んでみてください！

### 前提条件
このガイドは **Windows** と **Python環境** を前提としています。

- **ComfyUI Desktop**: お使いのパソコンにインストールされている必要があります。
- **CUDA Toolkit 12.8**: もともとインストールされていることを確認してください。ない場合は、公式サイトからインストールしておいてください。

### 原因の解説
このエラーは、新しいバージョンのPyTorch（例えば`torch 2.9+cu128`）が、旧世代のGPU（GTX 1070などパシフィックアーキテクチャを持つもの）と互換性がない場合に出ます。技術用語で言えば、「ComfyUIやその他のカスタムノードを動かすために必要なPyTorchのバージョンが、あなたのGPUのサポート範囲を超えていたり、非対応だったりする」ということです。

### 解決ステップ (Step-by-Step)

#### Step 1: インストールされているPyTorchとCUDAのバージョンを確認
まず、現在インストールされているPyTorchおよびCUDAのバージョンを確認します。ターミナルまたはコマンドプロンプトを開き、以下のコマンドを実行してください。

```bash
pip show torch torchvision torchaudio
```

結果から、`torch` のバージョンが `2.9+cu128` であることを確認してください。また、CUDAのインストールディレクトリを確認して、CUDA Toolkit 12.8が利用可能であることもチェックします。

#### Step 2: PyTorchと関連パッケージを再インストール
エラーが出ている場合、以下のコマンドを実行してPyTorchやその他の必要なモジュールを再インストールしてください。既存のバージョンを削除し、古いバージョン（`2.8.0+cu128`）に戻すのが目的です。

```bash
pip uninstall torch torchvision torchaudio -y
pip install torch==2.8.0+cu128 torchvision==0.14.0+cu128 torchaudio===2.0.2 --index-url https://download.pytorch.org/whl/cu128
```

これらのコマンドを実行すると、PyTorchとその他のモジュールが既存のものから削除され、CUDA 12.8に対応した古いバージョンがインストールされます。

### よくある質問 (FAQ)
- **Q: PyCharmやAnacondaで操作する場合、どうすればいいですか？**
  - A: 実際のPythonインタプリタを確認し、それに合わせて上記手順を実行してください。仮想環境（venv）を使っている場合は、その仮想環境内でコマンドを実行します。

### まとめ
このエラーが起きた場合、必ずしも古いハードウェアを持っているからといって諦める必要はありません。「torch 2.9 incompatible with Pascal architectures」は、単純なインストール設定の問題であり、手順通りに従えば確実に対処できます。ComfyUIや他のソフトウェアを使い続けるために、ぜひこのガイドを参考にしてみてください！

あきらめないで！解決できるはずです。
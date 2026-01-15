---
title: "【CivitAI】Extremely slow image generation with Flux model on MacOS Apple M4 Pro の完全解決ガイド"
description: "ComfyUIのエラー 'Extremely slow image generation with Flux model on MacOS Apple M4 Pro' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

## はじめに

こんにちは！ComfyUIを使って画像生成をしている際に、「Fluxモデルを使用すると非常に時間がかかる」という問題を抱えている方へ。この記事では、その原因と簡単な解決策について解説します。Pythonやプログラミングの知識がなくても大丈夫です。一緒に頑張りましょう！

## 原因の解説

あなたが使っているMacOS上のApple M4 Proは、新しいCPUで計算を高速に行うことができますが、CUDAという技術を使ってGPUを有効にするとパフォーマンスが向上します。

Fluxモデルは非常に複雑なため、計算量が多くなります。また、特定のバージョンのtorch（Pythonで使われるライブラリ）では、Apple M1/M2チップ上でCUDAによる高速化がうまくいかないことがあります。そのため、Fluxモデルを生成する際には時間がかかるという現象が起こります。

## 解決ステップ (Step-by-Step)

### ステップ1: CUDAのインストール

1. 開始前に、Terminalを開いて以下のコマンドを実行してCUDAがインストールされているか確認します。
   ```bash
   nvcc --version
   ```
   これが表示されない場合は、次の手順に進みます。

2. [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)のサイトから最新版をダウンロードしインストールします。Apple M4 Proのシステム要件を満たすものを選びましょう。
   - ダウンロード後、`.dmg`ファイルを開き、CUDA Toolkitをインストールします。

### ステップ2: PyTorchにCUDA対応版をインストール

1. 既存のPython環境で次のコマンドを使ってCUDAに対応したPyTorchをインストールまたは更新します。
   ```bash
   pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
   ```
   このコマンドは、CUDA 11.3版のPyTorchライブラリを使用します。これにより、GPUが計算を高速に行うことができます。

2. インストール後に再度、ComfyUIを起動し、Fluxモデルを使用して画像生成を試みてください。

### ステップ3: 確認と調整

1. CUDAが適切にインストールされ、PyTorchのCUDA版もインストールされていることを確認します。
   ```bash
   python -c "import torch; print(torch.cuda.is_available())"
   ```
   このコマンドにより「True」が出力されるはずです。

2. ComfyUIで画像生成を再度試みてください。生成時間は改善されたでしょうか？

## まとめ

ComfyUIを使ってFluxモデルの画像生成が非常に時間がかかる問題を解決するには、CUDAとPyTorchのCUDA対応版を使用することが有効です。これらの手順により、パフォーマンス向上が期待できます。

解決までに時間がかかったり、何か不具合があった場合は、ComfyUIのサポートコミュニティやGitHub Issuesに問題を報告してみてください。助けを求めることは全く問題ありません。一緒に頑張りましょう！

以上、ComfyUIを使って画像生成をする上で役立つ情報を提供しました。どういった状況でも諦めずに、少しずつ進んでいきましょう。
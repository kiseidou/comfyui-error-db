---
title: "【HuggingFace】AssertionError: Torch not compiled with CUDA enabled の完全解決ガイド"
description: "ComfyUIのエラー 'AssertionError: Torch not compiled with CUDA enabled' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"
---

### 【本文構成】

#### はじめに
こんにちは！ComfyUIを使っていて、「AssertionError: Torch not compiled with CUDA enabled」エラーが出てしまった、という経験はありませんか？この記事では、このエラーの原因と対処法を初心者の方でもわかるように解説します。これで直ります！

#### 前提条件
このガイドは主に Windows 環境での Python の仮想環境 (`venv`) を前提としています。

#### エラーの原因の解説
ComfyUIを更新したり、新しいCustom Node（拡張機能）をインストールした後に発生する可能性があるエラーメッセージです。「AssertionError: Torch not compiled with CUDA enabled」というメッセージは、「PyTorch」ライブラリがCUDA（並列処理ハードウェア）と統合されていないことを示しています。これは、プログラムがGPUを必要とする機能を使おうとしているときに発生します。

#### 解決ステップ (Step-by-Step)
1. **現在のPyTorchバージョンを確認する**
    ターミナルまたはコマンドプロンプトを開き、以下のように `pip show torch` コマンドを実行して、インストールされている PyTorch のバージョンを確認します。
    ```bash
    pip show torch
    ```
    このコマンドによって表示される情報から、「CUDA version」や「Build date」といった項目に注意してください。これらの情報が期待通りであれば、次のステップへ進みましょう。

2. **PyTorchの再インストール（CUDA版）**
    以下のコマンドを実行して、CUDAに対応した PyTorch を再インストールします。
    ```bash
    pip uninstall torch -y
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
    ```
    ここで使用されている`cu117`は、CUDAのバージョンを指定しています。もし自分のシステムが異なるバージョンのCUDAを使用している場合は、適切なバージョンのURLに変更してください（例えば、`cu113`など）。

#### よくある質問 (FAQ)
- **Q: なぜ `pip uninstall` を使うのですか？**
    A: 現在インストールされている PyTorch のインスタンスを削除してから再インストールすることで、古い設定や問題のあるインスタンスが残らないようにします。

#### まとめ
このエラーは簡単に解決できます。自分自身を信じて、手順に従って進んでください。「あきらめないで！これで直ります！」
---
title: "【UnityML】Torch not being compiled with CUDA enabled の完全解決ガイド"
description: "ComfyUIのエラー 'Torch not being compiled with CUDA enabled' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

# 【完全解決】ComfyUIで「Torch not being compiled with CUDA enabled」エラーが出た時の対処法

## はじめに
ComfyUIを使っていて、「Torch not being compiled with CUDA enabled」というエラーメッセージが出て、何をしたらいいのかわからない…そんな経験はありませんか？この記事では、このエラーの原因と、初心者でも簡単に解決できる手順をお伝えします。これでComfyUIを再開できますよ！

## 前提条件
- **オペレーティングシステム**: Windowsを使用しています。
- **Python環境**: Python 3.11.9をインストール済みです。

## 原因の解説
このエラーは、Torch（PyTorchという深層学習フレームワーク）がCUDAをサポートしていない場合に発生します。CUDAとは、GPUを使用するための技術で、AIや画像処理などの計算を高速化します。

なぜこれが起きるかというと、Python環境がCUDAに対応したバージョンのTorchをインストールしていない可能性が高いです。CUDAをサポートしていない状態では、ComfyUIがGPUの能力を使って作業しようとするとき、エラーが出てしまうのです。

## 解決ステップ (Step-by-Step)

### Step 1: PythonとTorchの環境を確認する
まず最初に、Pythonのバージョンとインストールされているパッケージを確認しましょう。これにより、現在の状態がどのようになっているか把握できます。

```bash
python --version
pip show torch
```

このコマンドで、`torch`パッケージがCUDAに対応しているかどうか確認します。対応していない場合、次に進みます。

### Step 2: CUDAをサポートしたTorchをインストールする

CUDAをサポートしたバージョンのPyTorchをインストールします。以下は具体的な手順です。

1. [PyTorch公式サイト](https://pytorch.org/get-started/locally/)から最新版のPython Wheelファイル（pipでインストール可能なパッケージ）をダウンロードする。
2. 以下のコマンドを使用して、CUDA対応版のPyTorchをインストールします。

```bash
pip uninstall torch -y   # 現在インストールされているtorchを削除
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu120  # CUDAに対応したバージョンのPyTorchをインストール。cuda120はCUDAのバージョンに合わせて変更してください。
```

`cu120`は具体的なCUDAバージョンに対応して、必要であれば `cu117`, `cu118` 等に変更します。

### Step 3: ComfyUIを再起動する
Torchが正しくインストールされたら、ComfyUIを再び起動してみてください。
```bash
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build
```

これでエラーは解消されるはずです。もしもまだエラーが出る場合は、Python環境全体のクリーンアップ（venv の削除と再インストール）を検討してみてください。

## よくある質問 (FAQ)

**Q: PyTorch以外のCUDA対応パッケージもインストールする必要がある？**
A: たいていの場合、PyTorchだけインストールすれば問題ありませんが、必要な他のライブラリ（torchvision, torchaudioなど）も同様にCUDAに対応したバージョンをインストールしてみてください。

**Q: CUDA対応のバージョンがわからなかったら？**
A: その場合、公式サイトで自分のGPUとPythonバージョンに最適なパッケージを選べるように案内があります。CUDAのバージョンは、NVIDIA Developerページで確認できます。

## まとめ
今回のエラー解決を機会に、Python環境やCUDAについて詳しくなるのもいいですね！これでまた一つスキルアップしたことになりますよ。あきらめずに取り組んでみてください！

---

この記事があなたの問題解決にお役立てば幸いです。頑張ってください！
---
title: "【Python】CUDA error : invalid argument の完全解決ガイド"
description: "ComfyUIのエラー 'CUDA error : invalid argument' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"
---

## はじめに

こんにちは！ComfyUIを使っていて「CUDA error : invalid argument」エラーが出たことがある方、多いですよね？この記事では、そのエラーを手軽に解決する方法を詳しく解説します。Pythonやプログラミングが苦手なクリエイターさんでも安心して読み進めることができますよ！

## 前提条件

- この記事は **Windows** や Python環境 を想定しています。
- 仮想環境（venv）の利用推奨。

## 問題の原因について

ComfyUIで「CUDA error : invalid argument」が出る主な理由は、CUDAが使用するGPUメモリに問題がある場合や、Pythonスクリプト内でCUDAライブラリを使用しているNode (Custom Node) が適切に設定されていないことが考えられます。 

このエラーは特定のワークフロー（例えばqwen-image-2509 + Lightning 8stp 1.1 + LoRA）を複数回実行する際に発生し、原因は大抵はPythonスクリプト内でGPUメモリが適切に解放されていない場合が多いです。特にGPUがRTX 4070 Superのような中級的な性能のものであると、メモリ管理には注意が必要です。

## 解決ステップ (Step-by-Step)

### Step 1: ワークフローを再起動する

まず最初に、問題の発生しているワークフロー全体を一度止めてから再開してください。これはメモリが適切な状態で解放されていることを確認するためです。

### Step 2: Pythonスクリプト内で適切なメモリ管理を行うコマンドを実行する

問題の発生しているワークフローで使用されているPythonスクリプトを見直し、各セクションの最後に`torch.cuda.empty_cache()`と記述します。これはCUDAカーネルが使ったRAMやVRAM（GPUメモリ）を解放するコマンドです。

```python
import torch

# ワークフローの処理部分
...

# 各セクションの終わりに以下を追加する
torch.cuda.empty_cache()
```

### Step 3: 環境変数CUDA_LAUNCH_BLOCKING=1で実行する

デバッグのために環境変数 `CUDA_LAUNCH_BLOCKING` を設定して、CUDAエラーが発生した際に即座に停止し、その時点でのスタックトレースを確認します。これにより、具体的な問題箇所の特定が容易になります。

```cmd
set CUDA_LAUNCH_BLOCKING=1 && comfyui.exe
```

### Step 4: カスタムノードの再インストール

カスタムノード (Custom Node) の設定に問題がある場合があります。以下のように、まずはカスタムノードを一度全て削除し、再度インストールします。

```cmd
# 仮想環境を有効化する
.\venv\Scripts\activate

# カスタムノードのアンインストール
pip uninstall comfyui-custom-nodes

# カスタムノードの再インストール
pip install comfyui-custom-nodes
```

## FAQ (よくある質問)

- **Q: 他のGPUでも同じエラーが出る？**
  - A: メモリ管理が問題であれば、他のGPUでも同様に発生します。必ず`torch.cuda.empty_cache()`の使用を確認してください。

- **Q: エラーが解決しない場合？**
  - A: 原因が特定できない場合は、スタックトレースやログファイルを共有して詳細な情報を得ましょう。また、ComfyUIの公式フォーラムでの質問も有効です。

## まとめ

CUDA error : invalid argument は直すことができます！手順を踏んで一つずつ確認しながら進めると良いでしょう。もし解決できない場合は、コミュニティやサポートに頼ってみましょう。あきらめずに挑戦すれば必ず解決します！

これでComfyUIのエラー対処が一歩前進ですね！
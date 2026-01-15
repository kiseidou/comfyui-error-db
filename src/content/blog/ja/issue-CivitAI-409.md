---
title: "【CivitAI】Basic support for Intel XPU (Arc Graphics) の完全解決ガイド"
description: "ComfyUIのエラー 'Basic support for Intel XPU (Arc Graphics)' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"
---

## はじめに

こんにちは！ComfyUIを使っていて「Basic support for Intel XPU (Arc Graphics)」というエラーが出てしまった方、大丈夫です。この記事を読めば、初心者でも安心して問題解決することができます。一緒に頑張りましょう！

## 前提条件

- 操作対象のOS: Windows / Linux
- 必要なソフトウェア環境: PythonとComfyUI（Custom Node[拡張機能]）

この記事ではWindowsやLinuxのPython環境での操作を想定しています。

## 理解する：なぜエラーが出るのか？

「Basic support for Intel XPU (Arc Graphics)」というエラーは、Intel Arc GPUが完全にサポートされていない状況で発生します。これは通常、必要なライブラリやツールキットがインストールされていないことが原因です。この記事では、その解決方法を詳しく説明します。

## 解決ステップ (Step-by-Step)

### Step 1: 必要なツールキットをインストールする

Intelの公式ページから[oneAPI Base Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html)と[AURの`intel-compute-runtime-bin`](https://aur.archlinux.org/packages/intel-compute-runtime-bin/)をインストールします。Linuxの場合、具体的なコマンドは以下の通りです。

- Arch Linux:
  ```bash
  paru -S intel-oneapi-basekit intel-compute-runtime-bin
  ```

### Step 2: Pythonの依存関係を設定する

ツールキットがインストールされたら、Pythonで必要なライブラリをインストールします。この段階では、仮想環境（venv）を使うとよりスムーズです。

1. テーツクセットに移動し、次のコマンドを実行して依存関係をインストールします。
   ```bash
   pip install torch==1.13.0a0 torchvision==0.14.1a0 intel_extension_for_pytorch==1.13.10+xpu -f https://developer.intel.com/ipex-whl-stable-xpu
   ```
2. 環境変数を設定します。
   ```bash
   source /opt/intel/oneapi/setvars.sh
   ```
3. さらに必要な依存関係をインストールするには、以下のコマンドを使用します。
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: プログラムの実行

すべてのライブラリが適切にインストールされ、環境設定が完了したら、以下のようにプログラムを実行できます。

```bash
python main.py --use-split-cross-attention
```
このオプションを使用することで、ノイズが生成される可能性が低減します。


## よくある質問 (FAQ)

### Q: 実際にXPUが使用されていることを確認する方法は？

Pythonのインタープリターで以下のコマンドを実行してみてください。

```python
import torch
print(torch.xpu.is_available())
```

もし`True`が出力されたら、XPUが正しく設定されています。さらに詳細な情報が必要な場合は以下のようなコードも試すと良いでしょう。
```python
torch.xpu.get_device_properties('xpu')
```
これで具体的なデバイス名やメモリなどの情報を得られます。

## まとめ

この記事では、「Basic support for Intel XPU (Arc Graphics)」のエラーを完全に解決するための手順を詳しく説明しました。難しいかもしれませんが、一つずつ進めていけば必ず解決できるはずです！あきらめずにチャレンジしてみてくださいね。

もし何か不明な点があればコメント欄やサポートコミュニティで質問してください。あなたも問題解決のプロになれるよう、応援しています！
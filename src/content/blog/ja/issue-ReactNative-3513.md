---
title: "【ReactNative】undefined symbol: iJIT_NotifyEvent の完全解決ガイド"
description: "ComfyUIのエラー 'undefined symbol: iJIT_NotifyEvent' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"
---

## はじめに

ComfyUIを使って創作活動をしているあなた、「undefined symbol: iJIT_NotifyEvent」なんて謎めいたエラーが出て、一体何をしたらいいのかわからなくなってしまった経験はありませんか？これでプロジェクトの進行が止まってしまうのは本当に困りますよね。でも大丈夫！この記事では初心者でもできる修正手順をお伝えしますので、一緒に解決していきましょう！

## 前提条件

この記事は、WindowsやPython環境を使用している方を対象としています。また、仮想環境（venv）を使っていることが前提となります。

### 必要なツール
- Python (3.10 推奨)
- 仮想環境管理ツール (venv)
- ComfyUI

## 原因の解説

このエラーは、PyTorchやIntel Extension for PyTorch（以下、IPEXと略）がインストールされている際に発生しやすいです。具体的には、PyTorchの特定バージョンとIPEXのバージョン間で非互換性がある場合に起きる可能性があります。

Pythonの依存関係管理ツール `pip` は、通常は最新バージョンのライブラリをインストールしようとしますが、これは必ずしもすべての環境で動作するとは限らないことがあります。特にこのエラーの場合、PyTorchとIPEXの両方を使用している場合に、バージョンの整合性が欠けていることが原因です。

## 解決ステップ (Step-by-Step)

### Step 1: PyTorchとIntel Extension for PyTorchのバージョンを確認する

まず、現在インストールされているPyTorchとIPEXのバージョンをチェックしましょう。以下のコマンドでそれぞれのバージョン情報を取得できます。

```bash
pip show torch
pip show intel-extension-for-pytorch
```

### Step 2: PyTorchとIntel Extension for PyTorchを互換性のあるバージョンに更新する

PyTorchの安定版（1.9.xや1.10.xなど）とIPEXの互換性がある特定のバージョンをインストールしましょう。以下は、代表的な対応表ですが、最新情報を公式ドキュメントで確認することをお勧めします。

```bash
pip install torch==1.9.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
pip uninstall intel-extension-for-pytorch
pip install intel-extension-for-pytorch==1.9.0
```

### Step 3: ComfyUIを起動し、正常に動作することを確認する

上記の手順を完了したら、ComfyUIを再度起動して、エラーが解消したことを確認してください。

```bash
ipexrun main.py --use-pytorch-cross-attention --highvram
```

## よくある質問 (FAQ)

### Q: PyTorchとIPEXのバージョンが一致しても解決しない場合は？

PyTorchやIPEX自体に問題がある可能性があります。その際は、最新版をインストールするか、あるいはサポートコミュニティに相談してみてください。

### Q: 仮想環境の作り直しを行うべきですか？

場合によっては、仮想環境全体を削除し、再度作成することで一から依存関係を整える方法もあります。ただし、これは最終手段として考えてください。

## まとめ

「undefined symbol: iJIT_NotifyEvent」というエラーで困っているあなたへ。「これでもダメなら諦めるしかない…」なんて思わないでください！ステップバイステップで進めれば、誰でも簡単に解決できますよ。試行錯誤しながら進むことが大事です。あきらめずにチャレンジし続けてくださいね！

あなたの創作活動がスムーズに進行することを心から願っています！
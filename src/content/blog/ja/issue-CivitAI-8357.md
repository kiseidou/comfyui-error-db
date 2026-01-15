---
title: "【CivitAI】add support to read pyproject.toml from custom node の完全解決ガイド"
description: "ComfyUIのエラー 'add support to read pyproject.toml from custom node' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

## はじめに

こんにちは！ComfyUIを使っていて「add support to read pyproject.toml from custom node」エラーが出たと困っている方へ。この記事では、初心者の方でも安心して解決できるように、詳しく手順を解説します。

まず最初に、「pyproject.toml」というファイルが何なのか簡単に説明しましょう。「pyproject.toml」はPythonのプロジェクト設定ファイルで、`Custom Node（拡張機能）`開発時に重要な情報が含まれています。この記事ではこれを解決するための方法をご紹介します。

## 前提条件

- ComfyUIを使っている
- Python環境がセットアップされている
- Windowsか他のOSでも問題ありません

## なぜエラーが出るのか？

このエラーは、ComfyUIが特定のカスタムノードで`pyproject.toml`ファイルを読み込む能力がない場合に出ます。具体的には、開発者用のパッケージ（comfy-cli）とコア間での定義が同期されていないことが原因です。

## 解決ステップ (Step-by-Step)

### Step 1: エラー内容を確認する

エラーメッセージが表示されたら、その内容をよく見てください。特に「pyproject.toml」と関連があるメッセージを探します。

### Step 2: 必要なパッケージをインストールする
`tomlkit`というPythonパッケージが必要です。このパッケージは、`pyproject.toml`ファイルの読み込みに使われます。

以下のコマンドでインストールします：
```
pip install tomlkit
```

### Step 3: コード修正と同期

次に、ComfyUIのソースコードを修正して、カスタムノードでのpyproject.tomlの処理に対応する必要が出てきます。具体的には以下のような手順です。

1. ComfyUIの`comfy-cli`プロジェクト内の定義を確認します。
2. その定義をComfyUIコアにもコピーして同期させます（詳細な操作は開発者向けのドキュメントを参照してください）。

### Step 4: テスト環境で動作確認

修正が完了したら、テスト環境で動作確認を行ってください。エラーが出なくなったことを確認します。

## よくある質問 (FAQ)

**Q: この問題は他のOSでも起こりますか？**
A: はい、WindowsだけでなくLinuxやmacOSでも同様のエラーが発生する可能性があります。それぞれのOSでインストール方法に少し違いがあるかもしれませんが、基本的な解決策は同じです。

## まとめ

「add support to read pyproject.toml from custom node」エラーを修正するために必要な手順を紹介しました。Python初心者の方でも、コマンドライン上で簡単に実行できるようになっていますので、諦めずにチャレンジしてみてください！
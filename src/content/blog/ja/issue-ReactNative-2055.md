---
title: "【ReactNative】ImportError: cannot import name 'get_full_repo_name' from 'huggingface_hub' の完全解決ガイド"
description: "ComfyUIのエラー 'ImportError: cannot import name 'get_full_repo_name' from 'huggingface_hub'' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"
---

## はじめに

ComfyUIを使っていて、「ImportError: cannot import name 'get_full_repo_name' from 'huggingface_hub'」というエラーが出てしまい、困っている方へ向けた記事です。このエラーメッセージを解決するための完全ガイドをご提供します。

## 前提条件

この解説は Windows と Python 環境を想定しています。また、Python の仮想環境（venv）を使用していることが望ましいです。

## 原因の解説

`ImportError: cannot import name 'get_full_repo_name' from 'huggingface_hub'` というエラーは、huggingface_hub パッケージがインストールされているものの、その内部で特定の名前（ここでは `get_full_repo_name`）を参照しようとした際に問題が発生したことを示します。このエラーは通常、huggingface_hub のバージョンと相性が悪いために起こります。

具体的には、huggingface_hub パッケージの最新版では `get_full_repo_name` という関数名を使用しているかもしれませんが、古いバージョンでは存在しない（または異なる場所にある）可能性があります。そのため、このエラーを解決するには、huggingface_hub のバージョンを更新したり、適切なバージョンを選択することが必要です。

## 解決ステップ (Step-by-Step)

### Step 1: pip バージョンの確認と更新

まずは、pip（Python のパッケージ管理ツール）が最新版であることを確認します。コマンドプロンプトや PowerShell で以下のコマンドを実行してください。

```bash
python -m pip install --upgrade pip
```

### Step 2: huggingface_hub パッケージの再インストール

次に、huggingface_hub パッケージを最新版に更新します。以下のように pip を使用して再度インストールを行ってください。

```bash
pip uninstall huggingface_hub
pip install huggingface_hub
```

この手順により、問題のあるバージョンのパッケージが削除され、最新の安定バージョンがインストールされます。

### Step 3: ComfyUI の依存関係を再構築

最後に、ComfyUI の依存関係を再構築することで、全体的な相性問題に対応します。以下のコマンドを実行してください：

```bash
pip install -r requirements.txt
```

ここで `requirements.txt` は ComfyUI のプロジェクトディレクトリ内にあるファイルです。

## よくある質問 (FAQ)

### Q: この手順で解決しない場合、どうすればいいですか？

A: それでも問題が残る場合は、Python の仮想環境を完全に削除して再作成するか、もしくは ComfyUI の新しいバージョンのインストールを試みてください。

### Q: huggingface_hub パッケージのどのバージョンが必要ですか？

A: `get_full_repo_name` を使用している最新版をインストールするのが望ましいです。通常、pip は常に最新の安定版をインストールしますが、特定のバージョンを指定したい場合は `-r requirements.txt` の代わりに、具体的なバージョン番号を使用してインストールできます。

## まとめ

このエラーは、huggingface_hub パッケージのバージョン問題から生じることが多いです。しかし、きちんと pip を更新し、必要なパッケージを最新版にアップデートすれば解決できることが多いです。あきらめずに試してみてください！

頑張って続けていくと、必ず成果がでますよ！
---
title: "【ComfyUI】Replace chainner_models with Spandrel package の完全解決ガイド"
description: "ComfyUIのエラー 'Replace chainner_models with Spandrel package' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

# 【ComfyUI】Replace chainner_models with Spandrel package の完全解決ガイド

## はじめに
こんにちは！ComfyUIを使っているものの、Pythonやプログラミングについて詳しくないクリエイターさんの中には、「Replace chainner_models with Spandrel package」というエラーに出くわして困った経験があるかもしれません。この記事では、そのようなエラーを手取り足りて解決する方法をお伝えします。

## 前提条件
- このガイドは **Windows** または **Python環境** を前提としています。
- ComfyUIとPythonの基本的な使い方について理解していることが望ましいです。

## 原因の解説
このエラーは、ComfyUIが以前使用していた `chainner_models` フォルダを新しいパッケージの **Spandrel** に置き換えるための変更で生じています。SpandrelはchaiNNerのモデル読み込みコードを独立したパッケージ化したもので、新しいモデルタイプに対するサポートも提供します。

しかし、この変更がまだ完全には完了していない可能性があります。そのため、ComfyUIのセットアップに最新版のSpandrelパッケージが必要になる場合、適切な設定がされていないためにエラーが発生するのです。

## 解決ステップ (Step-by-Step)

### Step 1: Spandrelパッケージをインストールする
まず、コマンドプロンプトまたはターミナルを開き、以下のコマンドを実行してSpandrelパッケージをインストールしてください。

```bash
pip install spandrel
```

### Step 2: ComfyUIの設定ファイルを確認する
次に、ComfyUIの設定ファイル（`config.yaml`など）を開き、以下の通り `chainner_models` の指定が存在しないかチェックしてください。もしあればそれを削除します。

また、必要であれば、新たに **Spandrelパッケージ** を利用できるように設定を追加します。具体的な箇所はComfyUIのドキュメンテーションやサポートコミュニティで確認してみてください。

### Step 3: モジュールが最新かどうか確認する
場合によっては、Pythonのモジュール自体が古いままになっていることがあります。その場合は、以下のコマンドを使ってComfyUIとSpandrelパッケージをアップデートします。

```bash
pip install --upgrade comfyui spandrel
```

## よくある質問 (FAQ)

### Q: ComfyUIの設定ファイルが見つからないのですが？
A: 通常、ComfyUIのインストール先フォルダ内に配置されています。具体的な場所はインストール時のログやドキュメンテーションを参照してください。

### Q: インストール後もエラーが出るのですが？
A: ComfyUIとSpandrelパッケージの互換性がまだ完全ではない可能性があります。その場合、最新のベータ版またはアプデート版を利用するとよいでしょう。ComfyUIの公式ウェブサイトやDiscordサーバーで最新情報を確認してください。

## まとめ
エラーが出てもあきらめないでください！今回のステップを踏んで問題が解決した方々からのフィードバックがあれば、この記事をさらに改善することができます。ぜひ、あなたの成功体験もお聞かせくださいね！

これで直ります！頑張ってみてください。
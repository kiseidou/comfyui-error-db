---
title: "【ComfyUI】TypeError: forward_orig() got an unexpected keyword argument 'attn_mask' の完全解決ガイド"
description: "Error fix guide for TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'"
pubDate: "2026-01-15"
---

### 本文

この記事では、ComfyUIの更新後に発生した「TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'」エラーについて、初心者にもわかりやすく原因と解決方法を解説します。

#### エラーメッセージ
```
TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'
```

このエラーはComfyUIのノード「SamplerCustomAdvanced」を使用する際に発生することが多いです。主に、モデルやライブラリの更新と関連があります。

#### 原因
- ComfyUIまたは使用しているモデルが最新版でない場合。
- 特定のパッチにより、'attn_mask'引数が不要になったり、異なる形式となった可能性がある。

#### 解決方法

##### 1. ComfyUIを最新版に更新する
ComfyUIのインストールディレクトリへ移動し、以下コマンドで最新バージョンへの更新を行います。
```bash
pip install --upgrade ComfyUI
```

##### 2. 必要なライブラリのアップデートと再インストール
更新時に依存関係が変わった場合がありますので、以下のコマンドを用いて必要なら必要なパッケージをアップデートします。
```bash
pip install --upgrade torch transformers diffusers
```
これらのコマンドはPythonから入る可能性がある他のライブラリを最新版に更新します。

##### 3. モデルの再ダウンロード
一部のモデルが変更され、既存のインストールと互換性がなくなった可能性があります。この場合、最新版のモデルを再度ダウンロードしてみてください。
```bash
git clone <model_repository_url>
```
その後、ComfyUI上で新しいモデルを使用できるように設定してください。

##### 4. セッションクリア（オプション）
古いセッションデータが影響している可能性もありますので、以下のコマンドでセッションをクリアしてみてください。
```bash
python -m comfyui.clean_sessions
```

これらの手順を行ってもエラーが解決しない場合は、ComfyUIのGitHubリポジトリにあるIssuesページやDiscordコミュニティを利用して、詳しい情報を提供しつつ支援を求めると良いでしょう。

以上で「TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'」エラーを完全に解決するためのガイドが終了です。うまくいったかどうかお知らせください。
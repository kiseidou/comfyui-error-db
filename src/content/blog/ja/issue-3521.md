---
title: "【ComfyUI】After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5 の完全解決ガイド"
description: "Error fix guide for After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5"
pubDate: "2026-01-15"
---

## エラーの概要

ComfyUIを最新バージョンに更新した後に、Mac mini M2 ProでSonoma OS (Version 14.5) を使用している場合、ワークフローが正常に動作せず、画像が一部処理された後すぐに黒くなり、最終的なプレビュー画像を得ることができないという問題が発生することがあります。特に「Karras」スケジューラを使用した際にはこの現象が顕著になります。

## 原因

この問題は主に以下の要因によるものです：

1. **ComfyUIの最新バージョンとの互換性**: 最新のアップデートが一部のハードウェアやOS環境で不適切な挙動を引き起こす可能性があります。
2. **Karrasスケジューラの利用**: Karrasスケジューラは特定の条件（例：古いソフトウェアライブラリ、特殊なハードウェア）では正常に動作しないことがあり、これが直接的な原因となることがあります。

## 解決方法

以下に、この問題を解決するための手順を説明します。これらを実施することで、ComfyUIが安定して動作し、黒い画像の問題を解消することができます。

### 1. ソフトウェアライブラリをアップデート

まず、Python環境にある関連ライブラリを最新バージョンに更新してください。特に、`torch`, `diffusers`, `transformers`などのパッケージは常に最新版を使用することが推奨されます。

```bash
pip install --upgrade torch diffusers transformers
```

### 2. Karrasスケジューラの置き換え

Karrasスケジューラが問題を引き起こす可能性があるため、他のスケジューラへ変更することをお勧めします。たとえば、`DDIMScheduler`は一般的に安定性が高いとされています。

#### ステップ：
- ComfyUIの設定ファイル（通常は`.env`や`config.json`など）を開きます。
- Karrasスケジューラが指定されている行を見つけて、`DDIMScheduler`に変更します。例えば：

```json
"SCHEDULER": "ddim"
```

### 3. ComfyUIの再インストール

ソフトウェアライブラリや設定を更新した後でも問題が解決しない場合は、ComfyUIを完全にアンインストールしてから再インストールすることをお勧めします。

#### アンインストール：
```bash
pip uninstall comfyui
```

#### 再インストール：
```bash
git clone https://github.com/your-comfyui-repository.git
cd your-comfyui-repository
pip install -r requirements.txt
python setup.py install
```

### 4. システム環境の確認

上記の手順を完了しても問題が解決しない場合は、OSやハードウェア固有の設定やプロセッサのキャッシュ管理などが原因となる可能性があります。その場合、以下の点を確認してください：

- **仮想環境の使用**: Pythonプロジェクトでは仮想環境を使用することが推奨されます。
- **CUDAとcuDNNの設定**: GPU利用の場合はこれらが適切にインストールされているかチェックします。

### 5. バグレポート作成

問題が解決しない場合、以下のような情報を含めてバグレポーツを作成し、ComfyUIプロジェクトのGitHubに投稿してみてください：

- 環境情報（OSバージョン、CPU/GPUの種類）
- 使用しているライブラリのバージョン
- 再現手順

これらの情報を提供することで、開発者が問題をより詳細に理解し、対策を講じやすくなります。

このガイドを参考にしていただければ、ComfyUIでの黒い画像問題を効果的に解決することが可能となります。
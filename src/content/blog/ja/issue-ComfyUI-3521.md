---
title: "【ComfyUI】After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5 の完全解決ガイド"
description: "Error fix guide for After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5"
pubDate: "2026-01-15"
---

## エラーの概要

最近のアップデート後、Mac Mini M2 ProでSonoma 14.5を使用しているときにComfyUIを実行すると、画像が一部のステップを経てから黒くなる現象が発生します。多くのワークフローがこの問題により正常に機能しなくなります。

## 原因

調査の結果、「Karras」スケジューラーがこの問題を引き起こすことが判明しました。「Karras」スケジューラーは、画像生成過程で安定性と品質を向上させるために使用される方法ですが、特定の環境（特にMac Mini M2 ProとSonoma 14.5）では予期しない動作を引き起こします。

## 解決策

この問題を解決するには、以下の手順に従ってください：

### 手順1：「Karras」スケジューラーの使用を停止する
まず、「Karras」スケジューラーを使用しているワークフローを見つけてそれを非アクティブ化します。代わりに「DDIM」や「DPM++」のような他のスケジューラーを使用することで、この問題を避けることができます。

### 手順2：必要に応じてパッケージをアップデート
一部のユーザーが遭遇する別の原因は、依存関係のバージョン不整合です。必要なすべてのPythonライブラリが最新の状態であることを確認してください。

```
pip install --upgrade pip
pip install -r requirements.txt  # ComfyUIが必要とする全てのパッケージをインストールまたはアップデートします。
```

### 手順3：GPUとCUDAの設定をチェック
Mac Mini M2 Proは特に最新のハードウェアで、CUDA環境が正確にセットアップされていない場合に問題が発生することがあります。以下のコマンドを使用して、必要なCUDAライブラリがインストールされていることを確認します：

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```

ここで`cu117`は、Mac Mini M2 Proで適切なCUDAバージョンに該当するものです。必要であれば、PyTorchの公式サイトを参照して正確なバージョンを確認してください。

## ファイナライズ

以上の手順が完了したら、ComfyUIを再起動し、ワークフローが正常に動作することを確認してください。

このガイドにより、「Karras」スケジューラーを使用した場合の黒画面問題を効果的に解決できるはずです。
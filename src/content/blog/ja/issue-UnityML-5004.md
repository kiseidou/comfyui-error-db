---
title: "【UnityML】Error occurred when executing IPAdapterUnifiedLoader:  ClipVision model not found の完全解決ガイド"
description: "ComfyUIのエラー 'Error occurred when executing IPAdapterUnifiedLoader:  ClipVision model not found' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

## はじめに

こんにちは！ComfyUIを使っている時に「Error occurred when executing IPAdapterUnifiedLoader: ClipVision model not found」というエラーが出た場合の対処法をご紹介します。この記事では、Pythonやプログラミングが詳しくない方でも理解しやすいように説明します。

このエラーは、ComfyUIで特定のモデル（ClipVision）を見つけることができなかったときに発生します。その解決方法をステップバイステップでお伝えしますので、一緒に取り組んでいきましょう！

## 原因の解説

### エラーメッセージの意味
エラーの詳細な内容は以下の通りです：

```
Error occurred when executing IPAdapterUnifiedLoader:
ClipVision model not found.
```

このメッセージは、ComfyUIが「IPAdapterUnifiedLoader」機能を実行しようとした際に、「ClipVision」という名前のモデルファイルを見つけることができなかったことを示しています。

### ClipVisionとは？
ClipVisionは、画像とテキストの両方を処理できる大規模な画像認識モデルです。ComfyUIでは、このモデルを使用して画像生成や変換などの高度なタスクを行うことができます。

しかし、このモデルが存在しない場合（または場所が正しくない場合）にエラーが発生します。

## 解決ステップ (Step-by-Step)

### 1. モデルファイルの確認
まず最初に、ClipVisionのモデルファイルがあることを確認してください。以下の手順で行います：

#### 手順：
- ClipVisionモデルを格納しているディレクトリを開きます。
- ディレクトリ内に「clip-vision」または似たような名前のフォルダ（またはファイル）があるか確認します。

**参考：**
通常、モデルのファイルパスは以下のようになっています：

```
C:\Users\Owner\Desktop\ComfyUI_windows_portable\models\clip-vision
```

### 2. モデルの再インストール

もしモデルファイルが見つからない場合や不完全な状態だとしたら、以下のように再インストールを行います。

#### 手順：
1. ComfyUIを閉じます。
2. ClipVisionモデルに関連する全てのファイルとフォルダを削除します（バックアップは必ず取ってください）。
3. 実行可能な「ClipVision」のダウンロードリンクを見つけて、最新版をダウンロードします。

**参考：**
GitHubリポジトリや公式サイトから最新のモデルを入手できます。必要な情報は以下にまとめています：

- モデルのURL: [Model Download URL](https://github.com/username/repository/releases/download/v0.1/model-file.zip)
- ダウンロードしたファイルを適切な場所（例：`C:\Users\Owner\Desktop\ComfyUI_windows_portable\models\clip-vision`）に展開します。

### 3. ComfyUIの設定確認
次に、ComfyUI内のモデルパスが正しく設定されているか確認しましょう。

#### 手順：
1. ComfyUIを立ち上げます。
2. 「Settings」または「設定」から「Model Path」や「モデルパス」を探します。ここに正しいファイルパス（Step 2で展開したディレクトリの場所）が入っていることを確認してください。

### 4. テスト実行
最後に、エラーが出たタスクを再度試してみましょう。

#### 手順：
1. エラーメッセージが出た機能（例えば「IPAdapterUnifiedLoader」）を選択します。
2. 実行すると正常に動作するか確認してください。

## まとめ

このエラーは、モデルファイルが見つからないときに出ます。しかし、モデルを再インストールし、パスを適切に設定すれば解決できることが多いです。

もし試しても改善しない場合や不明な点があれば、ComfyUIのコミュニティーやサポートチームに質問してみてくださいね！

これからも頑張っていきましょう！挫折は誰にでもあります。うまくいかないときは一旦休憩を取ることも大切ですよ。
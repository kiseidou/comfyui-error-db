---
title: "【ComfyUI】**Exception Message:** TypeError: Cannot delete property 'value' of #<BooleanWidget2> ## Stack Trace の完全解決ガイド"
description: "ComfyUIのエラー '**Exception Message:** TypeError: Cannot delete property 'value' of #<BooleanWidget2> ## Stack Trace' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"
---

## はじめに

こんにちは！ComfyUIを使っているときに、「TypeError: Cannot delete property 'value' of #<BooleanWidget2>」というエラーが出たことはありませんか？この記事では、そのエラーを解決するための手順を詳しく解説します。プログラミングやPythonが苦手な人でも簡単に直せるように、段階を追って説明していきますので、一緒に解決しましょう！

## 前提条件

このガイドは、Windows環境とPythonで仮想環境（venv）を使用していることを前提としています。ComfyUIをインストールし、ワークフローを保存した状態でエラーが出ていることが必要です。

## 原因の解説

「TypeError: Cannot delete property 'value' of #<BooleanWidget2>」というエラーは、ComfyUIが特定のノード（Custom Node（拡張機能））をロードしようとしたときに発生します。具体的には、`comboBoolMigration.js`ファイル内で`BooleanWidget2`オブジェクトの値を削除しようとしている際に、その操作が許可されていないためエラーとなります。

この問題は主に、ComfyUIで保存されたワークフローに以前のバージョンとの互換性があるかどうかに関連しています。過去のバージョンでは、`BooleanWidget2`オブジェクトの値を削除できるようにコードが書かれていたかもしれませんが、新しいバージョンではそれが禁止されています。

## 解決ステップ (Step-by-Step)

### Step 1: ワークフローに問題のあるノードを特定する

エラーが発生したワークフローで使用されているCustom Node（拡張機能）を探します。通常、これらのノードはワークフローの上部や中央あたりに配置されています。

### Step 2: 原因となるCustom Nodeの修正または削除

次に、問題のあるCustom Nodeを削除または修正します。

#### **方法1：Custom Nodeを削除する**
- まず、ComfyUIのダッシュボードを開き、ワークフロー上でエラーを発生させているノードを選択します。
- 「Delete」（削除）ボタンをクリックし、問題のあるノードを取り除きます。

#### **方法2：Custom Nodeを修正する**
- 削除した場合でも機能が必要な場合は、「extensions/ComfyUI-Impact-Pack/comboBoolMigration.js」ファイルを開き、エラーが発生する部分のコード（通常は26行目付近）を見直します。
- このファイル内で`BooleanWidget2.set()`メソッドを使用している箇所があり、その行を修正または削除します。

### Step 3: 仮想環境を更新する

Custom Nodeが適切に動作するようになると、仮想環境（venv）も最新の状態にしておくことが重要です。以下のコマンドでインストールされているパッケージを確認し、必要であればアップデートします。

```bash
pip list
```

必要に応じて、以下のようなコマンドを使用して必要なパッケージを更新できます：

```bash
pip install --upgrade comfyui-impact-pack
```

### Step 4: ComfyUIを再起動する

最後に、ComfyUIを完全にシャットダウンし、再度起動します。これにより、修正が反映され、ワークフローが正常に読み込まれるはずです。

## よくある質問 (FAQ)

**Q: Custom Nodeとは？**
A: Custom Nodeは、ComfyUI内で特定のタスクや機能を実装するための拡張機能です。これは通常、`extensions`ディレクトリ内に配置され、独自のJavaScriptファイルで定義されます。

## まとめ

今回のエラー解決を通じて、どのようにして問題のあるノードを見つけて修正するか理解できたでしょうか？コードの理解やPythonの知識がなくても、ステップバイステップで進めることが可能です。あきらめずに取り組んでみてください！

これでComfyUIが正常に動作し、クリエイティブな活動を再開できるはずです！
---
title: "【CivitAI】headdim should be in [64, 96, 128]. の完全解決ガイド"
description: "ComfyUIのエラー 'headdim should be in [64, 96, 128].' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-14"
---

### 【CivitAI】headdim should be in [64, 96, 128]. の完全解決ガイド

#### はじめに
クリエイターのみなさん、こんなエラーが出て困っていませんか？

```
AssertionError: headdim should be in [64, 96, 128].
```

この記事では、ComfyUIで出やすい「headdim」関連のエラーを完全に解決する方法を初心者向けに紹介します。エラーを直すためには、Pythonの知識は必要ありません。ぜひお読みください！

#### 前提条件
- このガイドはWindows 10以上やPython環境で動作することを想定しています。
- ComfyUIがインストールされていること。

#### 原因の解説
「headdim should be in [64, 96, 128].」というエラーは、ComfyUIのKSamplerノードを使用する際に発生します。このエラーは通常、「Custom Node（拡張機能）」が適切な設定になっていない場合やインストールしたPythonライブラリに問題がある場合に出ます。

具体的には、`headdim`と呼ばれるパラメータの値が64, 96, 128以外の数値になっているときに発生します。これらの値はモデルの設定によって決まっており、不適切な値を設定すると上記のようなエラーが出力されます。

#### 解決ステップ (Step-by-Step)

##### Step 1: エラーログから情報を取得する
まず、エラーが発生したファイル名と行数から、エラーの発生箇所を探します。例えば、

```
File "D:\Comfyui\ComfyUI-aki-v1.2\ComfyUI-aki-v1.2\nodes.py", line 1503, in sample
```

このように指定されます。

##### Step 2: オプションを確認する
エラーが発生したノード（ここではKSampler）のオプション設定をチェックします。特に `headdim` の値が64、96、128以外であるかを確認してください。

もし該当のノードで `headdim` を手動で設定している場合は、指定した値が適切なものか確認しましょう。不適切な値は修正します。

##### Step 3: ComfyUIを再インストールする
一度ComfyUIを削除し、最新版をインストールすることで問題が解決することがあります。
- **Step 3.1:** ComfyUIのフォルダを完全に削除します。例えば、`D:\Comfyui\ComfyUI-aki-v1.2` を削除します。
- **Step 3.2:** Pythonの `venv（仮想環境）` も同様にクリーンアップし、新しいものを作成します。（Pythonで仮想環境を削除・作成するコマンドは以下の通りです）

```
python -m venv ComfyUI_env
ComfyUI_env\Scripts\activate
pip install --upgrade pip
pip install comfyui
```

##### Step 4: エラーが解決しない場合の対処法
エラーが解決しなければ、問題を報告するためのGitHub Issueを作成します。以下の情報も追加してください。
- **Node ID:** 3 
- **Node Type:** KSampler
- **Exception Type:** AssertionError

#### よくある質問 (FAQ)

**Q: Pythonの知識がないけど大丈夫？**
A: 大丈夫です！この記事ではPythonの知識を必要とせず、手順を忠実に従っていただければ解決できます。

**Q: 他のノードでも同じエラーが出る？**
A: 「headdim」に関連するパラメータが設定されていないノードは影響を受けません。KSampler以外で同様のエラーが出る場合は、そのノードに特定の設定が必要である可能性があります。

#### まとめ
「headdim should be in [64, 96, 128].」というエラーでもがいている方は、この記事を手元に置きながらステップバイステップで対処してみてください。必ず解決するはずです！あきらめずに頑張ってください。

最後まで読んでいただきありがとうございます！
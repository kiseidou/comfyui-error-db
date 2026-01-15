---
title: "【CivitAI】Support Z Image alipai controlnets. の完全解決ガイド"
description: "ComfyUIのエラー 'Support Z Image alipai controlnets.' の原因と、初心者でもできる修正手順をステップバイステプで解説します。"
pubDate: "2026-01-14"
---

## はじめに

こんにちは！ComfyUIを使っているあなたが「Support Z Image alipai controlnets.」というエラーに出くわして困ったことはありませんか？この記事では、そんなあなたのために手順を詳しく解説します。Pythonやプログラミングについて詳しくなくても大丈夫です。一緒に解決しましょう！

## 原因の解説

まず、「Support Z Image alipai controlnets.」エラーが出る原因は、特定のファイルが正しくロードされていないからだと思われます。このファイルは通常、ComfyUIで使われる「Controlnet」の一種ですが、特別な処理が必要です。

具体的には、該当するファイルが通常のモデルフォルダではなく、「models/model_patches」という別のフォルダに配置されるべきです。そして、そのファイルを正しく読み込むために、「ModelPatchLoader」や「QwenImageDiffsynthControlnet」ノードを使う必要があります。

これらの用語は少し難しそうに聞こえるかもしれませんが、心配しないでください！私があなたをガイドします。

## 解決ステップ (Step-by-Step)

### Step 1: ファイルのダウンロードと移動

まず、以下のリンクからファイルをダウンロードします：

```
https://huggingface.co/alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union/tree/main
```

ここから必要なファイル（通常は`.pt`や`.ckpt`などの拡張子を持つファイル）をダウンロードし、「models/model_patches」フォルダに移動します。

### Step 2: ファイルのパス設定

ComfyUIを開いて、以下の操作を行います：

1. **ノードパレット**から「ModelPatchLoader」ノードをドック上やグラフ上に追加します。
2. 追加した「ModelPatchLoader」ノードで、「Load Path」（または類似のプロパティ）に先ほどダウンロードしたファイルへのパスを指定します。例えば：
   ```
   ./models/model_patches/Z-Image-Turbo-Fun-Controlnet-Unions.pt
   ```

### Step 3: QwenImageDiffsynthControlnetノードの追加

次に、同じように「QwenImageDiffsynthControlnet」ノードをグラフ上に追加します。そして、このノードの入力（Input）セクションで、「ModelPatchLoader」ノードから出力を接続します。

### Step 4: グラフの保存と確認

すべての設定が完了したら、ComfyUI上でグラフを保存して再起動してください。これにより変更内容が反映されます。再度エラーが出なければ、問題は解決したと言えます。

## まとめ

「Support Z Image alipai controlnets.」エラーを解決するには、ファイルの正しい場所への配置と、「ModelPatchLoader」と「QwenImageDiffsynthControlnet」ノードを使用することが必要です。これでComfyUIが正常に動作し、クリエイティブな活動を再開できるはずです。

取り組むことは大変かもしれませんが、一つずつ進めていけば必ず解決できます。頑張ってくださいね！
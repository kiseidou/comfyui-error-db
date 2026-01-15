---

title: "【CivitAI】view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead. の完全解決ガイド"
description: "ComfyUIのエラー 'view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"

---

## はじめに

ComfyUIを使っているときに「view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.」というエラーが出てしまって、どうすればいいのかわからないってことはありませんか？この記事では、そんなときの解決法を初心者向けに詳しく解説します。

## 前提条件

- ComfyUIを使用していること
- Python環境（推奨は`venv`）が整っていること
- Mac Studio M2 Ultra（または同等のデバイス）
- MacOS 15.0 以上

## エラーの原因解説

このエラーは、PythonやPyTorch（深層学習フレームワーク）でtensorというデータ構造を扱うときに発生します。具体的には、tensorが持つデータ配列と視覚的に表示される形状（view）が互いに不適切な関係にある場合に出ます。「.reshape(...)`」を使って形を変える必要があることを教えてくれるエラーです。

PyTorchでは、`tensor.view(size)`や`tensor.reshape(shape)`を使うことで、既存のデータ配列から新しい形状を作成できます。しかし、サイズが適切でない場合、上記のようなエラーが出ます。

## 解決ステップ (Step-by-Step)

### Step 1: エラーログを確認する

まず、エラーメッセージとスタックトレース（エラーの発生元）を確認します。あなたの場合は以下のログからエラーが起きたことがわかります。

```python
File "/Volumes/Extreme_Pro/ComfyUI/custom_nodes/ComfyUI_UltimateSDUpscale/usdu_patch.py", line 66, in new_upscale
    old_upscale(self)
```

ここで、問題となっている`usdu_patch.py`ファイルを確認します。エラーが発生している部分のコードは以下のようなものだと考えられます。

```python
# 假设问题出现在某个reshape操作中，例如：
image_tensor = image_tensor.view(new_shape)  # 这里假设 new_shape 是一个不合适的形状。
```

### Step 2: 関連する Pythonスクリプトを修正する

エラーが発生したスクリプトの該当箇所を確認し、正しい`reshape`操作を行うようにコードを修正します。

1. **ファイルを開く**

    `usdu_patch.py`を開き、その中に書かれているTensorの操作部分を見つけるために、次の行を探します。
    
    ```python
    image_tensor = image_tensor.view(new_shape)
    ```
  
2. **`.reshape()` を使用して修正する**
   
   このエラーは、 `.view()` または `resize` と似たような操作が正しくない形で行われていることを示しているため、その部分を`.reshape(...)`を使って直します。例えば：
    
    ```python
    new_shape = (1, -1)  # 假设new_shape是一个不合适的形状，这里修改为正确的形状。
    image_tensor = image_tensor.reshape(new_shape)
    ```
   
   このようにすることで、Tensorの形を適切に変更できます。

### Step 3: コードを保存してComfyUIを再起動する

修正が完了したら、ファイルを保存し、ComfyUIを再度起動します。これで問題は解決することが多いです。

## よくある質問 (FAQ)

- **Q: ComfyUIのバージョンは何を使えばいいですか？**
  - A: 最新版または最新安定版を使用することを推奨しますが、問題がある場合は公式WikiやGitHub Issueページに詳細情報がありますので確認してください。
  
- **Q: PyTorchのバージョンはどれを選べばよいですか？**
  - A: ComfyUIと互換性のあるPyTorchのバージョンを使用することを推奨します。通常、公式ガイドラインやドキュメントに記載されています。

## まとめ

「view size is not compatible with input tensor's size and stride」エラーが出ても心配しないでください！これは単にtensorの形状を適切に変更するための指示であり、修正方法は簡単です。今回の記事で紹介した手順を試してみてください。きっと解決できるはずです！

これからもComfyUIを使い続けて、クリエイティブな作品作りを楽しんでくださいね！
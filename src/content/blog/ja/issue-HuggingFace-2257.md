---

title: "【HuggingFace】ModuleNotFoundError: No module named 'comfy.options' appeared after installing some custom nodes, now even a fresh install won't start. の完全解決ガイド"
description: "ComfyUIのエラー 'ModuleNotFoundError: No module named 'comfy.options'' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"

---

## はじめに

あなたのプロジェクトが途中で止まってしまった経験はありませんか？特に「ModuleNotFoundError: No module named 'comfy.options'」というエラーが出た時、頭を抱えてしまうかもしれません。でも大丈夫！この記事では初心者向けのステップバイステップの方法で解決策をお伝えします。

## 前提条件

この解説は ComfyUI を使用している Windows や Linux ユーザー向けです。また、Python 環境を理解していない方でも簡単に解決できるようになっています。この記事では仮想環境（venv）を使用しますので、事前に Python のインストールと仮想環境の作成ができることを前提としています。

## 原因の解説

このエラーは、ComfyUI に追加されたカスタムノード（拡張機能）が正しくインストールされていないか、もしくは ComfyUI の本体と互いに干渉している可能性があります。特に既存のカスタムノードをインストールした後に発生する場合が多いです。

## 解決ステップ (Step-by-Step)

### Step 1: カスタムノードのインストールフォルダを確認する

まず、あなたが追加したカスタムノード（拡張機能）のディレクトリがある場所を確認してください。通常は `ComfyUI/extensions/` フォルダ内に格納されます。

### Step 2: コマンドを実行して環境をクリーンアップする

次に、仮想環境内で以下のようなコマンドを順番に実行します。

```bash
# ComfyUIのフォルダで仮想環境をアクティブ化
source venv/bin/activate  # Windowsの場合、 `venv\Scripts\activate` を使用

# ComfyUI依存モジュールを更新または再インストール
pip install -r requirements.txt --upgrade

# カスタムノードが存在するフォルダを削除（バックアップは必ず取ってください）
rm -rf extensions/my_custom_node  # my_custom_nodeは実際にインストールしたカスタムノードの名前です

# ComfyUIを再起動
python3 main.py
```

これらの手順で、ComfyUI の依存関係が最新になり、問題のあるカスタムノードの影響がクリアされます。

### Step 3: カスタムノードのインストールをやり直す

もし上記の手順でもエラーが解決しない場合、カスタムノードのインストールからやり直してみてください。以下のコマンドを実行します：

```bash
# カスタムノードのインストールを再度実行（my_custom_nodeは具体的な名前）
git clone https://github.com/myusername/my_custom_node.git extensions/my_custom_node

# ComfyUIを再起動
python3 main.py
```

もしエラーが解決せず、詳細な情報を得たい場合はログファイルも確認してみてください。

## よくある質問 (FAQ)

### Q: 他のカスタムノードのインストールで同じ問題が出た場合？

他のカスタムノードでも同様の問題が出る場合、それぞれのカスタムノードが互いに依存関係を持っていないか確認してください。また、バージョンが古いカスタムノードを使用している場合、アップデートが必要かもしれません。

### Q: カスタムノード自体に問題がある？

カスタムノードが ComfyUI の仕様と互換性がない場合があります。その場合は、開発者やコミュニティフォーラムで助けを求めると良いでしょう。

## まとめ

「ModuleNotFoundError: No module named 'comfy.options'」というエラーは取り扱いが難しいですが、手順を追って対処すれば解決できます。あなたの問題が直ることを願っています！あきらめずに挑戦してみてくださいね！

この記事があなたの助けになりますように。頑張ってください！
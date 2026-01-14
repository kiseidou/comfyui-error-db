---

### はじめに

あなたはComfyUIを使用していて、「Feauture request: Dynamic Lora Weights」というエラーが出たとお困りではありませんか？この記事では、初心者の方でも簡単に解決できる方法を解説します。このエラーが起こる原因や、どのように対処すれば良いのかを詳しく紹介します。

### 前提条件

- **OS**: Windows
- **環境**: Python 環境（Python 3.7以上）

### 原因の解説

このエラーは、「Dynamic Lora Weights」という拡張機能がインストールされていないか、または正しくインストールされなかった場合に発生します。この拡張機能はLoRAモデルを使用する際に、各生成ステップでの重みを動的に調整できる非常に強力なツールです。

### 解決ステップ (Step-by-Step)

#### Step 1: 拡張機能の確認

まず、「Dynamic Lora Weights」拡張機能がインストールされていることを確認します。既にインストール済みであれば、次の手順を飛ばして問題解決を目指しましょう。

1. ComfyUIの設定画面（または管理ページ）を開きます。
2. 「Extensions」や「Custom Nodes」のセクションを探し、「Dynamic Lora Weights」があるかどうか確認します。

#### Step 2: 拡張機能のインストール

「Dynamic Lora Weights」が見つからない場合、以下の手順でインストールを行います。Pythonの仮想環境`venv`を使用して作業を進めましょう。

1. Pythonのターミナルを開きます。
2. 拡張機能のGitHubリポジトリから最新版のzipファイルをダウンロードします（リンク：https://github.com/cheald/sd-webui-loractl）。
3. ダウンロードしたzipファイルを解凍し、ComfyUIのextensionsフォルダに移動させます。

```bash
cd ~/path/to/comfyui/extensions/
unzip /path/to/downloaded/dynamic_lora_weights.zip -d dynamic_lora_weights
```

4. 拡張機能がインストールされたことを確認するために、以下のコマンドを実行します：

```bash
pip install --upgrade -r ./dynamic_lora_weights/requirements.txt
```

5. 最後にComfyUIを再起動し、「Dynamic Lora Weights」の設定画面を開いてみてください。エラーが消えていれば問題解決です！

### よくある質問 (FAQ)

- **Q**: リポジトリから直接インストールできない場合、どのようにしたら良いですか？
  - **A**: GitHubリポジトリをクローンする方法もあります。
    ```bash
    git clone https://github.com/cheald/sd-webui-loractl.git dynamic_lora_weights
    ```
- **Q**: Python環境が問題でエラーが出る場合、どうしたら良いですか？
  - **A**: ComfyUIのPython環境を新たに作成し直すか、別の仮想環境`venv`を作り直してみてください。

### まとめ

このエラーは「Dynamic Lora Weights」拡張機能がインストールされていないため起こるものです。手順通りに行うことで簡単に解決できます。もし何かトラブルがあれば、ComfyUIのフォーラムやコミュニティに質問すると良いでしょう！あきらめずに挑戦しましょう！
---
title: "【CivitAI】HIP error: invalid device function when running ComfyUI の完全解決ガイド"
description: "ComfyUIのエラー 'HIP error: invalid device function when running ComfyUI' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"
---

### 本文構成

#### はじめに
ComfyUIを使って素晴らしい画像を作ろうとしている中で、突然エラーが表示されて作業ができなくなることは大変ストレスフルですね。「HIP error: invalid device function when running ComfyUI」ってどんなエラーか知っていますか？これはGPUの問題から起こることが多いんですが、心配しないでください。この記事では、あなたを助けて解決する方法をお伝えします。

#### 前提条件
この解説は Windows / Python 環境を想定していますが、Linux や macOSでも同様に適用できるステップです。Python仮想環境（venv）を使ってComfyUIをインストールしていることを確認してください。

#### 原因の解説
エラー "HIP error: invalid device function" は主にGPUドライバーとCUDAやROCmなどの計算ライブラリとの間で問題が起きたときに発生します。特にRadeon GPU（この場合はAMD Radeon RX 5700 XT）を使う場合、必要な設定が正しく行われていない可能性があります。

具体的には、AMDのGPUではHIPというOpenCLベースのフレームワークを使いますが、これが正しく設定されていないとエラーが発生することがあります。また、ComfyUIはPyTorchやその他の深度学習ライブラリを必要とするため、これらのライブラリも適切にインストールされている必要があります。

#### 解決ステップ (Step-by-Step)
1. **必要なライブラリを更新する**
   まず、Pythonの仮想環境（venv）で次のコマンドを実行して、必要なパッケージを最新の状態に保ちます。これにより依存関係のバージョンミスマッチや古すぎるインストールなどが解決されます。
   
   ```bash
   pip install --upgrade pip
   pip install --upgrade torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
   ```
   プロジェクトが特定のバージョンを必要とする場合、そのバージョンを明示的に指定してください。

2. **AMD GPUドライバーとHIP環境を確認する**
   AMD GPUを使っている場合、公式サイトから最新版のGPUドライバーをインストールします。その後、HIP環境も適切にセットアップされていることを確認します。
   
   ```bash
   sudo apt-get update
   sudo apt-get install rocm-dev hipblas hipfft hipsparse miopen-hip rocminfo
   ```
   上記のコマンドはLinux用ですが、WindowsやmacOSではAMDの公式サイトで提供されるインストーラーを使用してください。

3. **ComfyUIを再起動する**
   すべての設定が完了したら、Python仮想環境を再度アクティブにしてから、ComfyUIを起動します。
   
   ```bash
   source venv/bin/activate  # Python仮想環境を有効化
   python /path/to/ComfyUI/app.py  # ComfyUIを実行
   ```

#### よくある質問 (FAQ)
- **Q: 上記のコマンドがうまく動かない場合**
  - A: 環境変数やCUDA/ROCmのパス設定が不適切な可能性があります。その場合は、プロジェクトルートディレクトリに移動し、`export` コマンドを使ってCUDAやHIPのPATHを手動で指定してみてください。

#### まとめ
エラーが出ても慌てないでください！これは通常の開発プロセスの一環であり、適切な知識と手順さえあれば必ず解決できます。また、問題が続く場合はプロジェクトのコミュニティーやサポートチャネルに相談することもおすすめします。

これで直ります！頑張ってみてくださいね！

---

この記事は初心者向けに分かりやすく書かれていますので、ComfyUIを使っているけどプログラミング言語については詳しくない方でも安心してご利用いただけます。
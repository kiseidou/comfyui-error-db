---
title: "【ComfyUI】XPU out of memory Error after LoadImage and KSampler の完全解決ガイド"
description: "ComfyUIのエラー 'XPU out of memory Error after LoadImage and KSampler' の原因と、初心者でもできる修正手順をステップバイステップで解説します。"
pubDate: "2026-01-13"
---

### 【本文構成】

#### はじめに

ComfyUIを使って画像生成をしているときに、「XPU out of memory Error」というエラーが出て、困っている方は多いと思います。この記事では、そんなあなたを助けるために、具体的な解決方法とその理由を詳しく解説します。

#### 前提条件

- このガイドは **Windows** または **Python環境** を想定しています。
- ComfyUIをインストールし、基本的な操作ができます。

#### 原因の解説

このエラーは「XPU（Cross Process Unit）」という概念と関連があります。ComfyUIでは、画像処理や生成には大きなデータが必要で、これらのデータをGPUメモリに保持しようとすると、メモリが不足することがあります。

具体的には、LoadImage、PadImageForInpainting、VAEencode（または単純な LoadImage--VAEencode）のノード構成を使用したとき、特定の状況下でGPUのメモリが十分に確保できず、「XPU out of memory」エラーが発生します。特に、128GiBという大きな要求が出ており、これは通常ではあり得ない値です。

この128GiBの要求は、モデルや画像データの処理中に一時的に必要とされるメモリサイズを表しており、一般的なGPU（例えば50GB以下）には確保できません。これがエラーの主な原因となります。

#### 解決ステップ (Step-by-Step)

1. **問題発生時に`empty_cache()`を実行する**

   エラーが発生した直後に、Pythonのコンソールやスクリプト内で以下のコマンドを実行します。これにより、未使用のメモリが解放されます。

   ```python
   import comfy.samplers
   comfy.samplers.empty_cache()
   ```

2. **VAEの設定を調整する**

   ComfyUIでは、自動で適切なVAE（変分自己_ENCODER）モデルを使用しますが、時には手動で指定した方が良い場合があります。例えば、以下のようにVAEモデルを直接指定してみてください。

   ```python
   VAE = "your_custom_vae_model_path"  # このパスはあなたの環境に適したものを使用してください。
   ```

3. **ノード構成の最適化**

   - LoadImageとVAEencode間で他のノード（例えばDownscaleやUpscale）を追加することで、必要なメモリ容量を抑えることができます。

4. **GPUメモリ設定を変更する**

   ComfyUIの設定ファイルに以下の値を追加します。これにより、ComfyUIが使用できるGPUメモリ量を制限することができます。

   ```python
   comfy.model_management.set_max_memory("cuda", "15GB")  # あなたのGPUサイズに合わせて適宜調整してください。
   ```

#### よくある質問 (FAQ)

**Q: なぜこのエラーは他のノード構成では発生しないのですか？**

A: このエラーが特定のノード構成でしか発生しないのは、その構成によってメモリ使用量が極端に増えるからです。特にLoadImageとVAEencodeの組み合わせは大量のデータを処理するため、多くの場合問題になります。

**Q: このエラーを完全に解消する方法はあるのでしょうか？**

A: 完全な解決策がないわけではありませんが、上記のような手順で大部分のケースでは問題が軽減されます。それでも難しい場合は、ComfyUIの開発者コミュニティやサポートへ相談することをお勧めします。

#### まとめ

「XPU out of memory Error」は、複雑な画像処理においてメモリ管理に問題を引き起こす可能性がありますが、上記の手順により改善することが可能です。あきらめずに試してみてください！
---
title: "【ComfyUI】SingleStreamBlock.forward() got an unexpected keyword argument 'modulation_dims_img'"
description: "ComfyUI Error: SingleStreamBlock.forward() got an unexpected keyword argument 'modulation_dims_img'"
pubDate: "2026-01-14"
---
### 【ComfyUI】SingleStreamBlock.forward() got an unexpected keyword argument 'modulation_dims_img' の完全解決ガイド

description: ComfyUIのエラー 'SingleStreamBlock.forward() got an unexpected keyword argument 'modulation_dims_img'' の原因と、初心者でもできる修正手順をステップバイステップで解説します。
pubDate: 2026-01-14


こんにちは！ComfyUIを使っている方の中には、「SingleStreamBlock.forward() got an unexpected keyword argument 'modulation_dims_img'」というエラーに出くわした経験がある方もいるでしょう。この記事では、その原因と解決方法を詳しく説明します。

### はじめに

「SingleStreamBlock.forward() got an unexpected keyword argument 'modulation_dims_img'」と表示されたら、ComfyUIの最新版を使用しているときに発生する可能性が高いエラーです。特にSamplerCustomAdvancedという機能を使ってビデオ生成をしている場合に多いようです。

### 前提条件

この解説は、Windows環境を想定しています。また、Pythonがインストールされていることを前提とします。venv（仮想環境）を使用している場合は、適切な仮想環境がアクティブであることを確認してください。

### エラーの原因

このエラーは、ComfyUIのコードベースに変更があったときに発生します。「modulation_dims_img」がSingleStreamBlockクラスで受け入れる引数として定義されていないために起こります。通常、これは新しいバージョンでの不整合や機能追加によって引き起こされることが多いです。

### 解決ステップ (Step-by-Step)

#### Step 1: ComfyUIの最新版を確認する

エラーが発生したときにはまず、使用しているComfyUIのバージョンと現在公開されている最新版を比較することが重要です。新しいバージョンでは問題が修正されている可能性があります。

```
# バージョン情報を表示します
git tag -l
```

#### Step 2: 更新前の状態に戻す

もし最新版で問題が解決していない場合、エラーが発生する直前の状態（つまり、更新前）にロールバックすることを検討しましょう。

```
# ブランチのリストを表示します
git branch

# 以前のコミットに戻ります (具体的なコミットハッシュが必要です)
git checkout <commit_hash>
```

その後、再度エラー発生前の状態でComfyUIを実行してみましょう。この方法であれば、最新版に含まれる不具合や変更点を避けることができます。

### よくある質問 (FAQ)

**Q: ComfyUIのバージョンを管理するにはどうすればよいですか？**

- A: Gitを使用することでバージョンの追跡が容易になります。特に、「tag」と「branch」を上手に使うことで、特定の状態の復元や更新履歴の確認が可能になります。

**Q: Pythonの仮想環境（venv）を使うとどんな利点がありますか？**

- A: 仮想環境を使用することで、プロジェクト毎に異なるバージョンのライブラリをインストールし、依存関係を管理できます。これにより、複数のプロジェクト間での相互干渉を防ぐことができます。

### まとめ

ComfyUIでエラーに出くわしても、諦めずに最新情報や既知の問題の修正版を探してみましょう。技術的な詳細に惑わされず、基本的な手順から解決を目指すことが大切です。この記事が皆さんの問題解決の一助になれば幸いです！
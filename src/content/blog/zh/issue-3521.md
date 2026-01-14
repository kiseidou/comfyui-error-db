---
title: "【ComfyUI】After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5 修复指南"
description: "Fix: After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5"
pubDate: "2026-01-14"
---
### 正文

#### 问题描述
最近在使用 ComfyUI 进行工作流程操作时，发现大部分的操作步骤都会导致图像变成黑色。经过多次测试后确定是“Karras”调度器引发的问题。

#### 解决方案

**背景信息：**
当你更新了 ComfyUI 或者你的系统环境发生了变化（如 macOS 更新）后，可能会遇到一些不兼容的情况。在这种情况下，“Karras”调度器会触发一个导致图像显示为黑色的错误。

**步骤 1: 切换到另一个调度器**

首先尝试改变使用的调度器来解决这个问题。在 ComfyUI 中切换调度器的方法如下：

- 打开你的工作流程文件。
- 寻找并修改涉及到“Karras”调度器的部分，将其改为其他可用的调度器（如 "DDIM" 或 "PNDM"）。

**步骤 2: 更新相关依赖库**

有时候问题可能源于一些 Python 库版本不匹配。确保你安装了所有必要的库，并且它们都是最新的：

```bash
pip install --upgrade pip
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
pip install -r requirements.txt  # 根据你的环境调整这条命令，确保安装所有必需的依赖项。
```

**步骤 3: 检查 CUDA 版本**

由于你使用的是 Mac mini M2 pro，并且 macOS 上默认不支持 CUDA（这主要影响运行在 GPU 上的操作）。所以如果 ComfyUI 中有需要 GPU 支持的部分，可能需要调整这些部分以适应 CPU 或者寻找适合 M1/M2 架构的替代方案。

**步骤 4: 确认环境兼容性**

查看 ComfyUI 的官方文档或者 GitHub 页面来确认你的操作系统版本（macOS Sonoma 14.5）和硬件配置（Mac mini M2 pro）是否完全支持，如果有其他用户报告了相似的问题，请尝试他们的解决方法。

**步骤 5: 寻求社区帮助**

如果上述措施都不能解决问题，可以考虑在 ComfyUI 的 GitHub issue 页面或者相关的论坛上寻求更多的帮助。确保你已经详尽地描述了你的问题，并提供了所有可能有用的调试信息（例如日志文件、错误代码等）。

通过以上五个步骤的执行，大多数情况下都可以解决“After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5”的问题。希望对你有所帮助！